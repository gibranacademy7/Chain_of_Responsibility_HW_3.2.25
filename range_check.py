# range_check.py
from number_check import NumberCheck

class RangeCheck(NumberCheck):
    def check(self, number):
        if number < 10 or number > 100:
            print(f"The number {number} is out of range (must be between 10 and 100).")
            return False
        return super().check(number)
