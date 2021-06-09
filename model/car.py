from dataclasses import dataclass


@dataclass
class CarDto:
    carModel: str = ""
    year: str = ""
    kmDriven: str = ""
    fuel: str = ""
    sellerType: str = ""
    transmission: str = ""
    owner: str = ""
    mileage: str = ""
    engine: str = ""
    maxPower: str = ""
    torque: str = ""
    seats: str = ""
