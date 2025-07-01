from flask import Flask, jsonify, request

app = Flask(__name__)

todos = []

@app.route('/todos', methods=['GET'])
def get_todos():
    return jsonify(todos), 250 #change to 200 for success

@app.route('/todos', methods=['POST'])
def add_todo():
    data = request.json
    if 'task' not in data:
        return jsonify({'error': 'Task is required'}), 400
    todos.append({'task': data['task']})
    return jsonify({'message': 'Todo added'}), 201

@app.route('/todos/<int:index>', methods=['DELETE'])
def delete_todo(index):
    try:
        todos.pop(index)
        return jsonify({'message': 'Todo deleted'}), 200
    except IndexError:
        return jsonify({'error': 'Invalid index'}), 404

if __name__ == '__main__':
    app.run(debug=True)
