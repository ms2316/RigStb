import datetime
import sqlalchemy
from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Stb(Base):
    __tablename__ = 'boxes'

    id = Column(Integer, primary_key = True)
    rig_no = Column(Integer)
    stb_no = Column(Integer)
    version = Column(String)
    ip = Column(String)
    mac = Column(String)
    model = Column(String)
    oem = Column(String)
    ruid = Column(String)
    variant = Column(String)
    timestamp = Column(DateTime, default=datetime.datetime.now )

    def __repr__(self):
        return "<Stb(id = '%i', mac = '%s', date = '%s')>" % (self.id, self.mac, self.timestamp)

#TO create new table create engine and call create_all on Base
'''
engine = create_engine('postgresql://stb-tester:testaut@localhost:57998/testaut', echo = True)
Base.metadata.create_all(engine)
Empty table created
'''

#Creating session
'''
from sqlalchemy.orm import sessionmaker
Session = sessionmaker(bind = engine) #Session is associate with Engine, but hasnt opened any connections yet
session = Session() #establish a connection
session.close()
'''

#postgresql
#DROP TABLE table_name;
