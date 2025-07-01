from fastapi import FastAPI, HTTPException, status
from typing import List
from .models import Task, TaskCreate, TaskUpdate
from .database import create_task, get_tasks, get_task, update_task, delete_task

# Create FastAPI instance
app = FastAPI(
    title="Task Manager API",
    description="A simple task management API built with FastAPI",
    version="0.1.0"
)

@app.get("/")
async def root():
    return {"message": "Welcome to Task Manager API"}

@app.post("/tasks/", response_model=Task, status_code=status.HTTP_201_CREATED)
async def create_new_task(task: TaskCreate):
    """Create a new task"""
    return create_task(task)

@app.get("/tasks/", response_model=List[Task])
async def read_tasks():
    """Get all tasks"""
    return get_tasks()

@app.get("/tasks/{task_id}", response_model=Task)
async def read_task(task_id: int):
    """Get a specific task by ID"""
    task = get_task(task_id)
    if not task:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Task not found"
        )
    return task

@app.put("/tasks/{task_id}", response_model=Task)
async def update_existing_task(task_id: int, task_update: TaskUpdate):
    """Update a task"""
    task = update_task(task_id, task_update)
    if not task:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Task not found"
        )
    return task

@app.delete("/tasks/{task_id}")
async def delete_existing_task(task_id: int):
    """Delete a task"""
    if not delete_task(task_id):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Task not found"
        )
    return {"message": "Task deleted successfully"}

@app.get("/tasks/status/{status}")
async def get_tasks_by_status(status: str):
    """Get tasks filtered by status"""
    all_tasks = get_tasks()
    filtered_tasks = [task for task in all_tasks if task.status == status]
    return filtered_tasks