from typing import Any, Optional
from pydantic import BaseModel


class Response(BaseModel):
    success: bool
    message: str
    body: Optional[Any]
