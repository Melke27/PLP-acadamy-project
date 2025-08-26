# Base class: Smartphone
class Smartphone:
    def __init__(self, brand, model, storage):
        self.brand = brand
        self.model = model
        self.storage = storage  # in GB

    def phone_info(self):
        print(f"Brand: {self.brand}, Model: {self.model}, Storage: {self.storage}GB")

    def use(self):
        print(f"{self.model} is being used for regular tasks like calling and browsing.")

# Subclass: GamingPhone
class GamingPhone(Smartphone):
    def __init__(self, brand, model, storage, cooling_system):
        super().__init__(brand, model, storage)
        self.cooling_system = cooling_system  # e.g., "liquid cooling"

    def use(self):
        print(f"{self.model} is running high-performance games with {self.cooling_system} enabled!")

# Example usage
phone1 = Smartphone("Samsung", "Galaxy S21", 128)
phone2 = GamingPhone("Asus", "ROG Phone 5", 256, "liquid cooling")

phone1.phone_info()
phone1.use()

print("---")

phone2.phone_info()
phone2.use()
