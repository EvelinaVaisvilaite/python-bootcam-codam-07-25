#!/usr/bin/env python3

print("Enter a number: ")
tableNum = int(input())

tableSize = range(0,10)
for column in tableSize:
    result = column * tableNum
    print (f"{column} x {tableNum} = {result}")


