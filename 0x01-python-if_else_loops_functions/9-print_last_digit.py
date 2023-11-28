#!/usr/bin/python3
def print_last_digit(number):
    digits_str = str(number)
    digit = digits_str[-1] if number >= 0 else "-" + digits_str[-1]
    return int(digit)
