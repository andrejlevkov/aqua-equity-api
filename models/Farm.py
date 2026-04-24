from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from database import Base

class Farm(Base):
    __tablename__ = "farm"

    farm_id = Column(Integer, primary_key=True, index=True)
    farm_name = Column(String, nullable=False)
    hectares = Column(float, nullable=False)
    quota = Column(float, nullable=False)
    used_today = Column(float, nullable=False)
    user_id = relationship("User", back_populates="farm")
    top_left_x = Column(float, nullable=False)
    top_left_y = Column(float, nullable=False)
    top_right_x = Column(float, nullable=False)
    top_right_y = Column(float, nullable=False)
    bottom_left_x = Column(float, nullable=False)
    bottom_bottom_y = Column(float, nullable=False)
    bottom_right_x = Column(float, nullable=False)
    bottom_right_y = Column(float, nullable=False)
    soil_moisture = Column(float, nullable=False)
    stress_level = Column(float, nullable=False)
    uncertainty_level = Column(float, nullable=False)
    crop_id = relationship("Crop", back_populates="farm")