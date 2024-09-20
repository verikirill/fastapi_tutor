from typing import Annotated

from fastapi import Depends

from schemes import STaskAdd, STask, STaskId

from fastapi import APIRouter
from repository import TaskRepository

router = APIRouter(
    prefix="/tasks",
    tags=["Таски"]
)


@router.post("")
async def add_tasks(
        task: Annotated[STaskAdd, Depends()]
) -> STaskId:
    task_id = await TaskRepository.add_one(task)
    return {"ok": True, "task_id": task_id}


@router.get("")
async def get_tasks() -> STask:
    tasks = await TaskRepository.find_all()
    return tasks
