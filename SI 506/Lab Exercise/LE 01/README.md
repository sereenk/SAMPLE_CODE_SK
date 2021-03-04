
# SI 506: Lab Exercise 01

## This week's Lab Exercise

This week's lab exercise includes seven (7) problems that focus on comments, variable
assignment, using built-in functions, and basic arithmetic operations.

## 1.0 Problem 01 (3 Points)

Comment out (i.e., add a hash sign (#) as the first character on the line) the variable name and
assigned value that doesn't adhere to the Python variable naming rules and conventions.

:bulb: You may need to comment out more than one (1) of the variables. Make sure you comment the whole
line.

## 2.0 Problem 02 (2 Points)

Create a list. Name the list `valid_var` and add the elements those variables that are not
commented out in Problem 01.

:bulb: You must use **exactly the same** list name provided in the instructions in order to pass
the auto grader.

## 3.0 Problem 03 (3 Points)

Use the built-in function `len()` to return the number of elements in the list `valid_var`. Assign
the return value to a new variable named `valid_var_length`.

:bulb: You __must__ use the function `len()` to get the length of `valid_var` in order to pass
the auto grader.

## 4.0 Problem 04 (3 Points)

Use the built-in function `type()` to return the data type of  `valid_var`. Assign
the return value to a new variable named `data_type`.

:bulb: You __must__ use the built-in function `type()` to get the data type of `valid_var` in order to pass
the auto grader.

## 5.0 Problem 05 (3 Points)

The variables, `si_students` (School of Information (SI) students), `coe_students` (College of Engineering (COE) students), `lsa_students` (College of Literature, Science & the Art (LSA) students) all have the student populations assigned to them as an integer. Calculate the total population among these three schools/colleges by adding all three variables.

## 6.0 Problem 06 (3 Points)

Calculate the average student population per school/college among the SI, COE, & LSA by using the `total_students` variable computed in Problem 05 and dividing it by the number of schools/colleges.

:bulb: Consider using **floor division** here.

## 7.0 Problem 07 (3 Points)

Previously you created a list by listing out the valid variables in Problem 02.
Create another list by using the string method `str.split()` to change `school_abbr_str`, a list of abbreviated schools/colleges in a string format, to a list type. Assign the return value to `school_abbr_list`.

:bulb: You __must__ use the string method `str.split()` in order to pass
the auto grader.
