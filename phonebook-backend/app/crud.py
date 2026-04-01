from sqlalchemy.orm import Session
from fastapi import HTTPException
from . import models, schemas

def sanitize_email(email_str: str):
    if email_str and email_str.strip():
        return email_str.strip()
    return None

# CREATE
def create_contact(db: Session, contact: schemas.ContactCreate):
    email_val = sanitize_email(contact.email)

    existing_phone = db.query(models.Contact).filter(
        models.Contact.phone_number == contact.phone_number
    ).first()
    if existing_phone:
        raise HTTPException(status_code=400, detail="Phone already exists")

    if email_val:
        existing_email = db.query(models.Contact).filter(
            models.Contact.email == email_val
        ).first()
        if existing_email:
            raise HTTPException(status_code=400, detail="Email already exists")

    db_contact = models.Contact(
        name=contact.name,
        phone_number=contact.phone_number,
        email=email_val,
        address=contact.address if contact.address else None
    )

    db.add(db_contact)
    db.commit()
    db.refresh(db_contact)
    return db_contact

# GET ALL
def get_contacts(db: Session):
    return db.query(models.Contact).all()

# GET ONE
def get_contact(db: Session, contact_id: int):
    return db.query(models.Contact).filter(models.Contact.id == contact_id).first()

# UPDATE
def update_contact(db: Session, contact_id: int, data: schemas.ContactCreate):
    contact = get_contact(db, contact_id)
    if not contact:
        raise HTTPException(status_code=404, detail="Contact not found")

    email_val = sanitize_email(data.email)

    existing_phone = db.query(models.Contact).filter(
        models.Contact.phone_number == data.phone_number,
        models.Contact.id != contact_id
    ).first()
    if existing_phone:
        raise HTTPException(status_code=400, detail="Phone already exists")

    if email_val:
        existing_email = db.query(models.Contact).filter(
            models.Contact.email == email_val,
            models.Contact.id != contact_id
        ).first()
        if existing_email:
            raise HTTPException(status_code=400, detail="Email already exists")

    contact.name = data.name
    contact.phone_number = data.phone_number
    contact.email = email_val
    contact.address = data.address if data.address else None

    db.commit()
    db.refresh(contact)
    return contact

# DELETE
def delete_contact(db: Session, contact_id: int):
    contact = get_contact(db, contact_id)
    if not contact:
        raise HTTPException(status_code=404, detail="Contact not found")

    db.delete(contact)
    db.commit()
    return {"message": "Contact deleted successfully"}