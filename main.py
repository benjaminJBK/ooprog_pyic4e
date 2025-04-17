import json
from typing import List

from models import CarRental, Auto, PassengerCar, Truck


def load_cars_from_json(data: dict) -> List[Auto]:
    cars = []
    for item in data["cars"]:
        license_plate = item["license_plate"]
        model = item["model"]
        price = int(item["rental_price"])

        if "door_count" in item:
            door_count = int(item["door_count"])
            cars.append(PassengerCar(license_plate, model, price, door_count))
        elif "capacity" in item:
            capacity = int(item["capacity"])
            cars.append(Truck(license_plate, model, price, capacity))
    return cars


def prepared_rental() -> CarRental:
    with open("autok.json", 'r', encoding='utf-8') as f:
        data = json.load(f)

    rental = CarRental("Példa Autókölcsönző")

    for car in load_cars_from_json(data):
        rental.add_car(car)

    for rent in data["rents"]:
        rental.rent(rent["license_plate"], rent["date"])

    return rental


def main() -> None:
    rental = prepared_rental()

    while True:
        print("\n1. Elérhető járművek listázása")
        print("2. Bérlések listázása")
        print("3. Autó bérlése")
        print("4. Bérlés lemondása")
        print("0. Kilépés")
        choice = input("Válassz egy műveletet: ")

        if choice == "1":
            print(rental.list_available_cars())

        elif choice == "2":
            print(rental.list_rentals())

        elif choice == "3":
            license_plate = input("Add meg a rendszámot: ").strip().upper()
            date = input("Add meg a dátumot (ÉÉÉÉ-HH-NN): ").strip()
            print(rental.rent(license_plate, date))

        elif choice == "4":
            license_plate = input("Add meg a rendszámot: ").strip().upper()
            date = input("Add meg a dátumot (ÉÉÉÉ-HH-NN): ").strip()
            print(rental.cancel(license_plate, date))

        elif choice == "0":
            print("Kilépés...")
            break

        else:
            print("Érvénytelen választás!")
            input("\nNyomj Enter-t a folytatáshoz...")


if __name__ == "__main__":
    main()