from flask import Flask, jsonify, request
from maxheap import MaxHeap
import requests
import json

app = Flask(__name__)

data = requests.get('http://127.0.0.1:8000/comentarios')
data = data.json()

co_bus_heap = MaxHeap()
co_bus_heap.buildHeap(data)
rpt = co_bus_heap.sortedList(5)

@app.route('/prueba', methods=['GET'])
def prueba():
    response = jsonify(rpt)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

if __name__ == '__main__':
    app.run(debug=True, port=5000)