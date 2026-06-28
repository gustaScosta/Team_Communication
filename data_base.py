from sqlalquemy import creat_engine
from sqlalquemy import declarative_base

engine = creat_engine('postgresql://neondb_owner:npg_lXwgumYP71KN@ep-polished-sound-ack27btm-pooler.sa-east-1.aws.neon.tech/neondb?sslmode=require&channel_binding=require')

base = declarative_base()

class Usuario(base):
    __tablename__ = "usuarios"

    id: mapped[int] = mapped_column(primary_key=True)
    