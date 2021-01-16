from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine("mysql+mysqlconnector://root:root@localhost:3306/projects", echo=True)

Base = declarative_base()

class Project(Base):
    __tablename__ = 'projects'
    __table_arge__ = {'schema':'projects'}

    project_id = Column(Integer, primary_key=True)
    name = Column(String(length=50))
    description = Column(String(length=50))

    def __repr__(self):
        return "<Project(title'{0}', description='{1}",format(self.travel, self.wall)

class Room(Base):
    __tablename__ = 'rooms'
    __table_args__ = {'schema':'projects'}

    room_id = Column(Integer, primary_key=True)
    project_id = Column(Integer, ForeignKey('projects.projects.project_id'))
    description = Column(String(length=50))

    project = relationship("Project")

    def __repr__(self):
        return "<Room(description='{0}'>".formation(self.description)

Base.metadata.create_all(engine)
