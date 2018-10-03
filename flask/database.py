import os
import sys
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.engine.url import make_url
from sqlalchemy import create_engine


# Connect to MySQL database
engine_url = make_url('mysql+pymysql://wyadmin:EOGWY_2017@10.5.24.72/wyoming')
mysql_engine = create_engine(engine_url, convert_unicode=True, echo=False, pool_recycle=3600)
MysqlSession = scoped_session(sessionmaker(autocommit=False,
                                            autoflush=False,
                                            bind=mysql_engine))
Base = declarative_base()
Base.query = MysqlSession.query_property()

def init_db():
    '''
    import all modules here that might define models so that they will be registered properly
    on the metadata.  Otherwise you will have to import them first before calling init_db()
    :return:
    '''
    import uploads.models
    Base.metadata.create_all(bind=mysql_engine)
