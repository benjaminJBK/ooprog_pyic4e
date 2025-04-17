from .auto import Auto


class Truck(Auto):
    def __init__(self, license_plate: str, model: str, rental_price: int, capacity: int):
        super().__init__(license_plate, model, rental_price)
        self.capacity: int = capacity

    def __str__(self) -> str:
        return f"Teherautó - {self.license_plate}, {self.model}, {self.rental_price} Ft/nap, {self.capacity} kg teherbírás"
