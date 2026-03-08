from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.db import get_db
from app import crud, schemas

router = APIRouter(prefix="/tasks", tags=["tasks"])


@router.post("/", response_model= schemas.TaskResponse, status_code=status.HTTP_201_CREATED)
def create_task(payload: schemas.TaskCreate, db:Session= Depends(get_db)):
    return crud.create_task(db, payload)

@router.get("/", response_model=list[schemas.TaskResponse])
def list_tasks(db: Session= Depends(get_db)):
    return crud.list_tasks(db)


@router.get("/{task_id}", response_model= schemas.TaskResponse)
def get_task(task_id : int, db: Session= Depends(get_db)):
    task = crud.get_task(db, task_id)
    if not task:
        return HTTPException(status_code=404, detail="task not found")
    return task

@router.put("/{task_id}", response_model=schemas.TaskResponse)
def update_task(task_id: int, payload: schemas.TaskUpdate, db: Session = Depends(get_db)):
    task = crud.update_task(db, task_id, payload)
    if not task:
        raise HTTPException(status_code=404, detail="task not found")
    return task

@router.delete("/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_task(task_id: int, db: Session = Depends(get_db)):
    deleted = crud.delete_task(db, task_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Task not found")
    return None