from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from models import TaskDB
from schemas import TaskCreate
from datetime import datetime


async def get_tasks(db: AsyncSession):
    result = await db.execute(select(TaskDB))
    return result.scalars().all()


async def get_task(db: AsyncSession, task_id: int):
    return await db.get(TaskDB, task_id)


async def create_task(db: AsyncSession, task: TaskCreate):
    new_task = TaskDB(
        title=task.title,
        description=task.description,
    )
    db.add(new_task)
    await db.commit()
    await db.refresh(new_task)  # Обновляем объект, чтобы получить ID и даты
    return new_task


from datetime import datetime, timedelta

async def update_task(db: AsyncSession, task_id: int, task: TaskCreate):
    db_task = await db.get(TaskDB, task_id)
    if not db_task:
        return None


    db_task.title = task.title
    db_task.description = task.description


    db_task.updated_at = datetime.utcnow() + timedelta(hours=3)

    await db.commit()
    await db.refresh(db_task)
    return db_task


async def delete_task(db: AsyncSession, task_id: int):
    db_task = await db.get(TaskDB, task_id)
    if not db_task:
        return None
    await db.delete(db_task)
    await db.commit()
    return True
