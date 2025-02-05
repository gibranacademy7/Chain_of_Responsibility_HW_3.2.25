# divisible_by_check.py
from number_check import NumberCheck

class DivisibleBy2Check(NumberCheck):
    def check(self, number):
        if number % 2 == 0:
            print(f"The number {number} is divisible by 2, so it's not prime.")
            return False
        return super().check(number)


class DivisibleBy3Check(NumberCheck):
    def check(self, number):
        if number % 3 == 0:
            print(f"The number {number} is divisible by 3, so it's not prime.")
            return False
        return super().check(number)


class DivisibleBy5Check(NumberCheck):
    def check(self, number):
        if number % 5 == 0:
            print(f"The number {number} is divisible by 5, so it's not prime.")
            return False
        return super().check(number)


class DivisibleBy7Check(NumberCheck):
    def check(self, number):
        if number % 7 == 0:
            print(f"The number {number} is divisible by 7, so it's not prime.")
            return False
        return super().check(number)
