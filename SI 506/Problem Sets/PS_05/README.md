# SI 506: Problem Set 05

## This week's Problem Set

This Problem Set focuses on working with `for` loop, conditional statements, dictionary methods, list of dictionaries.

## Background

[Australian Open](https://ausopen.com/) ended last weekend. Novak Djokovic and Naomi Osaka won the title.
The tournament is the first of the four [Grand Slam](https://en.wikipedia.org/wiki/Grand_Slam_(tennis)) tennis events held each year, preceding the French Open, Wimbledon, and the US Open.

This week you'll be working on the data set of Grand Slam men's and women's singles champions from 2015 to 2019

`mens_champions` and `womens_champions` are lists of dictionaries. For each dictionary, it contains 5 key:value pairs

## 1.0 Problem 01 (20 points)

Loop over `womens_champions` and for each dictionary check the value associated with the key `'seed'` to figure out who won the Grand Slam with the largest seed number. Assign the champion name to the variable `dark_horse` and their seed to the variable `dark_horse_seed`

:bulb: You will need to use a `for` loop, a single-condition conditional statement to solve Problem 01.

## 2.0 Problem 02 (20 points)

Create an empty list `USOpen_native_winners`. Loop over `womens_champions` and for each dictionary check the values associated with the key `'Country'` and `'Major'`, and append the names of champions who were from the `'USA'` and won the `'us open'`.

:bulb: You will need to use a `for` loop, a multiple-condition conditional statement to solve Problem 02.

## 3.0 Problem 03 (20 points)

Loop over `mens_champions` to create a dictionary `mens_champions_times` where key is the name of the champion and value is number of times that they have won the Grand Slam from 2015 - 2019

The expected value of `mens_champions_times` is:

```python
{'Novak Djokovic': 9, 'Stan Wawrinka': 2, 'Andy Murray': 1, 'Roger Federer': 3, 'Rafael Nadal': 5}
```

:bulb: You need to handle `KeyError`, i.e. if the name of the champion doesn't exist in `mens_champions_times`, you need to initialize the key:value pair first.

:bulb: When looping over `mens_champions`, for each dictionary, you need to increment the value of the champion by **1** in `mens_champions_times`

## 4.0 Problem 04 (20 points)

Loop over the key:value pairs of `mens_champions_times` to figure out who have won the most Grand Slam from 2015 to 2019. Assign the champion name to the variable `most_GS_champion` and assign the number of winning times to the variable `most_GS_times`

:bulb: You will need to use a dictionary method, a for loop, a single-condition conditional statement to solve Problem 04.

## 5.0 Problem 05 (20 points)

Use similar methods in PS03 & PS04 to figure out the women's singles player who have won the most `'australian open'`. Assign the champion name to the variable `most_AO_champion` and assign the number of winning times to the variable `most_AO_times`

:bulb: You can create a dictionary `womens_AO_times` where key is the name of the champion and value is number of times that they have won the `'australian open'` from 2015 - 2019. Then loop over `womens_AO_times` to find out the results
