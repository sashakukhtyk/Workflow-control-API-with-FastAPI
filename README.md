# Workflow-control-API-with-FastAPI
## Description
This is a workflow control API built with FastAPI. It allows users to manage and control workflows in their applications.

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
- Sqalchemy: A SQL toolkit and Object-Relational Mapping (ORM) library for Python.

## Usage
1. Start the FastAPI server: `uvicorn main:app --reload`
2. Open your browser and go to `http://localhost:8000/docs` to access the Swagger UI documentation.
3. Use the provided endpoints to interact with the API.

## API Endpoints
- `POST /workflow/create`: Create a new workflow
- `PUT /workflow/update/{workflow_id}`: Update nodes
- `DELETE /workflow/delete/{workflow_id}`: Delete a workflow
- `POST /workflow/add_node/{workflow_id}`: Add a node to a workflow
- `POST /workflow/add_edge/{workflow_id}`: Add a dependency between nodes in a workflow
- `POST /workflow/path`: Retrieve the shortest path between two nodes in a workflow

## Contributing
Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.
