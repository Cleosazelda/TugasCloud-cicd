from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}}) 

data = [
    {"id": 1, "name": "Yudha", "role": "Cloud Architect"}
]

@app.route('/api/data', methods=['GET'])
def get_data():
    return jsonify(data)

@app.route('/api/data', methods=['POST'])
def add_data():
    new_item = request.json
    new_item['id'] = len(data) + 1
    data.append(new_item)
    return jsonify(new_item)

@app.route('/api/data/<int:id>', methods=['PUT'])
def update_data(id):
    for item in data:
        if item['id'] == id:
            item['name'] = request.json.get('name', item['name'])
            item['role'] = request.json.get('role', item['role'])
            return jsonify(item)
    return {"message": "Not found"}, 404

@app.route('/api/data/<int:id>', methods=['DELETE'])
def delete_data(id):
    global data
    data = [item for item in data if item['id'] != id]
    return {"message": "Deleted"}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)