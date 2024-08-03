import networkx as nx

class WebPlanner:
    def __init__(self):
        self.graph = nx.DiGraph()
    
    def decompose_query(self, query):
        # More sophisticated query decomposition logic
        sub_questions = self.split_into_clauses(query)
        for i, sub_question in enumerate(sub_questions):
            self.graph.add_node(i, question=sub_question.strip())
            if i > 0:
                self.graph.add_edge(i-1, i)
        return sub_questions
    
    def split_into_clauses(self, query):
        # Placeholder for advanced query splitting logic
        return query.split(' and ')
    
    def get_sub_questions(self):
        return [self.graph.nodes[n]['question'] for n in self.graph.nodes]
