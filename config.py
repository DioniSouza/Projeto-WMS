import os

class Config:
#String de  conexão com banco de dados PostGreSQL
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL','postgresql://dionis:44718640@localhost:54322/wms_db')
    SQLALCHEMY_TRACK_MMODIFICATIONS = False
    