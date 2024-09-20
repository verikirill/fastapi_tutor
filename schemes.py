from fastapi import FastAPI, Depends
from pydantic import BaseModel
from typing import Optional, Annotated
from contextlib import asynccontextmanager

from pydantic.v1 import ConfigDict


class STaskAdd(BaseModel):
    name: str
    description: Optional[str] = None


class STask(STaskAdd):
    id: int
    model_config = ConfigDict(from_attributes=True)


class STaskId(BaseModel):
    ok: bool = True
    task_id: int
