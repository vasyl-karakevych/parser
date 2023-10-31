class Product:
    def __init__(self, name='', price=0) -> None:
        self.name = name
        self.price  = price

    def __repr__(self) -> str:
        print(self.name)
        print(self.price)

