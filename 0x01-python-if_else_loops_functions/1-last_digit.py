#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)


def last(number):
    str_number = str(number)

    if number < 0:
        return "-" + str_number[-1]
    else:
        return str_number[-1]


last_num = last(number)
intege = int(last_num)


def state(intege):
    if intege > 5:
        return " and is greater than 5"
    elif intege == 0:
        return " and is 0"
    else:
        return " and is less than 6 and not 0"


num_state = state(intege)

print(f"Last digit of {number} is {last_num}{num_state}")
