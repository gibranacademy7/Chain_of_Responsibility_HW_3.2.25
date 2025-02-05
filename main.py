# main.py
from range_check import RangeCheck
from divisible_by_check import DivisibleBy2Check, DivisibleBy3Check, DivisibleBy5Check, DivisibleBy7Check
from prime_check import PrimeCheck

# Create the chain of responsibility
range_check = RangeCheck()
div2_check = DivisibleBy2Check()
div3_check = DivisibleBy3Check()
div5_check = DivisibleBy5Check()
div7_check = DivisibleBy7Check()
prime_check = PrimeCheck()

# Set the chain links
range_check.set_next(div2_check)
div2_check.set_next(div3_check)
div3_check.set_next(div5_check)
div5_check.set_next(div7_check)
div7_check.set_next(prime_check)

# Test cases
test_numbers = [12, 17, 23, 100, 121, 169]

for num in test_numbers:
    print(f"\nChecking number: {num}")
    range_check.check(num)
    print('-' * 30)
