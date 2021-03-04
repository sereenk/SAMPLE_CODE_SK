
# SI 506: Lab Exercise 03

## Background

The data for this week's lab includes African American inventors and their great inventions. African Americans have been the victims of oppression, discrimination and persecution throughout American history, with an impact on African American innovation. Despite the negative impact on innovation, these inventors and scientists have invented a multitude of items or made discoveries in the course of their lives. These inventions ranged from practical everyday devices to applications and scientific discoveries in diverse fields, including physics, biology, math, plus the medical space science.

Source: https://en.wikipedia.org/wiki/List_of_African-American_inventors_and_scientists

## This week's Lab Exercise

This week's lab exercise includes six (6) problems that focus on dictionary and tuples.

## 1.0 Problem 01 (3 Points)

| Inventor | Invention/Accomplishment |
|--------------|---------------------------|
| Marie Van Brittan Brown | Home security system|
| Alice H. Parker | Furnace for central heating |
| Leonidas Berry | Gastroscope pioneer |
| Otis Boykin | Artificial heart pacemaker control unit |
| David Crosthwait | Heating |

The table above includes inventors and their inventions. Create a dictionary from this table where the inventors are the keys and their invention is the value. Assign the dictionary to `inventors`.

The output of the dictionary should have a structure similar to:

```python
 {'Inventor 1': 'Invention',
'Inventor 2': 'Invention',
'Inventor 3': 'Invention'}
```

## 2.0 Problem 02 (3 Points)

David Crostwait's invented ventilation and air conditioning in addition to heating. His full invention is assigned to the variable `invention`. Update the key `David Crostwait` with the new variables `invention`.

:hint: Please do not **hard-code** the value, use the key to update the value like so:

```python
    dictionary['key'] = new_value
```

## 3.0 Problem 03 (3 Points)

The variable, `new_inventor`, consists of Alexander Miles, the inventor of automatic electric elevators doors as a key:value pair. Update `inventors` with this new key:value pair.

## 4.0 Problem 04 (3 Points)

Remove the first inventor from the dictionary using the `dict.pop()` method.

:bulb: You __must__ use the function `dict.pop()` method to pass the autograder.

## 5.0 Problem 05 (4 Points)

Use the variable `gastroscope_inventor` to create a tuple with just one element. Assign this tuple to the variable `tuple_gastroscope_inventor`

## 6.0 Problem 06 (4 Points)

Otis Boykin also had a medical invention. Use concatenation to add Otis Boykin to the tuple with Leonidas Berry and assign the newly created tuple to `medical_inventors`.