import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class Config:
    DATABASE_URL = os.getenv("DATABASE_URL")

# Test if the environment variables are loaded
if __name__ == "__main__":
    print("DATABASE_URL:", Config.DATABASE_URL)
