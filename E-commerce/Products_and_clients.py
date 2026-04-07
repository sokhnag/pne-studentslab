
class Products:
    def __init__(self, name, price):
        self.name = name
        self.price = float(price)

    def get_information(self):
        return f"Product: {self.name} | Price: {self.price}"

class Clients:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.shopping_cart = []
    def add_to_cart(self, product):
        return self.shopping_cart.append([product.price , product.name])

    def compute_total(self):
        total = 0
        for a , b in self.shopping_cart:
            total += a
        return total

class Vipclient(Clients):
    def __init__(self,name, email ):
        super().__init__(name,email)
        self.discount = 20
    def compute_total(self):
        super().compute_total()
        total = 0
        for a, b in self.shopping_cart:
            total += a
        total2 = total - (total * self.discount) / 100
        return total2



product1 = Products("LECHE", "1")
product2 = Products("AZUCAR", "1.5")
product3 = Products("PAN", "0.5")

client1 = Clients("Alba", "alba@gmail.com" )
client2 = Clients("ector", "ector@gmail.com" )
client3 = Vipclient("Sokhna", "sokhna@gmail.com" )

client2.add_to_cart(product1)
client2.add_to_cart(product3)

client1.add_to_cart(product1)
client1.add_to_cart(product2)

client3.add_to_cart(product1)
client3.add_to_cart(product2)

print(f"Client: {client2.name}, total: {client2.compute_total()} €")
print(f"Client: {client1.name}, total: {client1.compute_total()} €")
print(f"Client(VIP): {client3.name}, total: {client3.compute_total()} €")