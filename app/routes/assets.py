from fastapi import APIRouter, UploadFile, File, Depends
from sqlalchemy.orm import Session
from app.database import SessionLocal, engine, Base
from app.models import Asset
from app.schemas import AssetResponse
from app.services.storage import save_file

router = APIRouter()

Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=AssetResponse)
def upload_asset(
    file: UploadFile = File(...),
    tags: str = "",
    db: Session = Depends(get_db)
):
    filename = save_file(file)

    asset = Asset(
        filename=filename,
        content_type=file.content_type,
        tags=tags
    )

    db.add(asset)
    db.commit()
    db.refresh(asset)

    return asset

@router.get("/", response_model=list[AssetResponse])
def list_assets(tag: str | None = None, db: Session = Depends(get_db)):
    query = db.query(Asset)
    if tag:
        query = query.filter(Asset.tags.contains(tag))
    return query.all()
