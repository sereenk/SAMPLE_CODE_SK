# START LAB EXERCISE 03
print('Lab Exercise 03 \n')

# PROBLEM 1 (5 Points)

inventors = {'Marie Van Brittan Brown':'Home security system',
'Alice H. Parker' : 'Furnace for central heating',
'Leonidas Berry': 'Gastroscope pioneer',
'Otis Boykin' : 'Artificial heart pacemaker control unit',
'David Crosthwait' : 'Heating'}

print(inventors)

# PROBLEM 2 (4 Points)
#SETUP
invention = 'Heating, ventilation, and air conditioning'

inventors['David Crosthwait'] = invention

print(inventors)

#END SETUP


# PROBLEM 3 (4 Points)
# SETUP
new_inventor = {'Alexander Miles': 'Automatic electric elevator doors'}

inventors ['Alexander Miles'] = 'Automatic electric elevator doors'

print(inventors)

# END SETUP


# PROBLEM 4 (4 Points)

inventors.pop('Marie Van Brittan Brown')

print(inventors)


# PROBLEM 5 (4 Points)
# SETUP
gastroscope_inventor = 'Leonidas Berry'

tuple_gastroscope_inventor = gastroscope_inventor,

print(tuple_gastroscope_inventor)
# END SETUP

# PROBLEM 6 (4 Points)
medical_inventors = tuple_gastroscope_inventor + ('Otis Boykin',)

print(medical_inventors)

# END LAB EXERCISE
