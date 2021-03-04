# SI 506: Problem Set 04

## This week's Problem Set

This week's problem set focuses on using conditional statements and iterating over sequences using loops.

## Background

For this week's Problem Set, you will be analyzing data from the [Billboard Year End Charts]("https://www.billboard.com/charts/year-end") on who are the top artists and what are the top songs in various categories.

## Problem 01 (10 points)

You have been provided with three lists called `country_artists`, `hip_hop_artists`, and `rock_artists` that contain the top five artist in each of those categories.

1. Create another listed called `pop_artists` that will contain the top five pop artists for 2020. The top five pop artists last year were `The Weeknd, Dua Lipa, Justin Bieber, Harry Styles, and Lewis Capaldi`

2. There were a couple of issues with the previously reported data. Justin Bieber actually wasn't in the top five (for those curious, he was number 7). Additionally, the 5th most popular pop artist was actually Post Malone. Use the approrpiate list methods to remove Justin Bieber from the list and add Post Malone to the end of it.

    :bulb: When this step is completed, the list should look like this

    ```python
    ["The Weeknd", "Dua Lipa", "Harry Styles", "Lewis Capaldi", "Post Malone"]
    ```

3. Now that we have these lists of artists in various genres, let's create a container for them. Create a dicitonary called `genres` that maps each list to its corresponding genre. The table below indicates how the keys and values should be formatted for this dictionary

    | Genre | Top Artists |
    |--------------|---------------------------|
    | Country | country_artists|
    | Hip-Hop | hip_hop_artists |
    | Pop | pop_artists |
    | Rock | rock_artists |

## Problem 02 (20 points)

In addition to ranking artist in individual categories, Billboard also has an overall top artists category. You have been provided with a tuple called `top_ten_artists` that contains the top ten overall artists from last year. Using a `for loop`, loop through the `hip_hop_artists` list. If an artist appears in that list, print out the follwing statement

```commandline
< artist > topped the Hip-Hop/R&B charts as well as the overall charts in 2020!
```

Otherwise, print the follwing statement:

```commandline
< artist > topped the Hip-Hop/R&B charts in 2020!
```

:bulb: When constructing your `if` statement, you can use the `in` membership operator to check whether or not a given value exists inside of a sequence

:bulb: Use a `formatted string literal` to create this output. It must match the statement above exactly

## Problem 03 (20 points)

You have been provided with a list called `top_five_pop_songs` that contains five dictionaries. Each dictionary has two key:value pairs: `title`, which maps to the title of the song and `artist` which maps to the artist of the song.

1. The aritist that appears the most in the top five pop songs for 2020 is Dua Lipa. Create a variable called `dua_lipa_appearances` and initialize it to 0.

2. Using a `for loop`, loop through the `top_five_pop_songs` list. Increment the value of `dua_lipa_appearances` each time she appears in a song.

:bulb: In your `if` statement, you can check the value of `artist` in order to determine if Dua Lipa is in the song

## Problem 04 (30 points)

You are provided with two lists, one called `top_twenty_five_songs` which represents the top twenty five songs on the Billboard charts and another called `artist_appearances`. The artists that appeared the most in the top 25 songs overall category this year were `DaBaby`, `Harry Styles`, `Justin Bieber`, `Lewis Capaldi`, `Roddy Ricch`, and `The Weeknd`. Each item in the `artist_appearances` list contains a dictionary with two key, value pairs: `"artist"` which represents the artist's name and `"appearances"` which represents the number of times that artist appeared in the top twenty five songs. Using a similar appraoch to the one you took in Problem 3, loop through the `top_twenty_five_songs` list. Each time one of these artists appears, increment their respective number of appearances.

:bulb: Unlike in Problem 3, `"artists"` in the `top_twenty_five_songs` dictionaries now maps to a list instead of just a string. You may need to perform a `nested loop` in order to access the individual artists.

## Problem 05 (20 points)

1. You are given two variables, called `most_appearances` and `artist_name`. Loop through the `artist_appearances` list to determine which artist had the most appearances in the top twenty five songs.

   :bulb: As you loop through `artist_appearances`, update the values of `most_appearances` and `artist_name` whenever you come across a larger value.

2. Using `artist_name` and `most_appearances` print the following statment to display which artist appeared the most in the top twenty five songs:

   ```commandline
   < artist > appeared the most in the top 25 songs with < appearances > appearances.
   ```

:bulb: Use a `formatted string literal` to create this output. It must match the statement above exactly
