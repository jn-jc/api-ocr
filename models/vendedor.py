from sqlalchemy import Table, Column
from sqlalchemy.sql.sqltypes import Integer, String
from db.connection import meta

vendedores = Table("vendedor", meta, 
                 Column("id_vendedor", Integer, primary_key=True),
                 Column("id_tienda", Integer ),
                 Column("nombre_vendedor", String(20)),
                 Column("apellido_vendedor", String(30)),
                 Column("email_vendedor", String(255)),
                 Column("password", String(255)))

