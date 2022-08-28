from pydantic import BaseModel
from typing import Optional, List


class User(BaseModel):
    id: Optional[str] = None
    name: str
    phone: str
    my_product: List[Product]
    my_sales: List[Request]
    my_requests: List[Request]

class Product(BaseModel):
    id: Optional[str] = None
    user: User
    detail: str
    price: float
    available: bool = Flase

class Request(BaseModel):
    id:Optional[str] = None
    #relacionamento com a classe User
    user: User
    product: Product
    quantidade:int
    delivery: bool = True
    address: str
    note: Optional[str] = 'Sem observacoes'

    
