# SI 506: Problem Set 01

## This week's Problem Set

This Problem Set focuses on using comments, values and types, variables, built-in functions
(`print()`, `len()`, `type()`, etc.) and performing basic arithmetic operations using Python.

## Background

Amanda Gorman is the youngest inaugural poet in U.S. history, as well as an award-winning writer and cum laude graduate of Harvard University, where she studied Sociology. She has written for the New York Times and has three books forthcoming with Penguin Random House.

## 1.0 Problem 01 (20 points)

1. Uncomment the given statements that are valid variable assignment statements.

   :bulb: "Uncomment" means remove the leading has (`#`) symbol from a line of code.

2. Create a list named `valid_variables` and add all valid variables that you uncommented
   to the list.

:warning: Do not include the name of the variable in quotes, we want to display the contents of the
variables.

## 2.0 Problem 02 (20 points)

1. Use the built-in `type()` function to return the data type for each of the following variables:
    `name`, `age` and `work_collection`. Assign the values returned in three
    new variables named: `name_type`, `age_type` and `collection_type`.

2. Use the `print()` function to print `name_type`, `age_type` and `collection_type`.

## 3.0 Problem 03 (20 points)

1. Use the string method `str.split()` to split the multiline string `inaugural_poem` into a list of
   words (use default value for split()). Then use the built-in function `len()` to count the number of
   words in the list you create. Assign the value to the variable `num_words`.

2. Calculate the average number of words _per line_ in the multiline string `inaugural_poem` and save
   it to a variable named `avg_words`.

:bulb: There are 10 lines in the multiline string `inaugural_poem`; use this fact to calculate the
average number of words per line.

## 4.0 Problem 04 (20 points)

`next_line` represents the next line of the inaugural poem.

1. Adopt the same method used in Problem 03 to calculate the number of words in `next_line` and assign it to `num_words_next`.

2. Use `num_words` and `num_words_next` to calculate the total number of words in `inaugural_poem` and `next_line`. Assign the final value to the variable `total_words`

## 5.0 Problem 05 (20 points)

1. Calculate the number of characters in the `inaugural_poem` multiline string using `len()` and
   assign the value to a variable named `num_chars_poem`.

2. Calculate the average number of characters per word in the multiline string `inaugural_poem` using
   floor division (i.e., the `//` operator). Leverage the values assigned to `num_chars_poem` and
   `num_words`. Assign the return value to `avg_chars`.

:warning: You must use the values assigned to `num_chars_poem` and `num_words` or the autograder
test for this problem will fail.
