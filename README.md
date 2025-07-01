# Todo REST API

A simple Flask-based REST API for managing todos. Integrated with Jenkins for CI.

## Endpoints
- `GET /todos`: Get all todos
- `POST /todos`: Add a new todo (`{"task": "Do something"}`)
- `DELETE /todos/<index>`: Delete a todo

## Setup
```bash
pip install -r requirements.txt
python app.py
