# SI 506: Lab Exercise 07

## This week's Lab Exercise

This week's lab exercise includes five (5) problems focused on creating functions, reading docstrings, and leveraging the `main()` function.

## Data description

Over the past year owning indoor houseplants has become increasingly popular. Although houseplants can be therapeutic and a great way to bring nature inside, they can be difficult to care for. Knowing your houseplant's preference to light, water, and soil is essential to getting it the care it needs. This week's lab includes a list of dictionaries assigned to the variable `houseplants`, which includes common houseplants and their characteristics.

## 1.0 Problem 01 (4 Points)

Implement the function named `avg_height()` that defines a single parameter named `plants`. This function will loop through a plants `list`  of dictionaries and return the average value among all of the values assigned to `"Max height"`.

:bulb: The values assigned to `"Max height"` will need to be converted into an integer first. For example, a houseplant with a `"Max height"` value of `"6 feet"` will need to be changed to `6` before finding the average.

## 2.0 Problem 02 (4 Points)

Implement the function named `add_plants()` that defines two parameters: a new plants list (a nested `list`) and plants (a `list` of dictionaries). The `add_plants()` function changes the new plant nested list into key:value pairs (same as `houseplants`), adds the new key:value pairs to the plant list of dictionaries, and returns the plant list of dictionaries.

Implementation of `add_plants()` will change these lists:
```python
houseplants = [
    {"Name": "Areca Palm", "Max height": "8 feet", "Water": "Low", "Sunlight": "Part shade"},
    {"Name": "Parlor Palm", "Max height": "6 feet",  "Water": "Medium" , "Sunlight": "Part shade"} ]

new_houseplants = [
    ["Golden Pothos", "8 feet", "Medium", "Part shade"],
    ["Weeping Fig", "9 feet", "Medium", "Full sun"]]
```
into a final list that looks like this:

```commandline
[{'Name': 'Areca Palm', 'Max height': '8 feet', 'Water': 'Low', 'Sunlight': 'Part shade'},
{'Name': 'Parlor Palm', 'Max height': '6 feet', 'Water': 'Medium', 'Sunlight': 'Part shade'},
{'Name': 'Golden Pothos', 'Max height': '8 feet', 'Water': 'Medium', 'Sunlight': 'Part shade'},
{'Name': 'Weeping Fig', 'Max height': '9 feet', 'Water': 'Medium', 'Sunlight': 'Full sun'}]
```

### 3.0 Problem 03 (4 Points)

Implement the function named `large_plants()` that defines a parameter named `plants`. The function accepts a list of plants dictionaries and returns a new `list` of dictionaries with plants that have a value associated with `"Max height"` that is larger than the average `"Max height"`.

:bulb: You will call `avg_height()` within this function to create a variable used in a conditional statement.

## 4.0 Problem 04 (4 Points)

Implement the function named `soil_level()` that defines a parameter named `plants`. The function accepts a list of plants dictionaries as an argument, adds a new key `"Soil"`, and returns the plant `list` with the newly added key:value pair. The value associated with the key `"Soil"` depends on the value associated with the key `"Water"`. If the water level is `"Water": "Low"` the soil level will be `"Soil": "Dry"`, if the water level is `"Water": "Medium"` the soil level will be `"Soil": "Slightly dry"`, and if the water level is `"Water": "High"` the soil level will be `"Soil": "Never dry"`.

An example of the implementation of `soil_level()` will change:

```python
houseplant = {'Name': 'Areca Palm', 'Max height': '8 feet', 'Water': 'Low', 'Sunlight': 'Part shade'}
```

into:
```commandline
{'Name': 'Areca Palm', 'Max height': '8 feet', 'Water': 'Low', 'Sunlight': 'Part shade', 'Soil': 'Dry'}
```

## 5.0 Problem 05 (4 points)
Implement the `main()` function.

There are three steps to this section.

1. Call the `add_plants()` function and pass the arguments: `new_houseplants` and `houseplants`. Assign the output to the variable `new_houseplants_list`
2. Call the `large_plants()` function and pass the argument `houseplants`. Assign the output to the variable `large_houseplants`
3. Call the `soil_level()` function and pass the argument `houseplants`. Assign the output to the variable `final_houseplants`