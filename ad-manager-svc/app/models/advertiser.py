from sqlalchemy import Column, String, Integer, JSON, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.dialects.postgresql import JSONB


Base = declarative_base()

class Advertiser(Base):
    __tablename__ = 'advertiser'

    advertiserid = Column(String, primary_key=True, nullable=False)
    advertisername = Column(String)
    industry = Column(String)
    brands = Column(JSONB)
    contactinfo = Column(JSONB)
    advertisertype = Column(String)
    createdby = Column(String)
    updatedby = Column(String)
    createdat = Column(DateTime)
    updatedat = Column(DateTime)
    advertiserstate = Column(String)

    def __repr__(self):
        return f"<Advertiser(id={self.advertiserid}, name='{self.advertisername}', state='{self.advertiserstate}')>"



    """
    advertiserId varchar PRIMARY KEY,
  advetiserName varchar,
  industry varchar,
  brands varchar[],
  contactInfo jsonb,
  advertiserType varchar,
  createdAt timestamp,
  updatedAt timestamp,
  createdBy varchar,
  updatedBy varchar,
  advertiser_state varchar
    """

  