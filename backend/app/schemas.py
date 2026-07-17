from pydantic import BaseModel

class SecurityEvent(BaseModel):
    service: str
    severity: str
    message: str

    class Config:
        from_attributes = True
