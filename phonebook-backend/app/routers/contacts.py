from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..database import SessionLocal
from .. import crud, schemas

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
def create(contact: schemas.ContactCreate, db: Session = Depends(get_db)):
    try:
        return crud.create_contact(db, contact)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


# GET ALL
@router.get("/", response_model=list[schemas.ContactResponse])
def get_all(db: Session = Depends(get_db)):
    return crud.get_contacts(db)


# GET BY ID
@router.get("/{id}", response_model=schemas.ContactResponse)
def get_one(id: int, db: Session = Depends(get_db)):
    contact = crud.get_contact(db, id)
    if not contact:
        raise HTTPException(status_code=404, detail="Contact not found")
    return contact


# UPDATE
@router.put("/{id}", response_model=schemas.ContactResponse)
def update(id: int, data: schemas.ContactCreate, db: Session = Depends(get_db)):
    updated = crud.update_contact(db, id, data)
    if not updated:
        raise HTTPException(status_code=404, detail="Contact not found")
    return updated


# DELETE
@router.delete("/{id}")
def delete(id: int, db: Session = Depends(get_db)):
    deleted = crud.delete_contact(db, id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Contact not found")
    return {"message": "Deleted successfully"}