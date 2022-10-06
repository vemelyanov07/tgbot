from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class MediaIds(Base):
    __tablename__ = 'Media ids'
    id = Column(Integer, primary_key=True, autoincrement=True, null=False)
    file_id = Column(String(255))
    file_name = Column(String(255))