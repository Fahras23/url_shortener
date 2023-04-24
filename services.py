import database as db
import models as _models

def __add_tables():
    return db.Base.metadata.create_all(bind=db.engine)