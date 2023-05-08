class BikeShop:
    def __init__(self, stock):
        self.stock = stock
        self.revenue = 0
        self.filename = "inventory.txt"

    def display_stock(self):
        print("Current Bike Inventory:")
        for key, value in self.stock.items():
            print(f"{key.title()}: {value}")

    def rent_hourly_basis(self, n):
        if n <= 0:
            print("Invalid input. Number of bikes should be greater than zero.")
            return

        if n > self.stock["hourly"]:
            print("Sorry, we don't have that many bikes available for hourly rental.")
            return

        print(f"Rented {n} bike(s) on hourly basis.")
        self.stock["hourly"] -= n
        self.revenue += n * 5
        self.save_inventory()

    def rent_daily_basis(self, n):
        if n <= 0:
            print("Invalid input. Number of bikes should be greater than zero.")
            return

        if n > self.stock["daily"]:
            print("Sorry, we don't have that many bikes available for daily rental.")
            return

        print(f"Rented {n} bike(s) on daily basis.")
        self.stock["daily"] -= n
        self.revenue += n * 20
        self.save_inventory()

    def rent_weekly_basis(self, n):
        if n <= 0:
            print("Invalid input. Number of bikes should be greater than zero.")
            return

        if n > self.stock["weekly"]:
            print("Sorry, we don't have that many bikes available for weekly rental.")
            return

        print(f"Rented {n} bike(s) on weekly basis.")
        self.stock["weekly"] -= n
        self.revenue += n * 60
        self.save_inventory()

    def rent_family_rental(self, n):
        if n <= 0:
            print("Invalid input. Number of bikes should be greater than zero.")
            return

        if n > self.stock["hourly"] + self.stock["daily"] + self.stock["weekly"]:
            print("Sorry, we don't have that many bikes available for family rental.")
            return

        print(f"Rented {n} bike(s) for family rental (30% discount applied).")
        self.stock["hourly"] -= n // 3
        self.stock["daily"] -= n // 3
        self.stock["weekly"] -= n // 3
        self.revenue += (n * 5 * 0.7) + (n * 20 * 0.7) + (n * 60 * 0.7)
        self.save_inventory()

    def return_bike(self, n):
        if n <= 0:
            print("Invalid input. Number of bikes should be greater than zero.")
            return

        print(f"Returned {n} bike(s). Thank you for using our service.")
        self.stock["hourly"] += n
        self.stock["daily"] += n
        self.stock["weekly"] += n
        self.save_inventory()

    def save_inventory(self):
        with open(self.filename, "w") as file:
            for key, value in self.stock.items():
                file.write(f"{key}, {value}\n")

    def load_inventory(self):
        try:
            with open(self.filename, "r") as file:
                for line in file:
                    rental_type, quantity = line.strip().split(",")
                    self.stock[rental_type] = int(quantity)
            print('Inventory loaded successfully.')
        except FileNotFoundError:
            print("Inventory file not found. Creating new file with default inventory.")
            with open(self.filename, "w") as file:
                for key,value in self.stock.items():
                    file.write(f"{key}, {value}\n")



class BikeRental:
    def __init__(self):
        self.stock = {"hourly": 100, "daily": 50, "weekly": 20}
        self.shop = BikeShop(self.stock)

    def display_stock(self):
        self.shop.display_stock()

    def rent_bike(self, n, rental_type):
        if rental_type == "hourly":
            self.shop.rent_hourly_basis(n)
        elif rental_type == "daily":
            self.shop.rent_daily_basis(n)
        elif rental_type == "weekly":
            self.shop.rent_weekly_basis(n)
        elif rental_type == "family":
            self.shop.rent_family_rental(n)
        else:
            print("Invalid rental type. Please choose hourly, daily, weekly, or family.")

    def return_bike(self, n):
        self.shop.return_bike(n)

    def get_revenue(self):
        return self.shop.revenue

    def load_inventory(self):
        self.shop.load_inventory()


def main():
    rental = BikeRental()
    rental.load_inventory()

    while True:
        print("\nBike Rental Shop")
        print("1. Display available bikes")
        print("2. Rent a bike")
        print("3. Return a bike")
        print("4. Display shop revenue")
        print("5. Exit")
        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            rental.display_stock()
        elif choice == "2":
            n = int(input("How many bikes would you like to rent? "))
            rental_type = input("What type of rental would you like? (hourly, daily, weekly, or family): ")
            rental.rent_bike(n, rental_type)
        elif choice == "3":
            n = int(input("How many bikes would you like to return? "))
            rental.return_bike(n)
        elif choice == "4":
            print(f"Shop revenue: ${rental.get_revenue()}")
        elif choice == "5":
            rental.shop.save_inventory()
            print("Thank you for using our service.")
            break
        else:
            print("Invalid input. Please enter a number from 1 to 5.")


if __name__ == "__main__":
    main()
