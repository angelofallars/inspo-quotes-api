from typing import Optional
from pydantic import BaseModel


class Quote(BaseModel):
    id: Optional[int]
    text: Optional[str]
