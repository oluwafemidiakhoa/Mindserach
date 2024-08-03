import requests
from bs4 import BeautifulSoup
from src.config import Config
from src.cache import get_cache, set_cache

class WebSearcher:
    def __init__(self):
        self.search_url = Config.SEARCH_URL
        self.additional_sources = Config.ADDITIONAL_SOURCES

    def search(self, query):
        cached_results = get_cache(query)
        if cached_results:
            return cached_results

        all_results = self.search_google(query)
        for source in self.additional_sources:
            all_results.extend(self.search_additional_source(source, query))

        set_cache(query, all_results)
        return all_results

    def search_google(self, query):
        try:
            response = requests.get(self.search_url + query, timeout=10)
            response.raise_for_status()
            soup = BeautifulSoup(response.text, 'html.parser')
            results = []
            for g in soup.find_all('div', class_='g'):
                anchors = g.find_all('a')
                if anchors:
                    url = anchors[0]['href']
                    title = g.find('h3').text if g.find('h3') else 'No Title'
                    results.append({'title': title, 'url': url})
            return results
        except requests.RequestException as e:
            print(f"Error during search: {e}")
            return []

    def search_additional_source(self, base_url, query):
        try:
            response = requests.get(base_url + query, timeout=10)
            response.raise_for_status()
            data = response.json()
            results = [{'title': item['title'], 'url': item['url']} for item in data['results']]
            return results
        except requests.RequestException as e:
            print(f"Error during search: {e}")
            return []

    def retrieve_info(self, query):
        search_results = self.search(query)
        detailed_info = []
        for result in search_results:
            content = self.get_page_content(result['url'])
            if content:
                detailed_info.append(content)
            else:
                detailed_info.append(f"No detailed information found for URL: {result['url']}")
        return detailed_info

    def get_page_content(self, url):
        cached_content = get_cache(url)
        if cached_content:
            return cached_content

        try:
            response = requests.get(url, timeout=10)
            response.raise_for_status()
            soup = BeautifulSoup(response.text, 'html.parser')
            paragraphs = soup.find_all('p')
            content = ' '.join([p.get_text() for p in paragraphs])
            set_cache(url, content)
            return content
        except requests.RequestException as e:
            print(f"Error retrieving page content: {e}")
            return ""
