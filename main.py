from fastapi import FastAPI
from datetime import datetime
from typing import List
from pydantic import BaseModel

app = FastAPI()

# Sample In-Memory Data (To be replaced with DB later)
notifications = []
tasks = []

# Pydantic Models (For Data Validation)
class Notification(BaseModel):
    event_id: str
    event_type: str
    timestamp: str
    message: str

class Task(BaseModel):
    task_id: str
    task_name: str
    assigned_to: str
    due_date: str
    status: str
