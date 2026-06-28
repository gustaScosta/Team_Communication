from sqlalchemy import create_engine, String
from sqlalchemy.orm import declarative_base, Mapped, mapped_column

engine = create_engine(
    "postgresql+psycopg://neondb_owner:npg_lXwgumYP71KN@ep-polished-sound-ack27btm-pooler.sa-east-1.aws.neon.tech/neondb?sslmode=require&channel_binding=require")
class Base(declarative_base):
    pass

class chamado(Base):
    __tablename__ = "chamados"

    id: Mapped[int] = mapped_column(primary_key=True, unique=True)
    titulo: Mapped[str] = mapped_column(String(50), nullable=False)
    descrição: Mapped[str] = mapped_column(String(200), nullable=False)
    setor: Mapped[str] = mapped_column(nullable=False)
    