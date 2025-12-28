from dataclasses import dataclass
from datetime import datetime
from typing import Optional


@dataclass # this is a decorator  used to modify the behavious of a class or a function 
class Task:
    id: int
    title: str
    status: str = "pending"
    due: Optional[str] = None
    created_at: str = datetime.utcnow().isoformat()