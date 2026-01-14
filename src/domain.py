from abc import ABC, abstractmethod

# Абстрактный класс (Базовая сущность)
class RealEstateObject(ABC):
    def __init__(self, area: float, rooms: int, price: float):
        self.area = area
        self.rooms = rooms
        self.price = price

    @abstractmethod
    def get_description(self) -> str:
        pass

# Конкретный класс - Квартира
class Apartment(RealEstateObject):
    def __init__(self, area, rooms, floor, price):
        super().__init__(area, rooms, price)
        self.floor = floor

    def get_description(self):
        return f"Квартира: {self.area} м2, комнат: {self.rooms}, этаж: {self.floor}, цена: {self.price}"

# Конкретный класс - Дом 
class House(RealEstateObject):
    def __init__(self, area, rooms, land_area, price):
        super().__init__(area, rooms, price)
        self.land_area = land_area

    def get_description(self):
        return f"Дом: {self.area} м2, участок: {self.land_area} соток, цена: {self.price}"