from sqlalchemy import create_engine, MetaData

ip_adress = ''

engine = create_engine("mysql+pymysql://root:root123@127.0.0.1:3309/ocr_db")

meta = MetaData()

conn = engine.connect()