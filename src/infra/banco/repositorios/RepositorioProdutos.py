from sqlalchemy import Session
from src.schemas import schemas 
from src.infra.banco.models import models

class RepositorioProdutos():
    def __init__(self, db: Session):
        self.db = db
    
    def criar(self, produtc: schemas.Product):
        db_produtos = models.Product(
            name = product.name
            detail = product.deatil
            price = product.price
            avaliabel = porduct.availabel
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