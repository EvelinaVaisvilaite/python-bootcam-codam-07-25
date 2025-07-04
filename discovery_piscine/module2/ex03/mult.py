#!/usr/bin/env python3

print("Enter the fisrt number: ")
num_1 = int(input())

print("Enter the second number: ")
num_2 = int(input())

result = num_1 * num_2 

print(f"{num_1} x {num_2} = {result}")

if result == 0:
    print("The result is positive and negative.")
elif result > 0:
    print("The result is positive.")
else:
    print("The result is negative.")



