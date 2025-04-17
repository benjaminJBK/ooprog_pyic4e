from datetime import datetime
from typing import List

from .auto import Auto
from .rental import Rental


class CarRental:
    def __init__(self, name: str):
        self.name: str = name
        self.cars: List[Auto] = []
        self.rentals: List[Rental] = []

    def add_car(self, car: Auto) -> None:
        self.cars.append(car)

    def rent(self, license_plate: str, date_str: str) -> str:
        try:
            date = datetime.strptime(date_str, "%Y-%m-%d")
        except ValueError:
            return "Hibás dátumformátum. Használja az ÉÉÉÉ-HH-NN formátumot."

        if date.date() < datetime.now().date():
            return "Nem lehet múltbéli dátumra foglalni."

        for car in self.cars:
            if car.license_plate == license_plate:
                for rental in self.rentals:
                    if rental.car.license_plate == license_plate and rental.date == date:
                        return "Ez az autó már foglalt erre a napra."
                self.rentals.append(Rental(car, date))
                return f"Bérlés sikeres. Ár: {car.rental_price} Ft"
        return "Nincs ilyen rendszámú autó."

    def cancel(self, license_plate: str, date_str: str) -> str:
        try:
            date = datetime.strptime(date_str, "%Y-%m-%d")
        except ValueError:
            return "Hibás dátumformátum. Használja az ÉÉÉÉ-HH-NN formátumot."

        for rental in self.rentals:
            if rental.car.license_plate == license_plate and rental.date == date:
                self.rentals.remove(rental)
                return "Bérlés lemondva."
        return "Nincs ilyen bérlés."

    def list_rentals(self) -> str:
        if not self.rentals:
            return "Nincs aktuális bérlés."
        return "\n".join(str(rental) for rental in self.rentals)

    def list_available_cars(self) -> str:
        if not self.cars:
            return "Nincs elérhető jármű."
        return "\n".join(str(car) for car in self.cars)
