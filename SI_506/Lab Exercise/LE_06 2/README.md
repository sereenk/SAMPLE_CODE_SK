# SI 506: Lab Exercise 06

## This week's Lab Exercise

This week's lab exercise includes four (4) problems focuses on creating functions.

## Data description

For this week's lab, you are to help a new Barista work with your store's
"new beverages of the month". Provided to you are the seven (7) new menu items
that your manager picked for this month. The drinks are assigned to the variable
name `starbucks_menu`, which includes a list of nested lists with each drink's
name and its corresponding calories.

## 1.0 Problem 01 (4 Points)

Create a function named `get_name()` that accepts a `list` representing a
beverage as an argument and returns the name of the beverage. Extract the name
of the first menu item in the `starbucks_menu` list by calling the `get_name()`
function and assigning the return value to the variable `name`.

## 2.0 Problem 02 (5 Points)

### Problem 2A

Create a function named `get_calories()` that accepts a beverage `list` as an
argument and returns the number of calories in the beverage.

Call the `get_calories()` function to return the number of calories in a
Chia Latte and assign it to the variable name `calories`.

### Problem 2B

Loop over the `starbucks_menu`. For each menu item print a formatted string
that incorporates the return values of the functions `get_name()` and
`get_calories()`. The strings must match the output below:

```commandline
Caramel Macchiato has 250 calories.
Chia Latte has 240 calories.
Flat White has 170 calories.
Chestnut Praline Latte has 330 calories.
Coffee Frapp has 230 calories.
Caramel Ribbon Crunch Frapp has 470 calories.
Matcha Green Tea Frapp has 420 calories.
```

## 3.0 Problem 03 (5 Points)

Create a function named `remove_menu_item()` that accepts two parameters: a menu
(`list`) and a menu item (`list`) to be removed. The function does not require a
specified return value.

Call the function in order to remove the last menu item from the list
`starbucks_menu`.

## 4.0 Problem 04 (6 points)

Create a function named `add_menu_item()` that defines three parameters: a menu
(`list`), a menu item (`list`) to add, and the index position in the menu to
add the item. Assign a default value of `0` to the last parameter. The function
does not require a specified return value.

Call the function in order to add the menu item `["Tea Latte", 100]` in the
_fourth_ position.