from datetime import datetime
from .auto import Auto

class Rental:
    def __init__(self, car: Auto, date: datetime):
        self.car: Auto = car
        self.date: datetime  = date

    def __str__(self) -> str:
        return f"{self.car.license_plate} bérlés - {self.date.strftime('%Y-%m-%d')}, Ár: {self.car.rental_price} Ft"