from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from database import Base

class Farm(Base):
    __tablename__ = "farm"

    farm_id = Column("farm_id", Integer, primary_key=True, index=True)
    farm_name = Column("farm_name", String, nullable=False)
    hectares = Column("hectares", float, nullable=False)
    quota = Column("quota", float, nullable=False)
    used_today = Column("used_today", float, nullable=False)
    user = relationship("User", back_populates="farm")
    top_left_x = Column("top_left_x", float, nullable=False)
    top_left_y = Column("top_left_y", float, nullable=False)
    top_right_x = Column("top_right_x", float, nullable=False)
    top_right_y = Column("top_right_y", float, nullable=False)
    bottom_left_x = Column("bottom_left_x", float, nullable=False)
    bottom_left_y = Column("bottom_left_y", float, nullable=False)
    bottom_right_x = Column("bottom_right_x", float, nullable=False)
    bottom_right_y = Column("bottom_right_y", float, nullable=False)
    soil_moisture = Column("soil_moisture", float, nullable=False)
    stress_level = Column("stress_level", float, nullable=False)
    uncertainty_level = Column("uncertainty_level", float, nullable=False)
    crop = relationship("Crop", back_populates="farm")