from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
# from sqlalchemy.orm import relationship

from database import Base

class Book(Base):
    __tablename__ = 'books'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    author = Column(String, index=True)
    year = Column(Integer, index=True)
    detail = Column(String, index=True)
    short = Column(String, index=True)
    category = Column(String, index=True)
    is_published = Column(Boolean, index=True)

class Menu(Base):
    __tablename__ = 'Menu'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    price = Column(Integer, index=True)
