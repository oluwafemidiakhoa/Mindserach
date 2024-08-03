import os
from openai import OpenAI
from src.web_planner import WebPlanner
from src.web_searcher import WebSearcher
from src.config import Config

client = OpenAI(api_key=Config.OPENAI_API_KEY)

class MindSearch:
    def __init__(self):
        self.planner = WebPlanner()
        self.searcher = WebSearcher()
    
    def process_query(self, query):
        sub_questions = self.planner.decompose_query(query)
        answers = []
        for sub_question in sub_questions:
            info = self.searcher.retrieve_info(sub_question)
            if info:
                answers.append(self.integrate_info(info))
            else:
                answers.append(f"No specific context provided for sub-question: {sub_question}")
        return self.generate_response(query, answers)
    
    def integrate_info(self, info):
        return ' '.join(info)
    
    def generate_response(self, query, context):
        context_text = ' '.join(context) if context else "No specific context provided."
        prompt = f"Answer the following query based on the provided context:\nQuery: {query}\nContext: {context_text}"
        response = client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt}
            ]
        )
        return response.choices[0].message.content.strip()

if __name__ == "__main__":
    query = "Explain the impact of climate change on agriculture and what measures can be taken"
    mindsearch = MindSearch()
    result = mindsearch.process_query(query)
    print(result)
