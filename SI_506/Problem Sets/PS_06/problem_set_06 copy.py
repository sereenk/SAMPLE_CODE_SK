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
    """
    Loops through a list of menu items and prints out each item

    Parameters:
        restaurant (dict): A dictionary with three lists items, prices, and cals

    Returns:
        None
    """
    pass #TODO: Replace

print_menu_items(mcdonalds)

#Problem 02 (20 points)
def most_expensive_menu_item(restaurant):
    """
    Loops through a list of menu items and determines the most expensive item

    Parameters:
        restaurant (dict): A dictionary with three lists items, prices, and cals

    Returns:
        str: A string with the name of the most expensive item
    """
    highest_price = 0
    highest_price_index = None
    pass #TODO: Replace

most_expensive_taco_bell_item = None

'#Problem 03 (35 points)
def create_menu(restaurant):'
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
    pass #TODO replace
    #return menu TODO: Uncomment when ready

subway_menu = None #TODO: Replace
mcdonalds_menu = None #TODO: Replace
burger_king_menu = None #TODO: Replace
taco_bell_menu = None #TODO: Replace

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
    pass #TODO Replace
    #return menu TODO: Uncomment when ready


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
    pass #TODO Replace
