import datetime as dt
import sqlalchemy as sql
 
import database as db


class Url(db.Base):
    __tablename__ = "urls"
    
    id = sql.Column(sql.Integer, primary_key=True,index=True)
    inputUrl = sql.Column(sql.String, index=True)
    outputUrl = sql.Column(sql.String, index=True,unique=True)
    date_created = sql.Column(sql.DateTime,default=dt.datetime.utcnow)
