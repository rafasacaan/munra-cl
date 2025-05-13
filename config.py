import os
from dotenv import load_dotenv

load_dotenv()

# API Keys and Model settings
ANTHROPIC_API_KEY = os.getenv("ANTHROPIC_API_KEY")
DEFAULT_MODEL = os.getenv("DEFAULT_MODEL", "claude-3-haiku-20240307") # claude-3-7-sonnet@20250219

# Application settings
DEBUG = os.getenv("DEBUG", "True").lower() == "true"
APP_NAME = "munra.cl"

# Database settings
DB_PATH = os.getenv("DB_PATH", "recs.db")
DATABASE_URL = os.getenv("DATABASE_URL", f"sqlite:///./{DB_PATH}")