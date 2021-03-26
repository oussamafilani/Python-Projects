from sqlalchemy import (Column, Integer, Float, String, Boolean, ForeignKey, Date, ForeignKeyConstraint, NVARCHAR,
                        DateTime, UniqueConstraint, Time, VARBINARY, PrimaryKeyConstraint)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import relationship
import sqlalchemy.exc
from setting import get_local_db
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from setting import get_server_db, get_local_db
from hashlib import sha512
from sqlalchemy import desc, asc

Base = declarative_base()


class Test(Base):
    __tablename__ = 'test'
    id = Column(Integer, primary_key=True)
    name = Column(String(250))

    def __repr__(self):
        return self.name


class TestQueries:
    def __init__(self, server=None):
        engine = create_engine(server)
        Session = sessionmaker(bind=engine)
        self.session = Session()

    def insert(self, id=None, name=''):
        if id is None:
            new_test = Test(name=name)
        else:
            new_test = Test(id=id, name=name)
        self.session.add(new_test)
        self.session.commit()


def create():
    engine = create_engine(get_local_db()[0])
    Base.metadata.create_all(engine)


def insert():
    tq = TestQueries(get_local_db()[0])
    # tq.insert(name='one')
    tq.insert(name='two')
    # tq.insert(id=10, name='one')


if __name__ == '__main__':
    # create()
    insert()