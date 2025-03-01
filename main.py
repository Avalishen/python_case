from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List
from database import get_db
from schemas import TaskResponse, TaskCreate
from crud import get_tasks, get_task, create_task, update_task, delete_task
from pydantic import BaseModel


app = FastAPI()


#Получение всех задач
@app.get("/tasks", response_model=List[TaskResponse])
async def read_tasks(db: AsyncSession = Depends(get_db)):
    return await get_tasks(db)

#Получение конкретной задачи
@app.get("/tasks/{task_id}", response_model=TaskResponse)
async def read_task(task_id: int, db: AsyncSession = Depends(get_db)):
    task = await get_task(db, task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Задача не найдена")
    return task

#Создание задачи
@app.post("/tasks", response_model=TaskResponse)
async def create_new_task(task: TaskCreate, db: AsyncSession = Depends(get_db)):
    return await create_task(db, task)

#Обновление задачи
@app.put("/tasks/{task_id}", response_model=TaskResponse)
async def update_existing_task(task_id: int, task: TaskCreate, db: AsyncSession = Depends(get_db)):
    updated_task = await update_task(db, task_id, task)
    if not updated_task:
        raise HTTPException(status_code=404, detail="Задача не найдена")
    return updated_task

#Удаление задачи
@app.delete("/tasks/{task_id}", status_code=204)
async def delete_existing_task(task_id: int, db: AsyncSession = Depends(get_db)):
    success = await delete_task(db, task_id)
    if not success:
        raise HTTPException(status_code=404, detail="Задача не найдена")
    return
