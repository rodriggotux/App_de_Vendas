from sqlalchemy import Session
from src.schemas import schemas 
from src.infra.banco.models import models

class RepositorioProdutos():
    def __init__(self, db: Session):
        self.db = db
    
    def criar(self, produto: schemas.Product):
        db_produtos = models.Product(
            name = produtos.name
            detail = produtos.deatil
            price = produto.price
            avaliabel = porduto.availabel
        )
        self.db.add(db_produtos)
        self.db.commit()
        self.db.refresh()
        return db_produtos()

    def listar(self):
        produtos = self.db.query(
            models.Product).All()
        return produtos

    def obter(self):
        pass

    def remover(self):
        pass