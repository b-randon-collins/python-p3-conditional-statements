#!/usr/bin/env python3

def admin_login(username, password):
    if username.lower() == "admin" and password == "12345":
        print("Access granted")
        return "Access granted"
    else:
        print("Access denied")
        return "Access denied"
    
admin_login("sudo", "12345")
# "Access denied"
admin_login("admin", "12345")
# "Access granted"
admin_login("ADMIN", "12345")
# "Access granted"

def hows_the_weather(temperature):
    if temperature > 85:
        print("It's too dang hot out there!")
        return "It's too dang hot out there!"
    elif temperature >= 65:
        print("It's perfect out there!")
        return "It's perfect out there!"
    elif temperature >= 40:
        print("It's a little chilly out there!")
        return "It's a little chilly out there!"
    else:
        print("It's brisk out there!")
        return "It's brisk out there!"


hows_the_weather(33)
# "Brisk!"
hows_the_weather(99)
# "Too dang hot"
hows_the_weather(75)
# "Perfect!"


def fizzbuzz(num):
    try:
        if num % 3 == 0 and num % 5 == 0:
            print("FizzBuzz")
            return "FizzBuzz"
        elif num % 5 == 0:
            print("Buzz")
            return "Buzz"
        elif num % 3 == 0:
            print("Fizz")
            return "Fizz"
        else:
            print(num)
            return num
    except TypeError:
        print("Error: The input must be a number.")

fizzbuzz(1)
# 1
fizzbuzz(2)
# 2
fizzbuzz(3)
# Fizz
fizzbuzz(4)
# 4
fizzbuzz(5)
# Buzz
fizzbuzz(15)
# FizzBuzz
        
def calculator(operation, num1, num2):
    try:
        result = eval(f"{num1} {operation} {num2}")
        print(result)
        return result
    except ZeroDivisionError:
        print("Error: Division by zero")
        return "Error: Division by zero"
    except (SyntaxError, TypeError, NameError):
        print("Invalid operation!")
        return None


calculator("+", 1, 1)
# 2
calculator("-", 3, 1)
# 2
calculator("*", 3, 2)
# 6
calculator("/", 4, 2)
# 2
calculator("nope", 4, 2)
# "Invalid operation!"
# None