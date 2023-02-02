from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

import crud, models, schemas
from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/countries/{country_code}")
def read_country_code(country_code: str, db: Session = Depends(get_db)):
    db_gdp = crud.get_country_code(db, country_code=country_code)
    if db_gdp is None:
        raise HTTPException(status_code=404, detail="Country code not found")
    return db_gdp


@app.get("/region/{region}")
def gdp_region(region: str, db: Session = Depends(get_db)):
    db_gdp = crud.get_gdp_region(db, region=region)
    if db_gdp is None:
        raise HTTPException(status_code=404, detail="Country code not found")
    return db_gdp

@app.get("/pib_year/{country_name}")
def gdp_year(country_name: str, db: Session = Depends(get_db)):
    db_gdp = crud.get_gdp_country_name(db, country_name=country_name)
    if db_gdp is None:
        raise HTTPException(status_code=404, detail="pib year not found")
    return db_gdp

@app.get("/rank_pib/")
def get_gdp_year(year_ini: str, year_end: str, db: Session = Depends(get_db)):
    db_gdp = crud.get_gdp_init_year_end_year(db, year_init=year_ini, year_end=year_end)
    if db_gdp is None:
        raise HTTPException(status_code=404, detail="Not found year")
    return db_gdp