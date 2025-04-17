from .auto import Auto


class PassengerCar(Auto):
    def __init__(self, license_plate: str, model: str, rental_price: int, door_count: int):
        super().__init__(license_plate, model, rental_price)
        self.door_count: int = door_count

    def __str__(self) -> str:
        return f"Személyautó - {self.license_plate}, {self.model}, {self.rental_price} Ft/nap, {self.door_count} ajtó"
