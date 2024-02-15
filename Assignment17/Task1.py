class Person:
    def __init__(self, name, deposit=1000, loan=0):
        self.name = name
        self.deposit = deposit
        self.loan = loan

    def __str__(self):
        return f"Name: {self.name}, Deposit: {self.deposit}, Loan: {self.loan}"

class House:
    def __init__(self, ID, price, owner):
        self.ID = ID
        self.price = price
        self.owner = owner
        self.status = "for sale"

    def sell_house(self, buyer, loan_amount=None):
        if loan_amount is None:
            # Regular sale
            self.owner.deposit += self.price
            self.owner = buyer
            self.status = "sold"
            print(f"Apartment {self.ID} sold to {buyer.name}.")
        else:
            # Sale with loan
            self.owner.deposit += self.price
            buyer.loan += loan_amount
            self.owner = buyer
            self.status = "sold on loan"
            print(f"Apartment {self.ID} sold on loan to {buyer.name} with a loan of {loan_amount}.")

# Creating Person objects
owner = Person("Alice")
buyer = Person("Bob")

# Creating a House object
house = House("1234ABCD", 300000, owner)


# # Selling the house
# house.sell_house(buyer)

# # Demonstrate the updated information
# print(owner)
# print(buyer)
# print(f"House ID: {house.ID}, Status: {house.status}, Owner: {house.owner.name}")


# Selling the house with a loan
house.sell_house(buyer, 50000)

# Demonstrate the updated information
print(owner)
print(buyer)
print(f"House ID: {house.ID}, Status: {house.status}, Owner: {house.owner.name}")
