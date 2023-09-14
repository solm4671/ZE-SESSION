import os
from dotenv import load_dotenv

load_dotenv()

API_ID = os.getenv("API_ID", "21627756").strip()
API_HASH = os.getenv("API_HASH", "fe77fbf0cae9f7f5ece37659e2466cf1").strip()
BOT_TOKEN = os.getenv("BOT_TOKEN", "6479433495:AAEf_dT0k678wrlWtJaGFQ6t1jJNL8p4_58").strip()
DATABASE_URL = os.getenv("DATABASE_URL", "").strip()
MUST_JOIN = os.getenv("MUST_JOIN", "https://t.me/Zz_Z_Z2")

if not API_ID:
    print("No API_ID found. Exiting...")
    raise SystemExit
if not API_HASH:
    print("No API_HASH found. Exiting...")
    raise SystemExit
if not BOT_TOKEN:
    print("No BOT_TOKEN found. Exiting...")
    raise SystemExit
if not DATABASE_URL:
    print("No DATABASE_URL found. Exiting...")
    raise SystemExit

try:
    API_ID = int(API_ID)
except ValueError:
    print("API_ID is not a valid integer. Exiting...")
    raise SystemExit

if "postgres" in DATABASE_URL and "postgresql" not in DATABASE_URL:
    DATABASE_URL = DATABASE_URL.replace("postgres", "postgresql")
