# START LAB EXERCISE 06
print('Lab Exercise 06 \n')

#SETUP
starbucks_menu = [
    ["Caramel Macchiato", 250],
    ["Chia Latte", 240],
    ["Flat White", 170],
    ["Chestnut Praline Latte", 330],
    ["Coffee Frapp", 230],
    ["Caramel Ribbon Crunch Frapp", 470],
    ["Matcha Green Tea Frapp", 420]
]

# END SETUP

# PROBLEM 1 (3 points)

# TODO Implement function

def get_name(beverage):
    for drink in starbucks_menu:
        drink = beverage
    return drink

name = get_name("Caramel Macchiato")

print(f"\n1. First menu item: {name}")


# PROBLEM 2A

# TODO Implement function

def get_calories(beverage):
    for drink in starbucks_menu:
        if drink == beverage:
            return drink[1]


calories = get_calories("Chia Latte")

print(f"\n2A. Calories for second menu item: {calories}")


# PROBLEM 2B
print('\n2B. Print strings:')

# TODO Implement loop; print strings


# PROBLEM 3 (5 points)

# TODO Implement function

# TODO call function

print(f"\n3. {starbucks_menu}")


# Problem 4 (6 points)

# TODO Implement function

# TODO call function

print(f"\n4. {starbucks_menu}")

# END LAB EXERCISE