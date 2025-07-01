
# 📝 Task Manager API

A simple task management REST API built with **FastAPI** and **Poetry** to demonstrate modern Python web development practices.

---

## 🚀 Features

- **CRUD Operations**: Create, Read, Update, Delete tasks  
- **Status Management**: Track task progress (pending, in_progress, completed)  
- **Automatic Documentation**: Interactive API docs with Swagger UI  
- **Type Safety**: Full type hints with Pydantic models  
- **Testing**: Comprehensive test suite with pytest  
- **Modern Tooling**: Poetry for dependency management  

---

## 🛠️ Tech Stack

- **FastAPI** – Web framework  
- **Pydantic** – Data validation  
- **Uvicorn** – ASGI server  
- **Poetry** – Dependency management  
- **Pytest** – Testing  

---

## 📋 Prerequisites

- Python 3.8 or higher  
- Poetry installed

### 📦 Installing Poetry

```
# Windows (PowerShell)
(Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | py -

# macOS/Linux
curl -sSL https://install.python-poetry.org | python3 -

# Or with pip
pip install poetry

```

## 🏗️ Project Structure

```
task-manager-api/
├── app/
│   ├── __init__.py
│   ├── main.py          # FastAPI application
│   ├── models.py        # Pydantic models
│   └── database.py      # In-memory database operations
├── tests/
│   ├── __init__.py
│   └── test_main.py     # Test cases
├── pyproject.toml       # Poetry configuration
└── README.md

```

## 🚀 Quick Start

```
git clone <your-repo-url>
cd task-manager-api
poetry install

```
## Run the App
```
poetry run uvicorn app.main:app --reload
# or with custom host/port
poetry run uvicorn app.main:app --reload --host 0.0.0.0 --port 8000

```

##  Open in Browser
```
Swagger UI: http://localhost:8000/docs

ReDoc: http://localhost:8000/redoc
```

```
| Method | Endpoint                 | Description            |
| ------ | ------------------------ | ---------------------- |
| GET    | `/`                      | Welcome message        |
| POST   | `/tasks/`                | Create a task          |
| GET    | `/tasks/`                | List all tasks         |
| GET    | `/tasks/{task_id}`       | Get task by ID         |
| PUT    | `/tasks/{task_id}`       | Update task            |
| DELETE | `/tasks/{task_id}`       | Delete task            |
| GET    | `/tasks/status/{status}` | Filter tasks by status |

```

## 🧪 Testing
```
# Run tests
poetry run pytest

# With coverage
poetry run pytest --cov=app

# Verbose mode
poetry run pytest -v

```


## 🧾 Usage Examples

```
# Create task
curl -X POST http://localhost:8000/tasks/ \
  -H "Content-Type: application/json" \
  -d '{"title": "Learn FastAPI", "description": "Build a simple API with FastAPI", "status": "pending"}'

# Get all tasks
curl http://localhost:8000/tasks/

# Get task by ID
curl http://localhost:8000/tasks/1

# Update task
curl -X PUT http://localhost:8000/tasks/1 \
  -H "Content-Type: application/json" \
  -d '{"status": "completed"}'

# Delete task
curl -X DELETE http://localhost:8000/tasks/1

# Get tasks by status
curl http://localhost:8000/tasks/status/pending

```

## 🔧 Development Notes

```
ADD DEPENDENCIES

poetry add requests
poetry add --group dev black flake8
poetry add --optional redis

CODE FORMATTING

poetry add --group dev black isort
poetry run black app/ tests/
poetry run isort app/ tests/

ENVIRONMENT INFO

poetry env info
poetry show --tree
poetry show --outdated

```

## 🎯 Learning Objectives

### Poetry
- Easy dependency management

- Isolated virtual environments

- Reproducible builds

- Modern Python packaging

