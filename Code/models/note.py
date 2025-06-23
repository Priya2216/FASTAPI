from pydantic import BaseModel
from typing import Optional  # ✅ required for optional fields

class Note(BaseModel):
    title: str
    desc: str
    important: Optional[bool] = None  # ✅ allows True, False, or None
