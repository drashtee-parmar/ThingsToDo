import psycopg2
from config_settings import Config

try:
    conn = psycopg2.connect(Config.DATABASE_URL)
    print("✅ Database connected successfully!")
    conn.close()
except Exception as e:
    print("❌ Database connection failed:", e)
