#Eric Malmström IA-Labb 3

#Products are kept in inventory
class Product:
    def __init__(self, productNumber:int, productName:str, price:int)-> None:
        '''
        constructor for Product class
        '''
        self.productNumber = productNumber
        self.productName = productName
        self.price = price

    def __str__(self) -> str:
        return f"Product number: {self.productNumber} - Product name: {self.productName} - Product price: {self.price} "