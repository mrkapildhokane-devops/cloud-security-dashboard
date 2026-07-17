from sqlalchemy import Column, Integer, String
from app.database import Base

class SecurityEvent(Base):
    __tablename__ = "security_events"

    id = Column(Integer, primary_key=True, index=True)
    service = Column(String)
    severity = Column(String)
    message = Column(String)
