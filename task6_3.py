class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):
    def get_full_name(self):
        return f"Полное имя сотрудника:  {self.surname} {self.name}."

    def get_total_income(self):
        inc = self._income['wage'] + self._income['bonus']
        return f"Полный доход: {inc}"


Felix = Position('Felix', 'Lee', 'dancer', 120000, 15300)
Han = Position('Jisung', 'Han', 'music producer', 150000, 23000)
print(Felix.get_full_name())
print(Felix.get_total_income())
print(Han.get_full_name())
print(Han.get_total_income())
