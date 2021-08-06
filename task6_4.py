class Car:
    def __init__(self, name, speed, colour, is_police):
        self.name = name
        self.speed = speed
        self.colour = colour
        self.is_police =is_police

    def go(self):
        return f"{self.colour} {self.name} начала движение со скоростью {self.speed}"

    def stop(self):
        return f"{self.name} совершила остановку"

    def turn(self, side):
        self.side = side
        return f"{self.name} совершила поворот {self.side}"
    def show_speed(self):
        return f"Текущая скорость машины {self.speed}"

class TownCar(Car):
    def show_speed(self, speed):
        self.speed = speed
        if self.speed >60:
            return f"Ваша скорость {self.speed} что выше положенной! Снизьте скорость"
        else: return f"Ваша скорость {self.speed}"


class SportCar(Car):
    def cool(self):
        return "Вау! У вас крутая тачка! Сильно не гоняйте"


class WorkCar(Car):
    def work(self):
        return "Ваша машина хорошо подходит для работы!"

    def show_speed(self, speed):
        self.speed = speed
        if self.speed > 40:
            return f"Ваша скорость {self.speed} что выше положенной! Снизьте скорость"
        else: return f"Ваша скорость {self.speed}"

class PoliceCar(Car):

    def police(self):
        return "Какие в полиции хорошие машины. Будьте осторожны в патруле!"

mazda = TownCar('Mazda', 75, 'green', False)
print(mazda.go())
print(mazda.turn('направо'))
print(mazda.show_speed(78))
print(mazda.stop())

audi = PoliceCar('audi', 100, 'black', True)
print(audi.go())
print(audi.police())
print(audi.stop())

lada = WorkCar('lada', 50, 'red', False)
print(lada.go())
print(lada.show_speed(50))
print(lada.show_speed(35))
print(lada.stop())