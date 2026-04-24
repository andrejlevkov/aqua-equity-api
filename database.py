from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase

# Point this at your existing database
DATABASE_URL = "mysql://aqua_equity_greaterlow:586798d703e7f33f1bd4aa0d0d2222cb4c13926f@qe71st.h.filess.io:3307/aqua_equity_greaterlow"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

class Base(DeclarativeBase):
    pass

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()