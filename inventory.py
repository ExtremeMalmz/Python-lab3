#Eric Malmström IA-Labb 3
from product import Product

class Inventory():
    def __init__(self)-> None:
        '''
        constructor for Inventory class
        '''
        self.listOfProducts = []

    def addItemToInventory(self, productNumber:int, productName:str, price:int)-> None:
        '''
        adds item to listOfProducts
        '''
        
        storeProduct = Product(productNumber, productName, price)
        self.listOfProducts.append(storeProduct)

        '''
        product1 = Product(123,'Ericstation',100)
        self.listOfProducts.append(product1)

        product2 = Product(123,'asda',100)
        self.listOfProducts.append(product2)
        '''
        
    def __str__(self):
        return  '\n'.join(str(storeProduct) for storeProduct in self.listOfProducts)