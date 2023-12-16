from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import Session


# Configurações iniciais
engine = create_engine("sqlite:///sqlalchemy.db", echo=True)
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()

class Filme(Base):
    __tablename__ = "tb_Filme"

    titulo = Column(String, primary_key=True)
    genero = Column(String, nullable=False)
    ano = Column(Integer, nullable=False)

    def __repr__(self):
        return f"Filme [titulo={self.titulo}, ano={self.ano}]"
    
# Insert
data_insert = Filme(titulo="Batman", genero="Drama", ano=2022)
session.add(data_insert)
session.commit()

# delete
session.query(Filme).filter(Filme.titulo=="alguma coisa").delete()
session.commit()

# update
session.query(Filme).filter(Filme.genero == "Drama").update({ "ano": 2000 })

#Select
data = session.query(Filme).all()
print(data)
print(data[0].titulo)

session.close()