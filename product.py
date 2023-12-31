from enum import Enum

class Produto:
    def __init__(self, name, barcode, preco, marca, categoria):
        self.name = name
        self.barcode = barcode
        self.preco = preco
        self.marca = marca
        self.categoria = categoria

class Marcas(Enum):
    Amazon = 1
    Renner = 2
    Avon = 3

class ProductError(ValueError):

    def __init__(self, message = "Produto não disponível"):
        self.message = message
        super().__init__(self.message)