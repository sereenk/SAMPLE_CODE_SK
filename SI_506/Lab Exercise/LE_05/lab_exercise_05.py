# LAB EXERCISE 05
print('Lab Exercise 05 \n')

# SETUP
pop_tv_shows = [
    {"Title": "WandaVision", "Creator": ["Jac Schaeffer"], "Rating": 8.2, "Genre": "Action"},
    {"Title": "Attack on Titan", "Creator": ["Hajime Isayama"], "Rating": 8.9, "Genre": "Animation"},
    {"Title": "Bridgerton", "Creator": ["Chris Van Dusen"], "Rating": 7.3, "Genre": "Drama"},
    {"Title": "Game of Thrones", "Creator": ["David Benioff", "D.B. Weiss"], "Rating": 9.3, "Genre": "Action"},
    {"Title": "The Mandalorian", "Creator": ["Jon Favreau"], "Rating": 8.8, "Genre": "Action"},
    {"Title": "The Queen's Gambit", "Creator": ["Scott Frank", "Allan Scott"], "Rating": 8.6, "Genre": "Drama"},
    {"Title": "Schitt's Creek", "Creator": ["Dan Levy", "Eugene Levy"], "Rating": 8.5, "Genre": "Comedy"},
    {"Title": "The Equalizer", "Creator": ["Andrew W. Marlowe", "Terri Edda Miller"], "Rating": 4.3, "Genre": "Action"},
    {"Title": "Your Honor", "Creator": ["Peter Moffat"], "Rating": 7.9, "Genre": "Crime"},
    {"Title": "Cobra Kai", "Creator": ["Jon Hurwitz", "Hayden Schlossberg", "Josh Heald"] , "Rating": 8.6, "Genre": "Action"}
    ]

# END SETUP

# Problem 01 (4 points)
print('/nProblem 01')

action_shows = []

for action in pop_tv_shows:
    if action["Genre"] == "Action":
        action_shows.append(action["Title"])

print(action_shows)

# Problem 02 (4 points)
print('/nProblem 02')

high_rating = 0
highest_rated_show = None

for r in pop_tv_shows[1:4]:
    current_highest_rating = 0
    if r["Rating"] > current_highest_rating:
        current_highest_rating = r["Rating"]
    high_rating = current_highest_rating
    highest_rated_show = r["Title"]


print(high_rating)
print(highest_rated_show)

# Problem 03 (4 points)
print('/nProblem 03')

low_rating = 0
lowest_rated_show = None



for r_2 in pop_tv_shows[1:3]:
    current_lowest_rating = 9
    if r_2["Genre"] != "Action":
        if r_2["Rating"] < current_lowest_rating:
            current_lowest_rating = r_2["Rating"]
        else: continue
        low_rating = current_lowest_rating
        lowest_rated_show = r_2["Title"]


print(low_rating)
print(lowest_rated_show)


# Problem 04 (4 points)
print('/nProblem 04')

multiple_creators = []

for length in pop_tv_shows:
    if len(length["Creator"]) > 1:
        multiple_creators.append(length["Title"])


print(multiple_creators)


# Problem 05 (4 points)
print('/nProblem 05')

show_genre = []

for i in pop_tv_shows:
    if i["Genre"] != "Action" and i["Genre"] != "Drama":
        show = {'Title':i["Title"], 'Genre':i["Genre"]}
        show_genre.append(show)
    elif i["Rating"] > 9:
        show = {'Title':i["Title"], 'Genre':i["Genre"]}
        show_genre.append(show)

print(show_genre)