# SI 506: Lab Exercise 02

## This week's Lab Exercise

This week's lab exercise includes five (5) problems, which focuses on strings and list operations.

## Background

In late 2019, the highly contagious virus, COVID-19, was first discovered in Wuhan, Hubei, China. Since then, COVID-19 made its first apperance in the United States in early 2020 and unfrotunetly had a serious impact and infected millions of US citizens. For this lab, you will be introduced to a list of confirmed cases from five states in the US. After completing this lab you will be able to show which state had the highest number of confirmed cases in January 2021.

## 1.0 Problem 01 (4 points)

The variable `us_states` is a string with US states followed by confirmed COVID-19 cases. Replace the punctuation "." with ", " and assign the new string object to a variable named `us_cases`.

:bulb: each state should be followed by a comma, then the number of cases

## 2.0 Problem 02 (4 points)

Create a list by splitting the string, `us_cases`. Assign this list to a new variable named `covid_cases`.

:bulb: Watch for spaces when using the `str.split()` function, the resultant list elements must have one space after splitting on the semicolon "; ".

## 3.0 Problem 03 (4 points)

Use the built-in list function, `list.pop()`, to remove the state that has the lowest number of cases.

## 4.0 Problem 04 (4 points)

Use list indexing to assign the state with the highest number of confirmed cases to the variable `highest_ranked`.

## 5.0 Problem 05 (4 points)

Build an f-string using the highest ranked state from the variable `highest_ranked`. Assign this string to the variable name `statement`.

The f-string has the following output:

``` "For January 2021, this state had the highest amount of confirmed COVID-19 cases: Texas, 11370 cases." ```