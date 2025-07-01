from typing import List, Optional
from datetime import datetime
from .models import Task, TaskCreate, TaskUpdate, TaskStatus

# In-memory database for simplicity
tasks_db: List[Task] = []
next_id = 1

def create_task(task_data: TaskCreate) -> Task:
    global next_id
    now = datetime.now()
    task = Task(
        id=next_id,
        title=task_data.title,
        description=task_data.description,
        status=task_data.status,
        created_at=now,
        updated_at=now
    )
    tasks_db.append(task)
    next_id += 1
    return task

def get_tasks() -> List[Task]:
    return tasks_db

def get_task(task_id: int) -> Optional[Task]:
    return next((task for task in tasks_db if task.id == task_id), None)

def update_task(task_id: int, task_update: TaskUpdate) -> Optional[Task]:
    task = get_task(task_id)
    if not task:
        return None
    
    update_data = task_update.model_dump(exclude_unset=True)
    for field, value in update_data.items():
        setattr(task, field, value)
    
    task.updated_at = datetime.now()
    return task

def delete_task(task_id: int) -> bool:
    global tasks_db
    task = get_task(task_id)
    if not task:
        return False
    
    tasks_db = [t for t in tasks_db if t.id != task_id]
    return True