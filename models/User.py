from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from database import Base

class Farm(Base):
    __tablename__ = "user"

    user_id = Column("user_id", Integer, primary_key=True, index=True)
    first_name = Column("first_name", String, nullable=False)
    last_name = Column("last_name", String, nullable=False)
    email = Column("email", String, unique=True, index=True, nullable=False)
    phone_number = Column("phone_number", String, nullable=False)
    password = Column("password", String, nullable=False) 
    username = Column("username", String, unique=True, index=True, nullable=False)