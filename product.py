class Product:
    DELIVERY = 1.2
    KURS = 9

    def __init__(self, name='', price=0, price_with_delivery=0) -> None:
        self.name = name
        value_price = price.replace(',', '.')
        self.price  = round(int(float(value_price)), 2)
        self.price_with_delivery = round(((self.price/1.23*self.DELIVERY*self.KURS)/100)) * 100

    def __repr__(self) -> str:
        return(f'NAME= {self.name}******* PRICE= {self.price} ******={self.price_with_delivery}\n')

    def getName(self) -> str:
        return self.name
    def getPrice(self) -> int:
        return self.price
    def getPriceWithDelivery(self) -> int:
        return self.price_with_delivery
    
    def setName(self, name):
        self.name = str(name)
    def setPrice(self, price):
        self.price = round(int(price), 2)

