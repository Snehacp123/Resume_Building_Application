from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# define engine for database
engine = create_engine(
    "postgresql://postgres:postgres@127.0.0.1:5432/resume_builder_db"
)
# Creating session object to interact with DB or manage transaction
Session = sessionmaker(bind=engine)
# Creating session instance
session = Session()
