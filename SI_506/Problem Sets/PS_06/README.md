# SI 506: Problem Set 06

## This week's Problem Set

This week's problem set focuses on creating user-defined functions.

## Background

For this week's Problem Set, you will be using python dictionaries to represent menus from the four largest fast food chains in the United States (according to [Datafiniti](https://datafiniti.co/fast-food-restaurants-america/)) with prices obtained from [Fast Food Menu Prices](https://www.fastfoodmenuprices.com/).

## Problem 01 (10 points)

You have been provided with four dictionaries, each containing information on menu items from the four largest fast food chains: `Subway`, `McDonald's`, `Burger King`, and `Taco Bell`. Each dictionary has three key:value pairs: `'items'`, which represents the name of the menu items, `'prices'` which represents the prices corresponding to those menu items, and `'cals'` which represents the number of calories each menu item contains. For each of these lists, the indexes correspond to each other (e.g., the `'Spicy Italian'` at Subway costs $`5.99` and has `900` Calories).

Implement a function called `print_menu_items()` that accepts one parameter: `restaurant`, a `dict` that represents a fast food chain. This function should `loop` through this restaurant's list of menu items and print each one out.

:bulb: After calling this function on `mcdonalds`, the output should be the following:
```console
Big Mac
Quarter Pounder
Chicken McNuggets
Filet-O-Fish
```

## Problem 02 (20 points)

1. Implement a function called `most_expensive_menu_item()` which accepts one parameter: `restaurant`, a `dict` that represents a fast food chain. This function should loop through this restaurant's list of prices to determine the most expensive item. `most_expensive_menu_item()` should then `return` the name of the most expensive item at that restaurant.

    :bulb: Remember that the indexes of each list in a `restaurant` correspond to each other. If, while looping, you use a function to obtain both the value of a price and its index, you can use that same index on the restaurant's `items` list.

2. Call the `most_expensive_menu_item()` function on the `taco_bell` dictionary and assign its result to a variable called `most_expensive_taco_bell_item`.
    :bulb: If you print `most_expensive_taco_bell_item`, the output should be the following:
    ```console
    Crunchwrap Supreme
    ```

## Problem 03 (35 points)

While our current `restaurant` dictionaries do allow us to represent the restaurant menu items, referencing multiple lists for each menu item is inconvenient. Lets see if we can create a better way of representing the menus of these restaurants.

1. Implement a fuction called `create_menu()` that accepts one parameter: `restaurant`, a `dict` that represents a fast food chain. Inside of the function is an initially empty `list` called `menu`. `create_menu()` should loop through the lists inside of each restaurant and create a dictionary for each menu item. This dictionary should have three key:value pairs: `'Item'`, which reprents the name of the menu item, `'Price'`, which represents the price of the menu item, and `'Cal'`, which represents the number of Calories for that menu item. The dictionary should then be `appended` to `menu`. This function should `return` a list of dictionaries in which each dictionary represents a single menu item.

    :bulb: There are multiple ways to go about solving this problem. A good idea would be to loop through the indexes as well as the values in one of the lists and then use those indexes to access the items in the other two lists.

2. Create four variables called `subway_menu`, `mcdonalds_menu`, `burger_king_menu`, and `taco_bell_menu`. Assign the results of calling `create_menu()` on `subway`, `mcdonalds`, `burger_king`, and `taco_bell` to `subway_menu`, `mcdonalds_menu`, `burger_king_menu`, and `taco_bell_menu` respectively. 

    :bulb: If you were to print `subway_menu`, the output should be the following:
    ```console
    [{'Item': 'Spicy Italian', 'Price': 5.99, 'Cal': 900}, {'Item': 'Steak & Cheese', 'Price': 9.49, 'Cal': 680}, {'Item': 'Meatball Mariana', 'Price': 5.29, 'Cal': 410}, {'Item': 'Oven Roasted Chicken', 'Price': 8.49, 'Cal': 540}]
    ```


## Problem 04 (20 points)

Now that we have our lists of menu items, let's create a function that allows us to add menu items to our lists.

1. Implement a function called `add_menu_item()` that accepts four parameters: `menu`, a `list` that represents the menu of a restaurant, `item`, a `str` that represents the name of a new menu item, `price`, a `float` which represents the price of the new menu item, and `cal` an `int` that represents the number of calories a menu item has. This function should create a new dictionary (with the same key:value pairs as in Problem 03) and `append` it to the `menu`. This function should then `return` the newly updated menu.

2. Using the `add_menu_item()` function, add a new item called `'Nacho Fries'` to the `taco_bell_menu`. `Nacho Fries` should have a `price` of $`1.39` and have `320` Calories.


## Problem 05 (15 points)

Now that we have created everything we need to store and modify our menus, let's create a more clear way to output them. Implement a function called `print_menu()` that accepts one parameter: `menu`, a `list` of dictionaries that reprents the menu of a restaurant. This function should loop through each dictionary in the list and print out the item along with its price and Calorie count in the following format:
```
< item >: $< price > (< calories >)
```

:bulb: The output needs to match this format exactly, otherwise it will not pass the autograder

:bulb: If you were to call `print_menu()` on the `taco_bell_menu` the output should be the following:
```console
Cheesy Gordita Crunch: $3.59 (500 Cal)
Quesarito: $3.39 (650 Cal)
Crunchwrap Supreme: $3.79 (530 Cal)
Chalupa Supreme: $3.19 (350 Cal)
Nacho Fries: $1.39 (320 Cal)
```