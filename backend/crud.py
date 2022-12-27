from sqlalchemy.orm import Session
import passlib.hash as _hash
import model
import schemas




def create_user(db: Session, user: schemas.UserCreate):
    fake_hashed_password = _hash.bcrypt.hash(user.hashed_password)
    db_user = model.User(email=user.email, hashed_password=fake_hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
