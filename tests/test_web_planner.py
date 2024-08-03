# tests/test_web_planner.py
import unittest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))
from src.web_planner import WebPlanner

class TestWebPlanner(unittest.TestCase):
    def setUp(self):
        self.planner = WebPlanner()

    def test_decompose_query(self):
        query = "What is AI and how does it work"
        sub_questions = self.planner.decompose_query(query)
        self.assertEqual(len(sub_questions), 2)
        self.assertIn("What is AI", sub_questions)
        self.assertIn("how does it work", sub_questions)

if __name__ == "__main__":
    unittest.main()
