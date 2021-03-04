# START LAB EXERCISE 02
print('Lab Exercise 02 \n')

us_states = 'Michigan.1358; Hawaii.103; Washington.2104; Texas.11370; Georgia.3000'

# PROBLEM 1 (4 points)

us_cases =  'Michigan, 1358; Hawaii, 103; Washington, 2104; Texas, 11370; Georgia, 3000'

# PROBLEM 2 (4 points)

covid_cases = us_cases.split("; ")

print(covid_cases )

# PROBLEM 3 (4 points)

top_covid_cases = covid_cases.pop(1)

print(top_covid_cases)

# PROBLEM 4 (4 points)

highest_ranked = covid_cases[-2]

print(highest_ranked)

# PROBLEM 5 (4 points)

statement = f"For January 2021, this state had the highest amount of confirmed COVID-19 cases: {highest_ranked} cases."

print(statement)

# END LAB EXERCISE