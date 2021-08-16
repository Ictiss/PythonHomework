class DelNull:
    def __init__(self, dividend, divisor):
       self.dividend = dividend
       self.denominator = divisor

    @staticmethod
    def err(dividend, divisor):
        try:
            return (dividend /divisor)
        except:
            return (f"Деление на ноль недопустимо")

numb = DelNull(15, 3)
print(numb.err(15,5))
print(numb.err(15,0))
print(numb.err(15,0.05))