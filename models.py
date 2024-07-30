from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, column
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

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String, index=True)
    price = Column(Integer, index=True)

class Order(Base):
    __tablename__ = 'Order'

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    order_id = Column(Integer, index=True)
    quantity = Column(Integer, index=True)
    note = Column(String, index=True)
    total_price = Column(Integer, index=True)
