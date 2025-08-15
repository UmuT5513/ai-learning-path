import sqlite3
from sqlalchemy import Column, Integer, String, ForeignKey, Table
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import DateTime

Base = declarative_base()


book_authors = Table('book_authors',
                     Base.metadata,
                     Column('author_id', Integer, ForeignKey('authors.author_id')),
                     Column('book_id', Integer, ForeignKey('books.book_id'))
                     )

book_publishers = Table('book_publishers',
                        Base.metadata,
                        Column('publisher_id', Integer, ForeignKey('publishers.publisher_id')),
                        Column('book_id', Integer, ForeignKey('books.book_id'))
                        )

author_publishers = Table('author_publishers',
                          Base.metadata,
                          Column('publisher_id', Integer, ForeignKey('publishers.publisher_id')),
                          Column('author_id', Integer, ForeignKey('authors.author_id'))
                          )


class Author(Base):
    __tablename__ = 'authors'
    author_id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    birth_year = Column(Integer)
    death_year = Column(Integer)
    nationality = Column(String)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)

    books = relationship('Book',
                         secondary=book_authors,
                         back_populates='authors'
                         )

    publishers = relationship('Publisher',
                              secondary=author_publishers,
                              back_populates='authors'
                              )

class Book(Base):
    __tablename__ = 'books'
    book_id = Column(Integer, primary_key=True)
    title = Column(String)
    isbn = Column(String)
    publication_year = Column(String)
    pages = Column(Integer)
    genre = Column(String)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)

    authors = relationship('Author',
                           secondary=book_authors, #many-to-many ilişkilerde aradaki köprü tablosu hangisiyse onu belirtir (bizim book_publisher).
                           back_populates='books' #Karşı tarafta tanımlı ilişkiyle manuel olarak çift yönlü bağlantı kurar. (Backref’e göre daha kontrollüdür.)
                           )

    publishers = relationship('Publisher',
                              secondary=book_publishers,
                              back_populates='books'
                              )



class Publisher(Base):
    __tablename__ = 'publishers'
    publisher_id = Column(Integer, primary_key=True)
    name = Column(String)
    country = Column(String)
    founded_year = Column(Integer)
    website = Column(String)

    created_at = Column(DateTime)
    updated_at = Column(DateTime)


    books = relationship('Book',
                         secondary=book_publishers,
                         back_populates='publishers'
                         )


    authors = relationship('Author',
                           secondary=author_publishers,
                           back_populates='publishers'
                           )






