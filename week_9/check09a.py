"""
Author: Lewis Lockhart
Assignment: check09a.py
"""

while True:
    try:
        num = int(input("Enter a number: "))
        print(f"The result is: {num * 2}")
        break
    except ValueError:
        print("The value entered is not valid")
