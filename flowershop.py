class Flower:
    def __init__(self, name, price, quantity):
        self.name = name.lower()
        self.price = price
        self.quantity = quantity

    def __str__(self):
        return f"{self.name} - ${self.price:.2f} (Quantity: {self.quantity})"


class FlowerShop:
    def __init__(self):
        self.inventory = []

    def add_flower(self, flower):
        self.inventory.append(flower)

    def display_inventory(self):
        if not self.inventory:
            print("No flowers in inventory.")
        else:
            for flower in self.inventory:
                print(flower)

    def sell_flower(self, name, quantity):
        for flower in self.inventory:
            if flower.name == name:
                if flower.quantity >= quantity:
                    flower.quantity -= quantity
                    print(f"Sold {quantity} of {flower.name}")
                    if flower.quantity == 0:
                        self.inventory.remove(flower)
                    return
                else:
                    print(f"Not enough {flower.name} in inventory.")
                    return
        print(f"{name} not found in inventory.")

    def check_inventory(self, name):
        for flower in self.inventory:
            if flower.name == name:
                return flower.quantity
        return 
    
def main():
    shop = FlowerShop()
    
    while True:
        print("\nWelcome to the Flower Shop")
        print("1. Add Flower")
        print("2. Display Inventory")
        print("3. Sell Flower")
        print("4. Check Inventory")  
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter flower name: ")
            price = float(input("Enter flower price: "))
            quantity = int(input("Enter flower quantity: "))
            flower = Flower(name, price, quantity)
            shop.add_flower(flower)
            print(f"Added {flower}")

        elif choice == '2':
            shop.display_inventory()

        elif choice == '3':
            name = input("Enter flower name to sell: ")
            quantity = int(input("Enter quantity to sell: "))
            shop.sell_flower(name, quantity)

        elif choice == '4':
            name = input("Enter flower name to check: ")
            quantity = shop.check_inventory(name)
            print(f"{name} in stock: {quantity}")

        elif choice == '5':
            print("Exiting the Flower Shop. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
