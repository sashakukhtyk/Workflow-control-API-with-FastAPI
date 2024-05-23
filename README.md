# Workflow-control-API-with-FastAPI
## Description
This is a workflow control API built with FastAPI. It allows users to manage and control workflows in their applications.

### YouTube video "https://youtu.be/qGAyL8SlB8Q"

## Features
- Create new workflows
- Add tasks to workflows
- Update task status
- Retrieve workflow details
- Delete workflows

## Installation
1. Clone the repository: `git clone https://github.com/sashakukhtyk/Workflow-control-API-with-FastAPI.git`
2. Navigate to the project directory: `cd Workflow-control-API-with-FastAPI`
3. Install the dependencies: `pip install -r requirements.txt`

## Stack of Technologies
- FastAPI: A modern, fast (high-performance) web framework for building APIs with Python 3.7+.
- Python: A powerful, high-level programming language.
- Uvicorn: A lightning-fast ASGI server implementation, perfect for FastAPI.
- Pydantic: A runtime data validation and parsing library for Python.
- NetworkX: A Python package for the creation, manipulation, and study of the structure, dynamics, and functions of complex networks.
- Pytest: A testing framework for Python.
- SQLAlchemy: A SQL toolkit and Object-Relational Mapping (ORM) library for Python.

## Usage
1. Start the FastAPI server: `uvicorn main:app --reload`
2. Open your browser and go to `http://localhost:8000/docs` to access the Swagger UI documentation.
3. Use the provided endpoints to interact with the API.

## API Endpoints
- `POST /start_node`: Add a start node to the graph manager.
- `POST /message_node`: Add a message node to the graph manager.
- `POST /condition_node`: Add a condition node to the graph manager.
- `POST /end_node`: Add an end node to the graph manager.
- `GET /run_workflow/{start_node_id}/{end_node_id}`: Find the path between the start node and end node in the graph manager.

## Contributions
Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.
