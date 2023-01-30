
from sqlalchemy.orm import Session
from sqlalchemy.sql import func
import sys
print(sys.setrecursionlimit(2000))
import models
import schemas

def get_country_code(db: Session, country_code: str):
    return db.query(models.GdpMktp).filter(models.GdpMktp.country_code == country_code).first()


def get_gdp_region(db: Session, region: str):
    return db.query(models.MetadataCountry.table_name, models.MetadataCountry.income_group).filter(models.MetadataCountry.region == region)


def get_gdp_country_name(db: Session, country_name: str):
    return db.query(models.GdpMktp.year, models.GdpMktp.gdp).filter(models.GdpMktp.country_name == country_name)


def get_gdp_init_year_end_year(db: Session, year_init: str, year_end: str):
    sql_1 = db.query(models.GdpMktp.country_name, models.GdpMktp.country_code).filter(models.GdpMktp.year.between(year_init, year_end)).group_by(func.avg(models.GdpMktp.gdp)).order_by(models.GdpMktp.country_name).limit(10)
    return sql_1   