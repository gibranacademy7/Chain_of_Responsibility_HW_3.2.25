# prime_check.py
from number_check import NumberCheck


class PrimeCheck(NumberCheck):
    def check(self, number):
        if number <= 1:
            print(f"The number {number} is not prime.")
            return False

        for i in range(2, int(number ** 0.5) + 1):
            if number % i == 0:
                print(f"The number {number} is divisible by {i}, so it's not prime.")
                return False

        print(f"The number {number} is prime.")
        return True
