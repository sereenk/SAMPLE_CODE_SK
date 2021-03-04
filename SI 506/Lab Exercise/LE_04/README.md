# SI 506: Lab Exercise 04

## This week's Lab Exercise

This week's lab exercise includes five (5) problems that focus on loops and conditional statements.

## Background

For this lab, you are provided with a list that includes names of grammy award winning artists.
The list contains nested lists which include the artist's name, the genre of music for which they
are known, and the number of grammies won. You are to use `for` loops, `conditonal statements` and
functions used from previous lab excercises and problem sets to complete each problem.

```python
grammy_winners = [
    ["Whitney Houston", "Pop", 6],
    ["Michael Jackson", "Pop", 19],
    ["Carrie Underwood", "Country", 7],
    ["Adell", "Soul", 15],
    ["Beyonce", "Pop", 20],
    ["Kendrick Lamar", "Hip-Hop", 12],
    ["Drake", "R&B Rap", 5]
    ]
```

## 1.0 Problem 01 (4 points)

Loop over the `grammy_winners` list and access the name of each artist. Append each name to
the empty list named `artist_names` using list indexing.

## 2.0 Problem 02 (4 points)

Implement an `if` statement inside a `for` loop that identifies each pop artist in the `grammy_winners`
list. Add each pop artist's list to the new list named `pop_genre`.

## 3.0 Problem 03 (4 points)

Implement an `if-else` statement inside a `for` loop that identifies those artists who have won a
minimum 15 Grammies. Loop over `grammy_winners` list and for those artists with 15+ Grammies _add_
their grammy count to `grammy_count_diff`. For those who have won fewer than 15 Grammies _subtract_
their grammy count from `grammy_count_diff`.

## 4.0 Problem 04 (4 points)

Loop over the `grammy_winners` list and retrieve those artists who have won between 5 and 7 Grammies
(inclusive). Implement the appropriate `if` statement inside the `for` loop and assign each
artist that satisfies the condition to the list `five_to_seven_grammies`.

## 5.0 Problem 05 (4 points)

Loop over the the `grammy_winners` list and check the number of Grammies that the artist has won.
During each iteration of the loop, if the artist's Grammy count is greater than (`>`) the current
`count` value replace the `count` value with the artist's Grammy count _and_ assign the artist's
name to the variable `top_artist`. When the loop is finished the artist with the most Grammies
will be named the `top_artist`.
