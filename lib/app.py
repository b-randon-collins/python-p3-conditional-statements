def divide(num1, num2):
    try:
        quotient = num1 / num2
        print(quotient)
    except ZeroDivisionError:
        print("Error: num2 cannot be equal to 0")
    except TypeError:
        print("Error: input must be of type int or float")
    except:
        print("An error occurred")
    finally:
        print("Isn't division fun?")
divide(10,2)

# Python
# dog = "cuddly"

# if dog == "hungry":
#     owner = "Refilling food bowl."
# elif dog == "thirsty":
#     owner = "Refilling water bowl."
# elif dog == "playful":
#     owner = "Playing tug-of-war."
# elif dog == "cuddly":
#     owner = "Snuggling."
# else:
#     owner = "Reading newspaper."
# 
# print(dog, owner)

dog = "cuddly"

dict_map = {
    "hungry": "Refilling food bowl.",
    "thirsty": "Refilling water bowl.",
    "playful": "Playing tug-of-war.",
    "cuddly": "Snuggling.",
}

# Remember that a dictionary's .get() method lets us set a default value!
owner = dict_map.get(dog, "Reading newspaper.")

print(dog, owner)