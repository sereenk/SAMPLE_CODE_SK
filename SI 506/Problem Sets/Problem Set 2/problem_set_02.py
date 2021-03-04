#Problem Set 02
print('Problem Set 02')

# Problem 01 (20 points)
print('\nProblem 1')

cases = [70, 75, 126, 144, 170]

cases_latest = cases[-1]

cases[0]= 67

cases.append(267)


# Problem 02 (20 points)
print('\nProblem 2')

tests = [2143, 4486, 6765, 16501, 20685]

tests_last_three = tests[2:]
print(tests_last_three)

tests_reverse = tests[::-1]
print(tests_reverse)


# Problem 03 (20 points)
print('\nProblem 3')

vaccines = " 39,896-41,826-44,154-46,458-48,634-50,090   "
vaccines = vaccines.strip()
vaccines_list = vaccines.split("-")

print(vaccines_list)
# Problem 04 (20 points)
print('\nProblem 4')

dates = ["January 31st", "January 30th", "January 29th", "January 28th", "January 27th", "January 26th"]

dates_str = '|'.join(dates[::-1])
print(dates_str)

# Problem 05 (20 points)
print('\nProblem 5')

vaccines_26th = f"As of {dates[5]}, UM has administered {vaccines_list[0]} vaccines."
print(vaccines_26th)

vaccines_31st = f"As of {dates[0]}, UM has administered {vaccines_list[5]} vaccines."
print(vaccines_31st)

