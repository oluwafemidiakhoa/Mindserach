from flask import Flask, request, jsonify, render_template
from src.mindsearch import MindSearch

app = Flask(__name__)
mindsearch = MindSearch()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/query', methods=['POST'])
def query():
    data = request.json
    if 'query' not in data:
        return jsonify({'error': 'Query not provided'}), 400
    query = data['query']
    response = mindsearch.process_query(query)
    return jsonify({'response': response})

@app.route('/favicon.ico')
def favicon():
    return '', 204

if __name__ == "__main__":
    app.run(debug=True)
