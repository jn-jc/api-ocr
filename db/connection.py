from sqlalchemy import create_engine, MetaData

engine = create_engine("mysql+pymysql://root:root123@192.168.0.4:3306/ocr-app")

meta = MetaData()

conn = engine.connect()