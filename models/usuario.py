from sqlalchemy import Table, Column
from sqlalchemy.sql.sqltypes import Integer, String
from db.connection import meta

usuario = Table("usuarios", meta, 
                 Column("id_usuario", Integer, primary_key=True),
                 Column("id_tienda", Integer ),
                 Column("nombre_usuario", String(20)),
                 Column("apellido_usuario", String(30)),
                 Column("email_usuario", String(255)),
                 Column("password", String(255)))

