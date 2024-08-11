from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column
from orm.settiing import db
class Product(db.Model):
    id = mapped_column(Integer,autoincrement=True,primary_key=True)
    title = mapped_column(String,nullable=False)
    desc = mapped_column(String)
    price = mapped_column(Integer)