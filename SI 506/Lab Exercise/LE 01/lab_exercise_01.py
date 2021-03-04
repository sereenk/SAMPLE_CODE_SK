# START LAB EXERCISE 01
print('Lab Exercise 01 \n')

# PROBLEM 1 (3 points)

si = "School of Information"
#pub&policy = "Gerald R. Ford School of Public Policy"
#public health = "School of Public Health"
um_coe = "College of Engineering"
#r-bus = "Ross School of Business"
lsa = "College of Literature, Science & the Arts"


# PROBLEM 2 (2 points)
valid_var = ["si", "um_coe", "lsa"]

print(f"\nThe valid variables are: {valid_var}")


# PROBLEM 3 (3 points)
valid_var_length = len(valid_var)

print(f"\nThe length of the valid variable list is {valid_var_length}")

# PROBLEM 4 (3 points)
data_type = type(valid_var)

print(f"\nThe data type of the valid_var is {data_type}")

# PROBLEM 5 (3 points points)
si_students = 1199
coe_students = 9682
lsa_students = 16504

total_students = si_students + coe_students + lsa_students

print(f"\nThe total number of students in SI, COE, & LSA is {total_students}")

# PROBLEM 6 (3 points)
avg_stu_size = (total_students//3)

print(f"\nThe average number of students per school/college is {avg_stu_size}")

# PROBLEM 7 (3 points)
school_abbr_str = "SI, SPH, BUS, LSA, COE, PUBPOL"

school_abbr_list = school_abbr_str.split()

print(f"""\nThe data type of school_abbr_str is {type(school_abbr_str)}.
\nThe data type of school_abbr_list is {type(school_abbr_list)}.""")


# END LAB EXERCISE