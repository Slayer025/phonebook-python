from fastapi import APIRouter, Depends, HTTPException, Request
from sqlalchemy.orm import Session
from ..database import SessionLocal
from .. import crud, schemas

# ✅ Import limiter from separate file (NO circular import)
from ..limiter import limiter

router = APIRouter(prefix="/contacts", tags=["Contacts"])

# Dependency (DB session)
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# CREATE
@router.post("/", response_model=schemas.ContactResponse)
@limiter.limit("5/minute")
def create(request: Request, contact: schemas.ContactCreate, db: Session = Depends(get_db)):
    try:
        return crud.create_contact(db, contact)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


# GET ALL
@router.get("/", response_model=list[schemas.ContactResponse])
@limiter.limit("10/minute")
def get_all(request: Request, db: Session = Depends(get_db)):
    return crud.get_contacts(db)


# GET BY ID
@router.get("/{id}", response_model=schemas.ContactResponse)
@limiter.limit("10/minute")
def get_one(request: Request, id: int, db: Session = Depends(get_db)):
    contact = crud.get_contact(db, id)
    if not contact:
        raise HTTPException(status_code=404, detail="Contact not found")
    return contact


# UPDATE
@router.put("/{id}", response_model=schemas.ContactResponse)
@limiter.limit("5/minute")
def update(request: Request, id: int, data: schemas.ContactCreate, db: Session = Depends(get_db)):
    updated = crud.update_contact(db, id, data)
    if not updated:
        raise HTTPException(status_code=404, detail="Contact not found")
    return updated


# DELETE
@router.delete("/{id}")
@limiter.limit("5/minute")
def delete(request: Request, id: int, db: Session = Depends(get_db)):
    deleted = crud.delete_contact(db, id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Contact not found")
    return {"message": "Deleted successfully"}