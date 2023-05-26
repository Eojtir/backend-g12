from db import db
from sqlalchemy import Column,Integer,String,Boolean,DateTime

class ProductsModel(db.Model):
    __tablename__='Products'
    id = Column(Integer,primary_key=True,autoincrement=True)
    name = Column(String(45))
    stock = Column(Integer)
    price = Column(Integer)
    status = Column(Boolean , default=True)
    create_at = Column(DateTime)
    update_at = Column(DateTime)