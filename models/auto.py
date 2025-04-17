from abc import ABC, abstractmethod


class Auto(ABC):
    def __init__(self, license_plate: str, model: str, rental_price: int):
        self.license_plate: str = license_plate
        self.model: str = model
        self.rental_price: int = rental_price

    @abstractmethod
    def __str__(self) -> str:
        pass
