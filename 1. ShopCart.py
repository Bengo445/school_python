
class ShopCart:

    def __init__(self):
        self.items = []

    def addItem(self, name, price):
        self.items.append((name, price))

    def removeItem(self, name):
        for i in range(len(self.items)):
            if self.items[i][0] == name:
                self.items.pop(i)
                break
    
    def printContent(self):
        for i in range(len(self.items)):
            print(f"{self.items[i][0]}: {str(self.items[i][1])}")


# cart = ShopCart()

# cart.addItem("lol", 50)
# cart.addItem("lol2", 43)
# cart.printContent()
# cart.removeItem("lol")
# cart.printContent()
