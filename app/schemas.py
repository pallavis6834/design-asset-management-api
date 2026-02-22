from pydantic import BaseModel
from datetime import datetime

class AssetResponse(BaseModel):
    id: int
    filename: str
    content_type: str
    tags: str
    uploaded_at: datetime

    class Config:
        orm_mode = True
