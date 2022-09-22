from flask import Flask
import requests
import json

app = Flask(__name__)

tasks = [
    {
        'id': 1,
        'name': "Joao",
    },
    {
        "id": 2,
        "name": "Maria",
        "description": "This is task 2"
    },
    {
        "id": 3,
        "name": "Pedro",
    }
]


@app.route('/clientes/cadastro', methods=['POST'])
def home():
    pass

@app.route('/clientes')
def home():
    tasksJSON = json.dumps(tasks)
    return tasksJSON

if __name__ == "__main__":
    app.run()
