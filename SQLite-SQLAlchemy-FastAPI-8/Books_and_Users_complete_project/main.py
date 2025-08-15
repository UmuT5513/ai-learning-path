from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

# diğer dosyalardan
import models
import schemas
from database import engine, engine_users, SessionLocal, SessionLocal_users

app = FastAPI(title="Books and Users API", version="1.0.0")

# veri tabanı oluştur
models.Base.metadata.create_all(bind=engine)

# veri tabanı oluştur - users için
models.Base.metadata.create_all(bind=engine_users)


# DB oturumu alma
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# users için DB oturumu alma
def get_db_user():
    db_user = SessionLocal_users()
    try:
        yield db_user
    finally:
        db_user.close()


@app.get("/")
def root():
    return {"message": "Books and Users API"}


# kitap ekleme - post method
@app.post("/books", response_model=schemas.BookOut)
def create_book(book: schemas.BookCreate, db: Session = Depends(get_db)):
    try:
        db_book = models.Book(**book.model_dump())
        db.add(db_book)
        db.commit()
        db.refresh(db_book)
        return db_book
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=400, detail=f"Kitap eklenirken hata oluştu: {str(e)}")


@app.post("/users", response_model=schemas.UserOut)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db_user)):
    try:
        # Email benzersizlik kontrolü
        existing_user = db.query(models.User).filter(models.User.email == user.email).first()
        if existing_user:
            raise HTTPException(status_code=400, detail="Bu email adresi zaten kullanılıyor")

        db_user = models.User(**user.model_dump())
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
        return db_user
    except HTTPException:
        db.rollback()
        raise
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=400, detail=f"Kullanıcı eklenirken hata oluştu: {str(e)}")


# kitap listeleme - get method
@app.get("/books", response_model=list[schemas.BookOut])
def list_books(db: Session = Depends(get_db)):
    try:
        return db.query(models.Book).all()
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Kitaplar listelenirken hata oluştu: {str(e)}")


# user listeleme - DÜZELTİLDİ: get_db_user kullanılıyor
@app.get("/users", response_model=list[schemas.UserOut])
def list_users(db: Session = Depends(get_db_user)):  # get_db_user kullanılıyor
    try:
        return db.query(models.User).all()
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Kullanıcılar listelenirken hata oluştu: {str(e)}")


# Tek kitap getirme
@app.get("/books/{book_id}", response_model=schemas.BookOut)
def get_book(book_id: int, db: Session = Depends(get_db)):
    book = db.query(models.Book).filter(models.Book.id == book_id).first()
    if book is None:
        raise HTTPException(status_code=404, detail="Kitap bulunamadı")
    return book


# Tek kullanıcı getirme
@app.get("/users/{user_id}", response_model=schemas.UserOut)
def get_user(user_id: int, db: Session = Depends(get_db_user)):
    user = db.query(models.User).filter(models.User.id == user_id).first()
    if user is None:
        raise HTTPException(status_code=404, detail="Kullanıcı bulunamadı")
    return user


@app.patch("/books/{book_id}", response_model=schemas.BookOut)
def update_book(book_id:int, updated_book: schemas.BookUpdate, db: Session = Depends(get_db)):
    book = db.query(models.Book).filter(models.Book.id == book_id).first()

    if book is None:
        raise HTTPException(status_code=404, detail="Kitap bulunamadı")

    updated_book_dict = updated_book.model_dump(exclude_unset=True)
    if not updated_book_dict:
        raise ValueError("Güncellenecek veri bulunamadı!") # to do: logger.error

    # Alanları tek tek güncelle (daha güvenli)
    for key, value in updated_book_dict.items():
        if hasattr(book, key): # book nesnesinde field adında bir özellik var mı diye kntrol eder.
            current_value = getattr(book, key) # zaten var olanın value si.
            if current_value != value:
                setattr(book, key, value) #örn: book.title = "muhtelif 2"
            else:
                print("eklenen değer ile önceki değer aynı") # to do: buraya logger.info ekle

    db.commit()
    db.refresh(book)
    return book
