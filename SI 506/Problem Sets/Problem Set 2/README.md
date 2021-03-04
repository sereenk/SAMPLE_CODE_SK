# SI 506: Problem Set 02
## This week's Problem Set

This week's problem set focuses on sequence indexing and slicing, list methods, string methods, and formatting values as strings using formatted sting literals (f-strings).

## Background
How many COVID-19 tests have been administered? How many COVID-19 vaccines have been given? In this problem set, we'll use data from the [COVID-19 Dashboard](https://campusblueprint.umich.edu/dashboard/) to get a better idea of how COVID-19 has been handled on campus.

## 1.0 Problem 01 (20 points)

In the weeks from 12/27 - 01/17, UM has reported **70, 75, 126, 144, 170** positive cases
weekly. We provide a list of positive cases named `cases`.

1. Use list indexing to return the latest positive case number in `cases` and assign it to a variable
   named `cases_latest`.

2. An error exists in the data. The first element of `cases` is actually **67** instead of
   **70**. Please update the list with the correct value using list indexing.

3. Last week (the week of 01/24), the number of reported cases was 267. Add this value to the end of the list using the appropriate list method

## 2.0 Problem 02 (20 points)

In the last five weeks (from 12/27 - 01/24), UM has conducted **2143, 4486, 6765, 16501, 20685** tests
weekly.

1. Create a list called `tests`. Add the weekly test numbers to `tests` in chronological
   order.

2. What was the number of tests administered in just the last three weeks? Assign the values from the last three weeks to a new list called `tests_last_three`

   :bulb: Use `list slicing` to get a sublist of `tests`

3. Now that you can create a list and make a slice of it, let's see if you can reverse a list. Using `slicing`, create a new list called `tests_reverse` that has the reverse of the `tests` list (ie: **20685, 16501, 6765, 4486, 2143**)

   :bulb: The `step` of a list slice doesn't always have to be in a postive (left-right) direction

## 3.0 Problem 03 (20 points)

Every day, the COVID-19 Dashboard is updated with the total number of vaccines that have been administered. We have provided a string called `vaccines` that has the values from six days last week (01/26 - 01/31), separated by a dash `('-')`. Note that at the start and end of `vaccines`, there are spaces.

Using string methods, create a list of strings that matches the list `['39,896', '41,826', '44,154', '46,458', '48,634', '50,090']`. Assign the list of strings to
a variable named `vaccines_list`.

:bulb: Use a combination of the `str.split()` and `str.strip()` methods to achieve this task

:bulb: If you use `chaining` you can even do this all in one line!

## 4.0 Problem 04 (20 points)

In this problem, we have provided you with a list called dates.

Reverse this list, so that the dates are in order and then use the `str.join()` method on this reversed list to create a new string called `dates_str` where each data is separated by a pipe symbol (`|`). In other words, the value assigned to `dates_str` _must_ match the string `'January 26th|January 27th|January 28th|January 29th|January 30th|January 31st'`

:bulb: You can call the `join()` method on a list slice (consider Problem 2 when reversing the list)

## 5.0 Problem 05 (20 points)

1. Use a formatted string literal (f-string) to generate a string named `vaccines_26th` that summarizes
   the number of vaccines given on the 26th of January.

   The value assigned to `vaccines_26th` _must_ implement the following text format:

    ```commandline
    As of < date >, UM has administered < vaccine_num > vaccines.
    ```

    :exclamation: Use of `< some_var >` indicates that a variable expression is to be inserted into the
    string.

   :bulb: `date` is an element of `dates` and `vaccine_num` is an element of `vaccines_list`.

2. Similarly, use a formatted string literal (f-string) to generate the string `vaccines_31st` that
   summarizes the number of vaccines given on the 31st of January. Use
   the same text format as described above in problem 5.1.