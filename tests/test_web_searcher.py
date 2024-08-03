# test_web_searcher_manual.py
from src.web_searcher import WebSearcher

def main():
    searcher = WebSearcher()
    query = "What is AI"
    results = searcher.search(query)
    for result in results:
        print(result)

if __name__ == "__main__":
    main()
