from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class NodeModel(Base):
    __tablename__ = "nodes"

    id = Column(String, primary_key=True)
    type = Column(String)
    message_text = Column(String)
    status = Column(String)
    outgoing_edge = Column(String)
    condition = Column(String)
    yes_edge = Column(String)
    no_edge = Column(String)

engine = create_engine('sqlite:///nodes.db')
Session = sessionmaker(bind=engine)
