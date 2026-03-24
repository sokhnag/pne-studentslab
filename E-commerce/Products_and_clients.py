class Products:
    def __init__(self, name, price):
        self.name = name
        self.price = int(price)

    def get_information(self):
        return f"Product: {self.name} | Price: {self.price}"

class Clients:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.shopping_cart = []
    def add_to_cart(self, product):
        return self.shopping_cart.append(product.price)

    def compute_total(self):
        return sum(self.shopping_cart)



product1 = Products("LECHE", "100")
product2 = Products("AZUCAR", "70")
product3 = Products("PAN", "50")

client1 = Clients("Alba", "alba@gmail.com" )
client2 = Clients("ector", "ector@gmail.com" )

client2.add_to_cart(product1)

print(f"Client: {client2.name}, total:{client2.compute_total()}")
print(f"Client: {client1.name}, total:{client2.compute_total()}")