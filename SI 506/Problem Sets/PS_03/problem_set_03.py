# START PROBLEM SET 03
print('Problem Set 03')

# PROBLEM 1 (10 points)
print('\nProblem 1')
shijingshan = ('Big Air',)
zhangjiakou = ('Cross', 'Halfpipe', 'Parallel slalom', 'Slopestyle',)
snowboarding_events = shijingshan + zhangjiakou

print(snowboarding_events)

# PROBLEM 2 (10 points)
print('\nProblem 2')
sports = ["Luge", "Ice hockey", "Curling", "Skating", "Biathlon", "Bobsledding", "Skiing"]


a = sports[4]
b = sports[5]
c = sports[2]
d = sports[1]
e = sports[0]
f = sports[3]
g = sports[6]


sports_new = [a,] + [b,]+ [c,]+ [d,]+ [e,]+ [f,]+ [g,]

print(sports_new)

# PROBLEM 3 (20 points)
#Part1
print('\nProblem 3')
skating_disciplines = "Figure skating|Short track speed skating|Speed skating"
skating_disciplines_lower = skating_disciplines.lower()
skating_disciplines_list = skating_disciplines_lower.split("|")

print(skating_disciplines_lower)
print(skating_disciplines_list)

#part2

events_count = [5,9,14]
#figure_skating = {"name": "figure skating","count": "5"}

figure_skating = {"name": "figure skating","count": 5}

short_track_speed_skating = {"name": "short track speed skating","count": 9}

speed_skating = {"name": "speed skating","count": 14}

# PROBLEM 4 (20 points)
print('\nProblem 4')
#part 1

figure_skating["name"] = 'Figure_Skating'
short_track_speed_skating["count"] = 12

speed_skating.pop("count")

print(figure_skating)

print(short_track_speed_skating)

print(speed_skating)

# PROBLEM  5 (20 points)
print('\nProblem 5')
sports_dict = {}
sports_dict['Skating'] = []

sports_dict['Skating'].append(figure_skating)
sports_dict['Skating'].append(short_track_speed_skating)
sports_dict['Skating'].append(speed_skating)

sports_dict['Skating'].pop(-1)

print(sports_dict)


# PROBLEM 6 (20 points)
print('\nProblem 6')
curling = {"Curling": [{"name": "Curling", "count": 3}]}

sports_dict.update(curling)
print(sports_dict)


word_count = len(curling['Curling'][0]['name'])
print(word_count)