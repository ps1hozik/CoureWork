from dotenv import load_dotenv
import os


load_dotenv()

SECRET_KEY = os.environ["SECRET_KEY"]
REFRESH_SECRET_KEY = os.environ["REFRESH_SECRET_KEY"]
FASTAPI_DB_URL = os.environ["FASTAPI_DB_URL"]
