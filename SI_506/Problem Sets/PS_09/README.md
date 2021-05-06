# SI 506: Problem Set 09

## This week's problem set

This week's problem set includes 7 problems. We will continue working with dictionaries, reading/writing files, and working with class instances, constructors, and methods.

## Background

This week, we will be working with the coolest part of Python: Classes! We will use meat consumption per capita of different countries, CO2 equivalent emission per kg consumption of different meat and other data to calculate the CO2 emission per capita and in total for a selective countries.

**country_population.csv** contains country code, name and population which is derived from [https://tradingeconomics.com/country-list/population?continent=g20]

**country_meat_consumption.csv** contains country code, meat type and meat consumption which is derived from [https://data.oecd.org/agroutput/meat-consumption.htm]

`meat_emission` in `main()` contains meat type and CO2 equivalent emission per kg meat consumption which is derived from [https://www.greeneatz.com/foods-carbon-footprint.html]

## 1.0 Problem 01 (20 Points)

### 1.1 (10 Points)
Implement the constructor, `__init__()`, of the `Meat` class following the Docstring.

### 1.2 (10 Points)
Implement the method, `emit()`, of the `Meat` class following the Docstring.


## 2.0 Problem 02 (20 Points)
### 2.1 (10 Points)
Implement the constructor, `__init__()`, of the `Country` class.

The constructor will take the following parameters:

- self
- code
- name
- population

and assign each to an instance variable of the same name. In addition, the constructor should create three instance variables `self.meat_co2_emission_per_capita` which should be initialized as an empty dictionary, `self.emission_per_capita` and `self.total_emission` which both should be initialized as a float zero. We'll update them later in other class methods.

:bulb: Read the attributes section in Docstring to help you better understand the meaning of each parameter.

### 2.2 (10 Points)

Implement the method, `__str__()`, of the `Country` class.

The return value must adhere to the following format:
```
<name> (<code>) emitted <emission_per_capita> kg CO2 caused by meat consumption per capita and <total_emission> kg in total
```

## 3.0 Problem 03 (20 Points)

Implement the method, `consume()`, of the `Country` class.

Read the function Docstring for additional implementation details.


## 4.0 Problem 04 (20 Points)

Implement the method, `calculate_total_emission()`, of the `Country` class.

Read the function Docstring for additional implementation details.


## 5.0 Problem 05 (20 Points)

Implement the method, `get_most_emittable_meat()`, of the `Country` class.

Read the function Docstring for additional implementation details.

## 6.0 Problem 06 (10 Points)

Implement the function `write_txt()`.

Read the function Docstring for additional implementation details.

## 7.0 Problem 07 (90 Points)

Complete Problem 07 in `main()` function

### 7.1 (10 Points)
1. Call `read_csv` to read **country_population.csv** into a list of dictionary and assign it to a variable `country_population`.
2. Call `read_csv` to read **country_meat_consumption.csv** into a list of dictionary and assign it to a variable `country_meat_consumption`.
3. Create an empty dictionary `meats`.
4. Loop over `meat_emission`, create instance of the `Meat` class using data from each key:value pair in the dictionary, and add a key:value pair where key is the **name** of the meat and value is the **meat instance** to `meats`.


### 7.2 (20 Points)
1. Create an empty dictionary `countries`.
2. Loop over `country_population`, create instance of the `Country` class using data from each dictionary in the list, and add a key:value pair where key is the **code** of the country and value is the **country instance** to `countries`.
3. Convert the country instance for USA to `str` and assign the string value to the variable `usa`.

:bulb: You need to convert population from `str` to `float`. 

:bulb: In the **country_population.csv** file the population is expressed in terms of millions, but you want to add the population expressed in terms of ones. So if the csv file says the population is 1.1, then the population you want to pass into the class constructor should be 1100000

:bulb: The expected value of `usa` should be
```
United States (USA) emitted 0.0 kg CO2 caused by meat consumption per capita and 0.0 kg in total
```

### 7.3 (20 Points)

1. Loop over `country_meat_consumption`, for each dictionary use country code to access the country instance, and call `consume` method of the country instance with proper arguments.
2. Assign the value of the attribute `meat_co2_emission_per_capita` of the country instance for USA to the variable `usa_meat_co2_emission_per_capita`.

:bulb: You need to convert consumption from `str` to `float` before creating the instance

### 7.4 (20 Points)

1. Loop over `countries`, calculate the total emission of each country instance using **the correct class method**.
2. Convert the country instance for USA to `str` and assign the string value to the variable `usa2`.
3. Create a list with two elements - `usa` and `usa2`. Write the list to file `usa.txt` by calling the function `write_txt`

:bulb: The expected value of `usa2` should be
```
United States (USA) emitted 1364.214 kg CO2 caused by meat consumption per capita and 448826406000.0 kg in total
```

### 7.5 (20 Points)

1. Loop over `countries` and filter the country instances whose most emittable meat is `'PIG'`, convert each country instance to string and append the string to a list `pork_lovers`
2. Write `pork_lovers` to file `pork_lovers.txt` by calling the function `write_txt`