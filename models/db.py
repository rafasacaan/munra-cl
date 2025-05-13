from sqlmodel import SQLModel, Session, create_engine
import config
import os
from sqlalchemy.exc import OperationalError
import sqlite3

# Create engine for database
engine = create_engine(config.DATABASE_URL, echo=config.DEBUG)

def database_exists():
    """
    Check if the database exists.
    """
    if config.DATABASE_URL.startswith('sqlite'):
        # Extract the database path from the URL
        # The format is typically 'sqlite:///path/to/database.db'
        db_path = config.DATABASE_URL.replace('sqlite:///', '')
        return os.path.exists(db_path)
    else:
        # For other database types, try to connect
        try:
            # Use a simple query to check if we can connect
            with engine.connect() as conn:
                conn.execute("SELECT 1")
            return True
        except OperationalError:
            return False


def create_db_and_tables():
    """
    Create database tables if they don't exist.
    """
    if database_exists():
        print(f"Database found at {config.DATABASE_URL}")
        # Check if tables exist by inspecting the schema
        try:
            # For SQLite specifically
            if config.DATABASE_URL.startswith('sqlite'):
                db_path = config.DATABASE_URL.replace('sqlite:///', '')
                conn = sqlite3.connect(db_path)
                cursor = conn.cursor()
                # Check if our tables exist
                cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='rec_generation_history'")
                if cursor.fetchone():
                    print("Database tables already exist")
                    conn.close()
                    return
                conn.close()
        except Exception as e:
            print(f"Error checking tables: {e}")
            
    # Create tables regardless
    print("Creating database tables...")
    SQLModel.metadata.create_all(engine)
    print("Database tables created successfully")


def get_session():
    """
    Get a database session.
    """
    return Session(engine)