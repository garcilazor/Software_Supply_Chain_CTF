
class test_package:
    def __init__(self):
        # constructor
        self.f = 1

    def calc_string(self, equation):
        equation = equation.strip()
        if equation.isdigit():
            return int(equation)
        if '+' in equation:
            temp = equation.split('+')
            total = 0
            for x in temp:
                value = self.calc_string(x)
                total = total + value
            return total
        return 0