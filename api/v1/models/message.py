from typing import Optional

from pydantic import BaseModel

class Message(BaseModel):
    id: str
    user: str
    message: str
    created_at: str