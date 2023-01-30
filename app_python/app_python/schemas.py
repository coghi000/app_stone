
from typing import List, Union
from pydantic import BaseModel


class GdpMktp(BaseModel):
    country_code: str
    country_name: str
    indicator_name: str
    indicator_code: str
    year: int
    gdp: float
    
    metadata_country_code: str    
    # metadata_country: MetadataCountry
    
    class Config:
        orm_mode = True

class MetadataCountry(BaseModel):
    country_code: str
    region: str
    income_group: str
    table_name: str
    
    gdp_country_code: str
    gdp: GdpMktp
    
    class Config:
        orm_mode = True
    
