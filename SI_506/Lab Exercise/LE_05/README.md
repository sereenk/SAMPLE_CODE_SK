# SI 506: Lab Exercise 05

## This week's Lab Exercise

This week's lab exercise includes five (5) problems that focus on dictionary and conditional statements.

## Background

For this lab, you are provided with a list of dictionaries that includes shows from IMDb's current list of most popular TV shows.
The dictionaries within the list contain the title, creator, rating and genre of the show.
You are to use `for` loops, `conditional statements` and
functions used from previous lab exercises and problem sets to complete each problem.

```python
pop_tv_shows = [
    {"Title": "WandaVision", "Creator": ["Jac Schaeffer"], "Rating": 8.2, "Genre": "Action"},
    {"Title": "Attack on Titan", "Creator": ["Hajime Isayama"], "Rating": 8.9, "Genre": "Animation"},
    {"Title": "Bridgerton", "Creator": ["Chris Van Dusen"], "Rating": 7.3, "Genre": "Drama"},
    {"Title": "Game of Thrones", "Creator": ["David Benioff", "D.B. Weiss"], "Rating": 9.3, "Genre": "Action"},
    {"Title": "The Mandalorian", "Creator": ["Jon Favreau"], "Rating": 8.8, "Genre": "Action"},
    {"Title": "The Queen's Gambit" , "Creator": ["Scott Frank", "Allan Scott"], "Rating": 8.6, "Genre": "Drama"},
    {"Title": "Schitt's Creek", "Creator": ["Dan Levy", "Eugene Levy"], "Rating": 8.5, "Genre": "Comedy"},
    {"Title": "The Equalizer", "Creator": ["Andrew W. Marlowe", "Terri Edda Miller"], "Rating": 4.3, "Genre": "Action"},
    {"Title": "Your Honor", "Creator": ["Peter Moffat"], "Rating": 7.9, "Genre": "Crime"},
    {"Title": "Cobra Kai", "Creator": ["Jon Hurwitz", "Hayden Schlossberg", "Josh Heald"] , "Rating": 8.6, "Genre": "Action"}
    ]
```

## 1.0 Problem 01 (4 points)

Loop over `pop_tv_shows` list and extract titles of all shows in the `"Action"` genre.
Append the titles to the list `action_shows`.

## 2.0 Problem 02 (4 points)

Loop over `pop_tv_shows` and check the value that belongs to the key `"Rating"`to find the show with the highest rating. Assign the show title to the variable `highest_rated_show` and it's rating to the variable `high_rating`.

:bulb: You will need to implement a `for` loop and conditional statement.

## 3.0 Problem 03 (4 points)

Similar to Problem 02,loop over `pop_tv_shows` and check the value that belongs to the key `"Rating"`to find the show with the lowest rating that is not the genre action. Assign the show title to the variable `lowest_rated_show` and it's rating to the variable `low_rating`.

## 4.0 Problem 04 (4 points)

Loop over `pop_tv_shows` and check the length of the value that belongs to the key `"Creator"` to find shows that have more than one creator listed. Assign the show title to the variable `multiple_creators`.

## 5.0 Problem 05 (4 points)

Loop over `pop_tv_shows` and create a new list of dictionaries with only the keys `"Title"` and `"Genre"` and their associated values of shows that **do not** have the genre `"Action"` or `"Drama"` unless the action show has a `"Rating"` of at least 9.  Save these shows as a list and assign to `show_genre`.

The expected output will look something similar to:

```python
[{"Title": "Show Title", "Genre": "Show Genre"}, {"Title": "Another Show Title", "Genre": "Another Show Genre"}]
```
