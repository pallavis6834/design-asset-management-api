from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime
from app.database import Base

class Asset(Base):
    __tablename__ = "assets"

    id = Column(Integer, primary_key=True, index=True)
    filename = Column(String, index=True)
    content_type = Column(String)
    tags = Column(String)
    uploaded_at = Column(DateTime, default=datetime.utcnow)
