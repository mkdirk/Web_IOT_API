from dotenv import load_dotenv
load_dotenv()

from fastapi import FastAPI, Depends, Response, APIRouter
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session

# Import models
from database import SessionLocal, engine
import models
from sqlalchemy import delete, update

models.Base.metadata.create_all(bind=engine)

app = FastAPI()
router_v1 = APIRouter(prefix='/api/v1')

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# https://fastapi.tiangolo.com/tutorial/sql-databases/#crud-utils

@router_v1.get('/books')
async def get_books(db: Session = Depends(get_db)):
    return db.query(models.Book).all()

@router_v1.get('/menu')
async def get_menues(db: Session = Depends(get_db)):
    return db.query(models.Menu).all()

@router_v1.get('/books/{book_id}')
async def get_book(book_id: int, db: Session = Depends(get_db)):
    return db.query(models.Book).filter(models.Book.id == book_id).first()

@router_v1.get('/menu/{menu_id}')
async def get_menu(menu_id: int, db: Session = Depends(get_db)):
    return db.query(models.Menu).filter(models.Menu.id == menu_id).first()

@router_v1.post('/books')
async def create_book(book: dict, response: Response, db: Session = Depends(get_db)):
    # TODO: Add validation
    newbook = models.Book(title=book['title'], author=book['author'], year=book['year'], detail=book['detail'], short=book['short'], category=book['category'],is_published=book['is_published'])
    db.add(newbook)
    db.commit()
    db.refresh(newbook)
    response.status_code = 201
    return newbook

@router_v1.post('/menu')
async def create_menu(menu: dict, response: Response, db: Session = Depends(get_db)):
    # TODO: Add validation
    newmenu = models.Menu(name=menu['name'], price=menu['price'])
    db.add(newmenu)
    db.commit()
    db.refresh(newmenu)
    response.status_code = 201
    return newmenu

# @router_v1.post('/order')
# async def confirm_order(order: dict, response: Response, db: Session = Depends(get_db)):
#     # TODO: Add validation
#     price = db.query(models.Menu).filter(models.Menu.id == order['menuId']).first()
#     all_price = (price*order['quantity'])
#     neworder = models.Order(order_id=order['menuId'], quantity=order['quantity'], note=order['note'], total_price=all_price)
#     db.add(neworder)
#     db.commit()
#     db.refresh(neworder)
#     response.status_code = 201
#     return neworder

@router_v1.patch('/books/{book_id}') #update
async def update_book(book_id: str, book: dict, response: Response, db: Session = Depends(get_db)):
    result = db.execute(update(models.Book).where(models.Book.id == book_id).values(book))
    db.commit()
    response.status_code = 201
    return result.all

@router_v1.patch('/menu/{menu_id}') #update
async def update_menu(menu_id: str, menu: dict, response: Response, db: Session = Depends(get_db)):
    result = db.execute(update(models.Menu).where(models.Menu.id == menu_id).values(menu))
    db.commit()
    response.status_code = 201
    return result.all

@router_v1.delete('/books/{book_id}')
async def delete_student(book_id: str, response: Response, db: Session = Depends(get_db)):
    result = db.execute(delete(models.Book).where(models.Book.id == str(book_id)))
    db.commit()
    response.status_code = 200
    return db.query(models.Book).all()

# @router_v1.patch('/books/{book_id}')
# async def update_book(book_id: int, book: dict, db: Session = Depends(get_db)):
#     pass

# @router_v1.delete('/books/{book_id}')
# async def delete_book(book_id: int, db: Session = Depends(get_db)):
#     pass

app.include_router(router_v1)

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app)
