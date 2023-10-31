class Product:
    def __init__(self, name='', price=0) -> None:
        self.name = name
        self.price  = price

    def __repr__(self) -> str:
        return(f'NAME= {self.name}******* PRICE= {self.price}\n')


