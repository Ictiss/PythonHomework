from abc import ABC, abstractmethod
class Clothes(ABC):
    def __init__(self, size):
        self.size = size

    @abstractmethod
    def calculation(self):
        pass

class Coat(Clothes):
    @property
    def calculation(self):
        return round(self.size/6.5 + 0.5, 2)

class Suit(Clothes):
    @property
    def calculation(self):
        return round(2*self.size + 0.3, 2)

coat = Coat(44)
suit = Suit(1.64)
print(f'Расчет ткани для пальто: {coat.calculation}')
print(f'Расчет ткани для костюма: {suit.calculation}')
print(f'Общий расход ткани: {coat.calculation + suit.calculation}')