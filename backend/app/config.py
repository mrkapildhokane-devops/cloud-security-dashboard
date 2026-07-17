import os
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "postgresql://admin:admin123@postgres:5432/securitydb"
)

AWS_REGION = os.getenv("AWS_REGION", "ap-south-1")
