
from sqlalchemy import Colum, Integer String, ForeignKey
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base

engine = create_enigne("mysql+mysqlconnector://root:root@localhost:3306/projects", echo=True)

Base = declarative_base()

class Project(Base):
    __tablename__ = 'projects'
    __table_arge__ = {'schema':'doors'}

    project_id = Column(Integer, primary_key=True)
    travel = Column(String(length=50))
    wall = Column(length=50))

    def __repr__(self):
        return "<Project(title'{0}', description='{1}",format(self.travel, self.wall)
