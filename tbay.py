from datetime import datetime

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime, Float, ForeignKey
from sqlalchemy.orm import relationship

engine = create_engine('postgresql://thinkful:thinkful@localhost:5432/tbay')
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base() #beginning of table creation


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    username = Column(String, nullable=False)
    password = Column(String, nullable=False)
    auctioned_items = relationship("Item", backref="auctioned_by")
    bids_placed = relationship("Bid", backref="placed_by")

class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    description = Column(String)
    start_time = Column(DateTime, default=datetime.utcnow)
    auctioner_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    bids_placed = relationship("Bid", backref="placed_on")

class Bid(Base):
    __tablename__ = "bids"

    id = Column(Integer, primary_key=True)
    price = Column(Float, nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    item_id = Column(Integer, ForeignKey('items.id'), nullable=False)

Base.metadata.create_all(engine) #end of table creation


dave = User(username="dgrohl", password="everlong")
alex = User(username="aturner", password="allmyownstunts")
mike = User(username="mlewis", password="moneyball")

guitar = Item(name="guitar - limited edition!",description="limited edition guitar recently found in john lennon's hidden cottage in albania")
pick = Item(name="solid gold guitar pick", description="prototype of a solid gold guitar pick made by up-and-coming music startup muziqcal")
baseball = Item(name="baseball", description="autographed by billy bean")

session.add_all([dave, alex, mike, guitar, pick, baseball])
session.commit()

baseball.auctioned_by = mike
session.add(baseball)
session.commit()
baseball.auctioner_id
mike.id
mike.auctioned_items
mike.auctioned_items[0]
mike.auctioned_items[0].name
bid = Bid(price=123, placed_on=baseball, placed_by=alex)
bid.user_id
session.add(bid)
session.commit()
bid.user_id
bid.item_id
