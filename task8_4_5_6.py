def validate(func):
    def wrapper(*args, **kwargs):
        try:
            func(*args, **kwargs)
        except ValueError:
            print('Недостаточно запрашиваемой техники на складе')
        except KeyError:
            print('На складе отсутсвует данный тип техники')
    return wrapper



class Warehouse:
    database = {}

    @classmethod
    @validate
    def receipt(cls, unit_type, unit_name, unit_model, unit_count):
        cls.database.get[unit_type][unit_name][unit_model]["count"] += unit_count


    @classmethod
    @validate
    def shipment(cls, unit_type, unit_name, unit_model, unit_count):
        cur_count = cls.database.get[unit_type][unit_name][unit_model]["count"]
        if cur_count < unit_count:
            raise ValueError
        else:
            cls.database.get[unit_type][unit_name][unit_model]["count"] -= unit_count

    def get_all_eq():
        for key, value in Warehouse.database.items():
            print(key, value)



class Equipment:                                #базовый класс
    def __init__(self, eq_type, name, model, count=0):
        self.eq_type = eq_type
        self.name = name
        self.model = model

        try:
            if type(count) not in [int]:
                self.__count = 0
                raise ValueError
        except ValueError:
            print("Ошибка в формате вводимых данных")
        else:
            self.__count = count
        finally:
            self.warehouse_update()

    def warehouse_update(self):
        database_info = Warehouse.database.get(self.eq_type, {})
        if self.name in database_info.keys():
            database_info_by_name = database_info[self.name]
            if self.model in database_info_by_name.keys():
                database_info_by_model = database_info_by_name[self.model]
                database_info_by_model["count"] +=self.__count
            else:
                database_info_by_name[self.model] = {"count" : self.__count}
        else:
            database_info[self.name] = {self.model : {"count" : self.__count}}

        Warehouse.database[self.eq_type] = database_info



class Copier(Equipment):
    def __init__(self, name, model, count, speed):
        super().__init__(name, model, "Copier", count)
        self.speed = speed

class Printer(Equipment):
    def __init__(self, name, model, count, colour):
        super().__init__(name, model, "Printer", count)
        self.color = colour

class PersonalComp(Equipment):
    def __init__(self, name, model, count, os):
        super().__init__(name, model, "PersonalComp", count)
        self.os = os


my_xerox = Copier('Xerox', 'TC567', 300, '50 шт/мин')
my_printer = Printer('Epson', 'EL660', 2000, ['black', 'white'])
my_pc = PersonalComp('PC1', 'Monoblock', 8000, 'Windows')

Warehouse.receipt(unit_type = 'Printer', unit_name = 'Epson', unit_model = 'EL660', unit_count = 15)
Warehouse.get_all_eq()


Warehouse.shipment(unit_type = 'PersonalComp', unit_name = 'PC1', unit_model = 'Monoblock', unit_count = 5000)
Warehouse.get_all_eq()