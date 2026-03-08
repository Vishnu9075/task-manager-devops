from sqlalchemy.orm import Session
from app.models import Task
from app.schemas import TaskCreate, TaskUpdate

def create_task(db: Session, payload: TaskCreate) -> list[Task]:
    task = Task(title= payload.title, description= payload.description)
    db.add(task)
    db.commit()
    db.refresh(task)
    return task

def list_tasks(db:Session) -> list[Task]:
    return db.query(Task).order_by(Task.id.desc()).all()


def get_task(db: Session, task_id: int) -> Task | None:
    return db.query(Task).filter(Task.id == task_id).first()

def update_task(db: Session, task_id: int, payload:TaskUpdate) -> Task | None:
    task = get_task(db, task_id)
    if not task:
        return None
    
    if payload.title is not None:
        task.title = payload.title
    if payload.description is not None:
        task.description = payload.description
    if payload.completed is not None:
        task.completed = payload.completed

    db.commit()
    db.refresh(task)
    return task


def delete_task(db: Session, task_id: int) -> bool:
    task = get_task(db, task_id)
    if not task:
        return False
    db.delete(task)
    db.commit()
    return True