import os
from fastapi import FastAPI
from dotenv import load_dotenv
from sqlalchemy import create_engine, text
from sqlalchemy.pool import NullPool



load_dotenv()
database_url = os.getenv("DATABASE_URL")

engine = create_engine(
		database_url,
		poolclass=NullPool
		)


try:
	with engine.begin() as connection:
		result = connection.execute(text("SELECT version();"))
		version = result.fetchone()
		print("Succesfully connected to Neon")
		print(f"Postgresql version : {version[0]}")
except Exception as e:
	print(f"Connection failed : {e}")




app = FastAPI()

@app.get('/')
def home():
	return {"message": "FastAPI is running"}

