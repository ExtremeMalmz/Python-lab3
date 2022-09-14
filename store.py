#Eric Malmström IA-Labb 3
from contextlib import nullcontext
from inventory import Inventory

class Store:
    def __init__(self)->None:
        '''
        Store class constructor
        '''
        self.storeName = "Erics Electronics"
        self.inventory = Inventory()

    def welcomeToStore(self)-> None:
        '''
        Skriver ut ett välkomst meddelande och funkar som main för Store där du kan välja att printa ut eller lägga till en produkt
        '''
        print("Välkommen till Erics Elektronik\nPlease wait while we open the store....")

        while True:
            print("\n---Erics Elektronik---\n")
            print("(1) Lägg till en Produkt\n(2) Få en lista på alla produkter")
            val = int(input("Ditt val: "))

            match val:
                case 1:
                    self.addAProduct()
                case 2:
                    self.printOutProducts()
                case _:
                    print("No comprende")
    
    def addAProduct(self)-> None:
        '''
        Frågar vad du vill ha för egenskapar till din produkt o sedan lägger den till i inventory
        '''
        productNumber = input("Vad är produktens nummer (int)")
        productName = input("Vad är produktens namn (str)")
        productPrice = input("Vad är produktens pris (int)")

        self.inventory.addItemToInventory(productNumber, productName, productPrice)

    def printOutProducts(self)-> None: 
        print("\nVåra produkter")
        print(self.inventory)