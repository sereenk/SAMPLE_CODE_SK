# Problem Set 08

## This Week's Problem Set

This week's problem set includes 5 problems. You will continue working with dictionaries and build several functions that will allow you to read/write a comma-separated value (csv) or text (txt) file using Python. These functions can be used as your utility functions in future assignments as well as later for your own work.

## Background

The Academy Awards (more commonly known as The Oscars) are an awards ceremony that recongizes artistic and technical merit within the film industry. The 93rd Adademy Awards will be held on April 25, 2021. We will be using data from this year's [list of nominees](https://www.oscars.org/oscars/ceremonies/2021).

## Problem 01 (15 points)

The file `best_actor.txt` contains the names of all of the actors that have been nominated for the `Best Actor in a Leading Role` category as well as the film they starred in.

1. Implement a function called `read_txt()` that takes a `txt` filepath as an argument and returns a list of strings (see the function docstring for details on implementation).

2. Inside of the `main()` function, call `read_txt()` passing to it the string argument `best_actor.txt` and assign the return value to a variable called `best_actors`.

:bulb: When reading the lines of the file, make sure you remove the `newline characters ('\n')` at the end of each line.

:bulb: If you were to print `best_actors`, it should look like this:
```console
['Riz Ahmed - Sound of Metal', "Chadwick Boseman - Ma Rainey's Black Bottom", 'Anthony Hopkins - The Father', 'Gary Oldman - Mank', 'Steven Yeun - Minari']
```

## Problem 02 (15 points)

The variable `best_actress` is a list of lists, each containing the name of an actress that was nominated for the `Best Actress in a Leading Role` category as well as the movies they starred in.

1. Implement a function called `write_txt()` that takes a `txt` filepath and a list of lists as arguments and outputs the information inside of that list to a `txt` file (see the function docstring for details on implementation).

2. Inside of the `main()` function, use the `write_txt()` function to create a file called `best_actress.txt` that contains the names of each of the actresses and the movies they star in.

:bulb: When outputting to `best_actress.txt` make sure that you add a `newline character` at the end of each line.

:bulb: After completing this problem, you should see a file called `best_actress.txt` that looks like this:
```
Viola Davis - Ma Rainey's Black Bottom
Andra Day - The United States vs. Billie Holiday
Vanessa Kirby - Pieces of a Woman
Frances McDormand - Nomadland
Cary Mulligan - Promising Young Woman
```

## Problem 03 (30 points)

`nominees.csv` contains all of the movies that were nominated for the following five categories: `Animated Feature Film`, `Best Picture`, `Documentary (Feature)`, `International Feature`, and `Short Film (Live Action)`. The file has three columns: `Category`, `Title`, and `Director(s)`.

1. Implement a function called `read_csv()` that takes a csv file as an argument and returns a list of dictionaries, each representing a movie (see the function docstring for details on implementaion).

2. Inside of the `main()` function, call the `read_csv()` function passing to it the string argument `nominees.csv` and assign the return value to a variable called `films`.

:bulb: You can use the `DictReader()` method from the `csv` module to achieve this task.

## Problem 04 (20 points)

1. Implement a function called `sort_films()` that accepts a list of film dictionaries as an argument and returns a dictionary that sorts the films by category (see the function docstring for details on implementation).

2. Inside of the `main()` function, call the `sort_films()` function on the `films` list and assign the return value to a variable called `sorted_films`.

3. Using the information stored in the `sorted_films` dictionary, create five lists: `animated_films`, `best_films`, `documentaries`, `international_films`, `short_films`. These lists should contain all of the film dictonaries for the `Animated Feature Film`, `Best Picture`, `Documentary (Feature)`, `International Feature Film`, and `Short Film (Live Action)` categories respectively.

:bulb: After completing this problem, `best_films` should look like this:
```console
[{'Category': 'Best Picture', 'Title': 'Mank', 'Director(s)': 'David Fincher'}, {'Category': 'Best Picture', 'Title': 'Judas and the Black Messiah', 'Director(s)': 'Shaka King '}, {'Category': 'Best Picture', 'Title': 'Minari', 'Director(s)': 'Lee Isaac Chung'}, {'Category': 'Best Picture', 'Title': 'Nomadland', 'Director(s)': 'Chloé Zhao'}, {'Category': 'Best Picture', 'Title': 'Promising Young Woman', 'Director(s)': 'Emerald Fennell'}, {'Category': 'Best Picture', 'Title': 'Sound of Metal', 'Director(s)': 'Darius Marder'}, {'Category': 'Best Picture', 'Title': 'The Trial of the Chicago 7', 'Director(s)': 'Aaron Sorkin'}, {'Category': 'Best Picture', 'Title': 'The Father', 'Director(s)': 'Florian Zeller'}]
```

## Problem 05 (20 points)

1. Implement a function called `write_csv()` that accepts a csv filepath and a list of film dictionaries as arguments and outputs the content of those dictionaries into a `csv` file (see the function docstring for details on implementation).

2. Inside of the main() function, use the `write_csv()` function to create a file called `best_picture.csv` using the `best_films` list.

:bulb: You can use the `DictWriter()` method from the `csv` module to complete this task.

:bulb: Make sure you write the `header row` of the csv before you write the remaining rows. 