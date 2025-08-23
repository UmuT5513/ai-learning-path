from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "sqlite:///./test.db" 
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()


# engine ve SessionLocal main.py dosyasına import edilecek. 
# engine --> ile veri tabanı oluşturulacak ve SessionLocal ile veri tabanına erişilecek(oturum alınacak/get_db()).

# Base ise models.py dosyasında class oluşturmak için kullanılacak. Oluşturulan class Base i miras alacak. 
# bu sayede table oluşturulacak.

# DATABASE_URL --> create_engine --> engine --> (1) models.Base.metadata.create_all(bind=engine) (2) SessionLocal --> get_db()