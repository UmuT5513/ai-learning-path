from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

# diğer dosyalardan
import models
import schemas
from database import engine, SessionLocal

app = FastAPI(title="Books and Users API", version="1.0.0")

# veri tabanı oluştur
models.Base.metadata.create_all(bind=engine)


# DB oturumu alma
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()



@app.get("/")
def root():
    return {"message": "Books and Users API"}


# kitap ekleme - post method
@app.post("/books", response_model=schemas.BookOut)
def create_book(book: schemas.BookCreate, session: Session = Depends(get_db)):
    try:
        db_book = models.Book(**book.model_dump())
        session.add(db_book)
        session.commit()
        session.refresh(db_book)
        return db_book
    except Exception as e:
        session.rollback()
        raise HTTPException(status_code=400, detail=f"Kitap eklenirken hata oluştu: {str(e)}")


@app.post("/users", response_model=schemas.UserOut)
def create_user(user: schemas.UserCreate, session: Session = Depends(get_db)):
    try:
        # Email benzersizlik kontrolü
        existing_user = session.query(models.User).filter(models.User.email == user.email).first()
        if existing_user:
            raise HTTPException(status_code=400, detail="Bu email adresi zaten kullanılıyor")

        db_user = models.User(**user.model_dump())
        session.add(db_user)
        session.commit()
        session.refresh(db_user)
        return db_user
    except HTTPException:
        session.rollback()
        raise
    except Exception as e:
        session.rollback()
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
def list_users(session: Session = Depends(get_db)):
    try:
        return session.query(models.User).all()
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Kullanıcılar listelenirken hata oluştu: {str(e)}")


# Tek kitap getirme
@app.get("/books/{book_id}", response_model=schemas.BookOut)
def get_book(book_id: int, session: Session = Depends(get_db)):
    book = session.query(models.Book).filter(models.Book.id == book_id).first()
    if book is None:
        raise HTTPException(status_code=404, detail="Kitap bulunamadı")
    return book


# Tek kullanıcı getirme
@app.get("/users/{user_id}", response_model=schemas.UserOut)
def get_user(user_id: int, session: Session = Depends(get_db)):
    user = session.query(models.User).filter(models.User.id == user_id).first()
    if user is None:
        raise HTTPException(status_code=404, detail="Kullanıcı bulunamadı")
    return user


@app.patch("/books/{book_id}", response_model=schemas.BookOut)
def update_book(book_id:int, updated_book: schemas.BookUpdate, session: Session = Depends(get_db)):
    book = session.query(models.Book).filter(models.Book.id == book_id).first()

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

    session.commit()
    session.refresh(book)
    return book

@app.get("/users/{user_id}/books", response_model=list[schemas.BookOut])
def get_user_books(user_id: int, session: Session = Depends(get_db)):
    user = session.query(models.User).filter(models.User.id == user_id).first()

    if not user:
        raise HTTPException(status_code=404, detail="user bulunamadı!")

    return user.books



@app.post("/users/{user_id}/books/{book_id}")
def assign_book_to_user(user_id:int, book_id:int, session: Session = Depends(get_db)):
    user = session.query(models.User).filter(models.User.id == user_id).first()
    book = session.query(models.Book).filter(models.Book.id == book_id).first()

    if not user or not book:
        raise HTTPException(status_code=404, detail="user or book not found!")


    book.user_id = user_id

    session.commit()
    session.refresh(book)

    return {"message": f"Book '{book.title}' assigned to user '{user.name}'"}
