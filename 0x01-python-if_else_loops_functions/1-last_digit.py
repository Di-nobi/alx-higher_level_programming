import random

number = random.randint(-10000, 10000)
if number >= 0:
    s = number % 10
elif number < 0:
    s = number % -10
if s > 5:
    print(f"Last digit of {number} is {s} and is greater than 5")
elif s == 0:
    print(f"Last digit of {number} is {s} and is 0")
elif s < 6 and s != 0:
    print(f"Last digit of {number} is {s} and is less than 6 and not 0")
