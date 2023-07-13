import sqlalchemy as _sql
import sqlalchemy.ext.declarative as _declarative
import sqlalchemy.orm as _orm
from dotenv import load_dotenv
import os
#fetch test
load_dotenv()

DATABASE_URL = os.getenv("db_url")
#create db engine
engine = _sql.create_engine(DATABASE_URL,pool_size=10,
                                      max_overflow=2,
                                      pool_recycle=300,
                                      pool_pre_ping=True,
                                      pool_use_lifo=True)
#create orm session
SessionLocal = _orm.sessionmaker(bind=engine,query_cls=_orm.RetryingQuery)

Base = _declarative.declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    except:
        db.close()