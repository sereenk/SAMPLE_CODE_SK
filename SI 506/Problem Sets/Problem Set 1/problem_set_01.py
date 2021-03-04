# START PROBLEM SET 01
print('Problem Set 01')

# PROBLEM 1 (20 points)
print('\nProblem 1')

# inaugural poet = 'Amanda Gorman'
# inaugural_poet = Amanda Gorman
inaugural_poet = 'Amanda Gorman'
undergraduate_school = 'Harvard University'
# 'Harvard University' = undergraduate_school

valid_variables = [inaugural_poet,undergraduate_school]

print(f"\nValid = {valid_variables}")

# PROBLEM 2 (20 points)


print('\nProblem 2')

# PROBLEM 2 SETUP
# Please do not change.

name = 'Amanda Gorman'
age = 22
work_collection = ['Change Sings', 'The Hill We Climb And Other Poems']
inaugural_poem = """
When day comes we ask ourselves, where can we find light in this never-ending shade?
The loss we carry, a sea we must wade.
We’ve braved the belly of the beast, we’ve learned that quiet isn’t always peace and the norms and notions of what just is, isn’t always justice.
And yet the dawn is ours before we knew it, somehow we do it, somehow we’ve weathered and witnessed a nation that isn’t broken but simply unfinished.
We, the successors of a country and a time where a skinny black girl descended from slaves and raised by a single mother can dream of becoming president only to find herself reciting for one.
And, yes, we are far from polished, far from pristine, but that doesn’t mean we are striving to form a union that is perfect, we are striving to forge a union with purpose, to compose a country committed to all cultures, colors, characters and conditions of man.
So we lift our gazes not to what stands between us, but what stands before us.
We close the divide because we know to put our future first, we must first put our differences aside.
We lay down our arms so we can reach out our arms to one another, we seek harm to none and harmony for all.
Let the globe, if nothing else, say this is true: that even as we grieved, we grew, even as we hurt, we hoped, that even as we tired, we tried, that we’ll forever be tied together victorious, not because we will never again know defeat but because we will never again sow division.
"""
# END PROBLEM 2 SETUP

name_type  =  type(name)
age_type = type(age)
collection_type = type(work_collection)

print(name_type)
print(age_type)
print(collection_type)


# PROBLEM  3 (20 points)
print('\nProblem 3')

# split multi-line string into a list

num_words =  len(inaugural_poem.split())

# to calculate the average number of words per line

avg_words = num_words / 10

print(f"\nNumber of words = {num_words}")
print(f"\nAverage number of words per line = {avg_words}")


# PROBLEM 4 (20 points)
print('\nProblem 4')
next_line = "Scripture tells us to envision that everyone shall sit under their own vine and fig tree and no one should make them afraid."
num_words_next = len(next_line.split())

total_words = num_words_next + num_words


print(f"\nNew total number of words in inaugural_poem and next_line = {total_words}")

# PROBLEM 5 (20 points)
print('\nProblem 5')

num_chars_poem = len(inaugural_poem)

print(f"\nNumber of characters = {num_chars_poem}")

avg_chars = num_chars_poem // num_words

print(f"\nAverage number of characters per word = {avg_chars}")