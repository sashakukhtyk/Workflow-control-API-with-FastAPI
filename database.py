from sqlalchemy import create_engine, ForeignKey, Column, String, CHAR, Text, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class NodeDB(Base):
    __tablename__ = "nodes"
    id = Column(String, primary_key=True, index=True)
    type = Column(String, index=True)
    name = Column(String, index=True)
    message_status = Column(String, index=True, nullable=True)
    message_text = Column(Text, nullable=True)
    condition = Column(Boolean, nullable=True)

class EdgeDB(Base):
    __tablename__ = "edges"
    id = Column(String, primary_key=True, index=True)
    source = Column(String, ForeignKey('nodes.id'), index=True)
    target = Column(String, ForeignKey('nodes.id'), index=True)
    condition = Column(String, index=True, nullable=True)

engine = create_engine("sqlite:///database.db")
Base.metadata.create_all(bind=engine)

Session = sessionmaker(bind=engine)
session = Session()