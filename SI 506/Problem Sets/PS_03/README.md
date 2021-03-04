# SI 506: Problem Set 03

## This week's Problem Set

This Problem Set focuses on working with dictionaries, tuples, strings and lists.

## Background

With just one year to go to the Olympic Winter Games Beijing 2022, the excitement is growing among winter sports athletes and fans from around the world.

From 4–20 February 2022, the best winter athletes will gather in the Chinese capital as well as Zhangjiakou to compete for 109 gold medals.

:bulb: [Official Olympic Website](https://www.olympic.org/beijing-2022)

## 1.0 Problem 01 (10 points)

1. Shijingshan District, a district in urban area of Beijing will feature the snowboarding `'Big Air'` event. Zhangjiakou city, Hebei province will feature all other snowboarding events: `'Cross'`, `'Halfpipe'`, `'Parallel slalom'`, `'Slopestyle'`. Create two tuples `shijingshan` and `zhangjiakou`, which contain the snowboarding events.

2. **Concatenate** tuples `shijingshan` and `zhangjiakou` together to form a new tuple `snowboarding_events`

The expected value of `snowboarding_events` is

```python
('Big Air', 'Cross', 'Halfpipe', 'Parallel slalom', 'Slopestyle')
```

## 2.0 Problem 02 (10 points)

1. The list `sports` contains 7 sport of the Winter. Use **list slicing** and **list concatenation** to generate a new list `sports_new` where strings are sorted in **alphabetical order**.

The expected value of `sports_new` is

```python
['Biathlon', 'Bobsledding', 'Curling', 'Ice hockey', 'Luge', 'Skating', 'Skiing']
```

:exclamation: In order to pass the autograder, please don't **hard-code** the value for `sports_new` or use the method `list.sort()`

:bulb: There are multiple ways of solving problem 01. One possible way is:

   1. slice `["Biathlon", "Bobsledding"]`
   2. reverse slice `["Luge", "Ice hockey", "Curling"]`
   3. slice `["Skating"]` and slice `["Skiing"]`
   4. concatenate 1,2,3 together to form `sports_new`

## 3.0 Problem 03 (20 points)

Each sport might have multiple disciplines and each discipline can have multiple events.

1. `skating_disciplines` contains three disciplines of skating separated by pipe `'|'`. Convert `skating_disciplines` to lower case, split it on the pipe and assign the value to the variable named `skating_disciplines_list`

2. `events_count` contains the event count for three skating disciplines respectively. Generate three dictionaries with names `figure_skating`, `short_track_speed_skating`, `speed_skating`. Each dictionary contains two key-value pairs following the format:

```
{
   "name": <discipline name>,
   "count": <event count>
}
```

:bulb: Use list indexing to access the skating discipline name from `skating_disciplines_list` and events count from `events_count`

## 4.0 Problem 04 (20 points)

1. Use `str.replace()`, `str.title()` to change the `name` of `figure_skating` from `'figure skating'` to `'Figure_Skating'`

2. Update the `count` of `short_track_speed_skating` from `9` to `12`

3. Remove the key:value pair associated with the key `'count'` from `speed_skating`

## 5.0 Problem 05 (20 points)

1. Use **dictionary literal** to create an empty dictionary named `sports_dict`

2. Add a new key-value pair to `sports_dict`, where key is `'Skating'` and value is an empty list

3. Append three dictionaries `figure_skating`, `short_track_speed_skating`, `speed_skating` to the list under the key `'Skating'` in `sports_dict`

4. Use `list.pop()` to remove the last element from the list

## 6.0 Problem 06 (20 points)

1. Update `sports_dict` with the given dictionary `curling`
2. Calculate the sum of the number of words used in the values under the key `name`. Assign the sum to the variable `word_count`

:exclamation: In order to pass the autograder, please don't **hard-code** the value for `word_count`

:bulb: There are multiple ways of solving Problem 05. One possible way is to access each value using correct key and index, then use `str.split()`, `len()`
