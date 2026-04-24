from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from database import Base

class Alert(Base):
    __tablename__ = "alert"

    alert_id = Column("alert_id", Integer, primary_key=True, index=True)
    farm_id = relationship("Farm", back_populates="alert")
    message = Column("message", String, nullable=False)
    severity = Column("severity", String, nullable=False)
    time_stamp = Column("timestamp", DateTime, nullable=False)
    water_amount = Column("warning_amount", Float, nullable=False)