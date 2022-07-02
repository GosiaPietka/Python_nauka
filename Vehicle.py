class Vehicle:

    color = "Biały"

    def __init__(self, name, max_speed, mileage, capacity):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage
        self.capacity = capacity

    def seating_capacity(self, capacity):
        return f"Liczba miejsc siedzących w {self.name} to {capacity} pasażerów"

    def fare(self):
        return self.capacity * 100

class Bus(Vehicle):
        def seating_capacity(self, capacity=50):
            return super().seating_capacity(capacity)

        def fare(self):
            amount = super().fare()
            amount += amount * 10 / 100
            return amount

class Car(Vehicle):
    pass

School_bus = Bus("Szkolne Volvo", 180, 100, 12)

print("Nazwa pojazdu:", School_bus.name, "Prędkość:", School_bus.max_speed, "Przebieg:", School_bus.mileage)

School_vehicle = Vehicle("Szkolne Volvo", 180,100, 12)
print(School_vehicle.seating_capacity(100))

School_bus = Bus("Szkolny bus Volvo", 180, 100, 12)
print(School_bus.seating_capacity())

School_bus = Bus("Szkolne Volvo", 12, 100, 50)
print("Całkowita opłata za przejazd autobusem wynosi:", School_bus.fare())

