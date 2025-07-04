#!/usr/bin/env python3

number_input = float(input("Give me a number: "))

whole_part = int(number_input)  #extracts the whole number part
decimal_part = number_input - whole_part #gives the decimal part 

if decimal_part > 0:
    rounded_number = whole_part + 1
else:
    rounded_number = whole_part
print(rounded_number)

