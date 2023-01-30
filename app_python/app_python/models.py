
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Float
from sqlalchemy.orm import relationship

from database import Base

class GdpMktp(Base):
    __tablename__ = "GDP_MKTP"
    
    country_code = Column("country_code", String, primary_key=True, index=True)
    country_name = Column("country_name", String)
    indicator_name = Column("indicator_name", String)
    indicator_code = Column("indicator_code", String)
    year = Column("Year", Integer)
    gdp = Column("GDP", Float)

class MetadataCountry(Base):
    __tablename__ = "Metadata_Country"
    
    country_code = Column("country_code",String, primary_key=True, index=True)
    region = Column("region", String)
    income_group = Column("incomegroup", String)
    table_name = Column("table_name", String)
    

