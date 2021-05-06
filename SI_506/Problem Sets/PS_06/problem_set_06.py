subway = {
    'items': ['Spicy Italian', 'Steak & Cheese', 'Meatball Mariana', 'Oven Roasted Chicken'],
    'prices': [5.99, 9.49, 5.29, 8.49],
    'cals': [900, 680, 410, 540]
}

mcdonalds = {
    'items': ['Big Mac', 'Quarter Pounder', 'Chicken McNuggets', 'Filet-O-Fish'],
    'prices': [4.27, 4.06, 4.80, 4.06],
    'cals': [550, 520, 420, 380]
}

burger_king = {
    'items': ['Whopper', 'Crispy Chicken Sandwich', 'Chicken Fries', 'Big Fish Sandwich'],
    'prices': [4.48, 5.34, 7.27, 4.27],
    'cals': [657, 670, 429, 513]
}

taco_bell = {
    'items': ['Cheesy Gordita Crunch', 'Quesarito', 'Crunchwrap Supreme', 'Chalupa Supreme'],
    'prices': [3.59, 3.39, 3.79, 3.19],
    'cals': [500, 650, 530, 350]
}

#Problem 01 (10 points)

def print_menu_items(restaurant):

    for item in restaurant['items']:
        print(item)

    pass

print_menu_items(mcdonalds)

#Problem 02 (20 points) ??????

def most_expensive_menu_item(restaurant):
    highest_price = 0.
    highest_price_index = None

    for idx, i in enumerate(restaurant['prices']):
        if i > highest_price:
            highest_price = i
            highest_price_index = idx

    return restaurant['items'][highest_price_index]


most_expensive_taco_bell_item = most_expensive_menu_item(taco_bell)
print(most_expensive_taco_bell_item)

#Problem 03 (35 points)
def create_menu(restaurant):
    """
    Loops through a list of menu items and creates a dictionary reprentation of each one with the following key value pairs:
    'Item': < item >
    'Price' < price >
    'Cal': < Calories >

    Parameters:
        restaurant (dict): A dictionary with three lists: items, prices, and cals

    Returns:
        menu (list): A list of dictionaries, each representing a restaurant item
    """
    menu = []
    for idx, item in enumerate(restaurant['items']):
        menu_item = {}
        menu_item['Item'] = item
        menu_item['Price'] = restaurant['prices'][idx]
        menu_item['Cal'] = restaurant['cals'][idx]
        menu.append(menu_item)
    return menu

subway_menu = create_menu(subway)
mcdonalds_menu = create_menu(mcdonalds)
burger_king_menu = create_menu(burger_king)
taco_bell_menu = create_menu(taco_bell)
print(taco_bell_menu)

#Problem 04 (20 points)
def add_menu_item(menu, item, price, cal):
    """
    Creates a dictionary representation of a new menu item and adds it to the menu.

    Parameters:
        menu (list): A list of dictionaries, each representing a restaurant item
        item (str): A string with the name of a new menu item
        price (float): A flot with the price of the new menu item
        cal (int): An integer with the number of calories for the new menu item

    Returns:
        menu (list): A list of dictionaries, each representing a restaurant item
    """
    new_menu_item = {}
    new_menu_item['Item'] = item
    new_menu_item['Price'] = price
    new_menu_item['Cal'] = cal
    menu.append(new_menu_item)
    return new_menu_item

pass #TODO Replace

newly_added = add_menu_item(menu = taco_bell_menu ,item = 'Nacho Fries',price = 1.39,cal = 320)
print(newly_added)

#Problem 05 (15 points)

def print_menu(menu):
    """
    Loops through a list of menu items and prints out each item with the follwing format:
    < item >: $< price > (< Cal > Cal)

    Parameters:
        menu (list): A list of dictionaries, each representing a restaurant item

    Returns:
        None
    """
    for food in menu:
        return f"{food['Item']}: ${food['Price']} ({food['Cal']} Cal)"
    pass #TODO Replace

a = print_menu(taco_bell_menu)

print(a)
