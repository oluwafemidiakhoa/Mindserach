# tests/test_mindsearch.py
import unittest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))
from src.mindsearch import MindSearch

class TestMindSearch(unittest.TestCase):
    def setUp(self):
        self.mindsearch = MindSearch()

    def test_process_query(self):
        query = "Explain the impact of climate change on agriculture and what measures can be taken"
        result = self.mindsearch.process_query(query)
        self.assertTrue(len(result) > 0)

if __name__ == "__main__":
    unittest.main()
