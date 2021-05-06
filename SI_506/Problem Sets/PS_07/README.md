# SI 506: Problem Set 07

## This week's Problem Set

This Problem Set focuses on working with functions, Docstrings, `for` loop, conditional statements, nested lists & dictionaries.

## Background

[Netflix](https://www.netflix.com/)  is a streaming service that offers a wide variety of award-winning TV shows, movies, anime, documentaries, and more on thousands of internet-connected devices

This week you'll be working on the data set of TV shows and movies produced by Netflix in 2020

`netflix` is a dictionary with 2 key:value pairs. `netflix["TV Show"]` and `netflix["Movie"]` are lists of dictionaries where each dictionary contains information about one TV show / movie.

## 1.0 Problem 01 (10 points)

Implement the function `extract_duration` based on the Docstring.

Sample function call: `extract_duration('46 min')`

Expected output: `46`

## 2.0 Problem 02 (20 points)

1. Implement the function `extract_month` based on the Docstring.
2. Implement the function `is_month` utilizing `extract_month` based on the Docstring.

Sample function call: `extract_month('August 20, 2020')`

Expected output: `'August'`

Sample function call: `is_month(netflix["Movie"][-2])`

Expected output: `True`

Sample function call: `is_month(netflix["Movie"][-2], 'May')`

Expected output: `False`

## 3.0 Problem 03 (10 points)

Implement the function `is_listed` based on the Docstring.

Sample function call: `is_listed(netflix["Movie"][-2], [])`

Expected output: `False`

Sample function call: `is_listed(netflix["Movie"][-2], ['Thrillers'])`

Expected output: `True`

Sample function call: `is_listed(netflix["Movie"][-2], ['Thrillers', 'Comedies', 'Documentaries'])`

Expected output: `True`

## 4.0 Problem 04 (30 points)

Implement the function `query` based on the Docstring.
   
Sample function call: `query(netflix["TV Show"], [], "May", "TV-Y7")`

Expected output: []

Sample function call: `query(netflix["TV Show"], ["TV Action & Adventure", "TV Sci-Fi & Fantasy"], None, None)`

Expected output: `[{'date_added': 'May 15, 2020', 'duration': '5 Seasons', 'listed_in': "Kids' TV, TV Action & Adventure, TV Sci-Fi & Fantasy", 'rating': 'TV-Y7', 'title': 'She-Ra and the Princesses of Power'}, {'date_added': 'January 23, 2020', 'duration': '1 Season', 'listed_in': 'TV Action & Adventure, TV Dramas, TV Horror', 'rating': 'TV-MA', 'title': 'October Faction'}]`

Sample function call: `query(netflix["TV Show"], ["Kids' TV"], None, "TV-Y")`

Expected output: `[{'date_added': 'December 22, 2020', 'duration': '1 Season', 'listed_in': "Kids' TV", 'rating': 'TV-Y', 'title': 'Rhyme Time Town Singalongs'}]`


## 5.0 Problem 05 (30 points)

Implement the `main()` function.

1. Call `query` with **keyword argument** to filter out the movies which have `'R'` rating. Assign the return value to the variable `r_movie`. :bulb: You should only pass two values to `query`)
2. Loop over `r_movie` to figure out which movie has the longest duration. Assign the movie to the variable `longest_movie`.
3. Use `is_listed` to check whether the `longest_movie` is listed in `['Dramas', 'Romantic Movies']`.
4. If it's listed, return `"<movie title> is listed!"`, otherwise return `"<movie title> is NOT listed!"`
