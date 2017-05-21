from datetime import datetime

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime, Float, ForeignKey
from sqlalchemy.orm import relationship

engine = create_engine('postgresql://thinkful:thinkful@localhost:5432/tbay')
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()

class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    description = Column(String)
    start_time = Column(DateTime, default=datetime.utcnow)
    auctioner_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    bids_placed = relationship("Bid", backref="placed_on")

    # def __init__(self, name, description):
    #     self.name = name
    #     self.description = description

class Bid(Base):
    __tablename__ = "bids"

    id = Column(Integer, primary_key=True)
    price = Column(Float, nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    item_id = Column(Integer, ForeignKey('items.id'), nullable=False)

    # def __init__(self, price):
    #     self.price = price

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    username = Column(String, nullable=False)
    password = Column(String, nullable=False)
    auctioned_items = relationship(Item, backref="auctioned_by")
    bids_placed = relationship(Bid, backref="placed_by")

    # def __init__(self, username, password):
    #     self.username = username
    #     self.password = password



Base.metadata.create_all(engine)
