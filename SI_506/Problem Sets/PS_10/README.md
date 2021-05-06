# SI 506: Problem Set 10

## This week's problem set
This week's problem set introduces the [Star Wars API (SWAPI)](https://swapi.py4e.com/about), the requests library and JSON objects. We will also continue working with classes and objects, dictionaries, file input and output, functions, class methods, etc.


## Background
[Star Wars](https://www.starwars.com/) is one of the most popular media franchises in the world featuring nine films as well as other media, including several TV series, video games, novel, theme parks, etc. The franchise is about an epic space saga of humans, several alien species, and robots or 'droids' who co-exist 'A long time ago in a galaxy far, far away.' These characters travel around different planets in the galaxy using starships that can travel through 'hyperspace' at the speed of light. A mystical power known as the 'Force' exists as an energy field created by all living beings that binds the galaxy together. Those whom 'the force is strong with' possess various superpowers. The Force is often used by two major knightly orders who are at conflict with each other: the Jedi, who are the peacekeepers of the Galaxy use the light side of the force and the Sith who use the dark side of the force to manipulate fear and destruction. The Galactic Empire is in control of the Sith and the rebellion forces are in a civil war with the Empire that spans several decades and timelines. Learn more about the Star Wars Universe on [Wookiepedia](https://starwars.fandom.com/wiki/Main_Page).

In this problem set, you will be working with a JSON file `'obi_wan.json'` which contains incomplete information on the character: `Obi-Wan Kenobi`. You will be calling the `SWAPI API` to get basic information on this character as well as General `Leia Organa` and link them to the films that they appear in.

## Problem  01 (20 points)
Implement the `get_swapi_resource()` function. When making an HTTP GET request, `params` do not need to be passed if it is using the default value `None`. Follow the docstring for further implementation details.

:bulb: Use an `if condition` to check if the `params` dictionary is `None` while making the request.<br>
:bulb: To convert your response to a JSON object, use the `<response>.json()` function.

## Problem 02 (15 points)
Implement the `read_json()` function. Use `json.load()` to parse the file into a JSON object and return it. Read the docstring for more details.

## Problem 03 (15 points)
Implement the `write_json()` function. Use the `json.dump()` function with an argument `indent=2`. Read the docstring for more details.

## Problem 04 (35 points)
Implement the `Film` class with the following methods:
1. Implement the `__init__()` method using the parameters described in the docstring. (7.5 points)

2. Read the docstring and implement the `__str__()` method. (7.5 points)

3. Implement the `jsonable()` method. The `jsonable()` method returns a JSON friendly implementation of the object. Use a dictionary literal - {} rather than built-in dict() to avoid built-in lookup costs.The return of this method is a dictionary with the following format: (10 points)
```
{
    "title": < title >,
    "episode_id": < episode_id >,
    "year": <year>,
    "url": < url >
}
```

## Problem 05 (15 points)
Implement the `convert_to_film()` function. This function should take the appropriate values from the `film_dict` and use them to instantiate the `Film` class.

:bulb: `film_dict` does not have a key called `'year'`, instead it has a key called `'release_date'`, which contains a string with the following format:

    'YYYY-MM-DD'

Extract the year from this string and use that for the `year` parameter of the `Film` class.

## Problem 06 (55 points)
Implement the `Person` class with the following methods:
1. Implement the `__init__()` method using the parameters described in the docstring. (7.5 points)

2. Read the docstring and implement the `__str__()` method. (7.5 points)

3. Implement the `update_films()` method. This method converts the `films` instance variable from a list of URLs to a list of `Film` objects. For each film URL, call the function `get_swapi_resource()` in order to return a SWAPI JSON representation of the film and decode it to a Python dictionary.  Pass the film dictionary as an argument to `convert_to_film` to create a `Film` object for each film. You can store the returned objects to a local list.  Assign this list of `Film` objects to the `films` instance variable. (15 points)

4. Implement the `jsonable()` method. The `jsonable()` method returns a JSON friendly implementation of the `Person` object. Use a dictionary literal - {} rather than built-in dict() to avoid built-in lookup costs.The return of this method is a dictionary with the following format: (10 points)
```
{
    "name": < name >,
    "hair_color": < hair_color >,
    "skin_color": < skin_color >,
    "eye_color": < eye_color >,
    "gender": < gender >,
    "films": [ < films > ],
    "url": < url >
}
```

:bulb: `Film` objects are not JSON friendly by default, you may need to make use of the `jsonable()` method of the `Film` class when implementing this method.

## Problem 07 (15 points)
Implement the `convert_to_person()` function. This function should take the appropriate values from the `person_dict` and use them to instantiate the `Person` class. Upon creating the `Person` instance, it should also `update` that instance's `film` urls to be `Film` objects.

## Problem 08 (15 points)
1. Inside of the main function, call the `read_json()` function to parse the JSON file `obi_wan.json`  and assign the return value to a variable named `obi_wan_dict`.

2. Create an instance of the `Person` class by calling the `convert_to_person()` function, passing in `obi_wan_dict` as an argument. Assign the return value to a variable named `obi_wan`.

3. Use the `write_json()` function to create a file called `updated_obi_wan.json`. This file should contain a JSON friendly representation of `obi_wan`.

:bulb: Here is an exerpt of what the complete `updated_obi_wan.json` file should look like:
```
{
  "name": "Obi-Wan Kenobi",
  "hair_color": "auburn, white",
  "skin_color": "fair",
  "eye_color": "blue-gray",
  "gender": "male",
  "films": [
    {
      "title": "A New Hope",
      "episode_id": 4,
      "year": "1977",
      "url": "https://swapi.py4e.com/api/films/1/"
    },
    {
      "title": "The Empire Strikes Back",
      "episode_id": 5,
      "year": "1980",
      "url": "https://swapi.py4e.com/api/films/2/"
    },
    ...,
  ],
  "url": "https://swapi.py4e.com/api/people/10/"
}
```

## Problem 09 (15 points)
1. Call `get_swapi_resource()` using a `search` parameter of `leia`. Use the results of this call to assign a dictionary to the variable `leia_dict`.


    :bulb: The following is an excerpt of what a typical SWAPI JSON response looks like when searching for people. You have to access the value of the key `"results"` which is a list. You then only need to extract the first element of the list. You can store this data into a list with a name of your choice.
    ```
    {
        "count": 1,
        "next": null,
        "previous": null,
        "results": [
            {
                "name": "Luke Skywalker",
                "height": "172",
                "mass": "77",
                "hair_color": "blond",
                "skin_color": "fair",
                ...,
                "films": [
                    "https://swapi.py4e.com/api/films/1/",
                    "https://swapi.py4e.com/api/films/2/",
                    "https://swapi.py4e.com/api/films/3/",
                    "https://swapi.py4e.com/api/films/6/",
                    "https://swapi.py4e.com/api/films/7/"
                ],
                ...,
                "url": "https://swapi.py4e.com/api/people/1/"
            }
        ]
    }
    ```

2. Create an instance of the `Person` class by calling the `convert_to_person()` function, passing in `leia_dict` as an argument. Assign the return value to a variable named `leia`.

3. Use the `write_json()` function to create a file called `leia.json`. This file should contain a JSON friendly representation of `leia`.

:bulb: Here is an exerpt of what the complete `leia.json` file should look like:
```
{
  "name": "Leia Organa",
  "hair_color": "brown",
  "skin_color": "light",
  "eye_color": "brown",
  "gender": "female",
  "films": [
    {
      "title": "A New Hope",
      "episode_id": 4,
      "year": "1977",
      "url": "https://swapi.py4e.com/api/films/1/"
    },
    {
      "title": "The Empire Strikes Back",
      "episode_id": 5,
      "year": "1980",
      "url": "https://swapi.py4e.com/api/films/2/"
    },
    ...,
  ],
  "url": "https://swapi.py4e.com/api/people/5/"
}
```
