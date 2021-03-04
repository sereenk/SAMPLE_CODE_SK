# SI 506 Lecture 03

# 1.0 COMMENTS

# A single line comment <-- commences with hash (#) character

"""
This is a block comment comprising a multi-line string. This is actually a string
constant that is denoted by the use of triple quotation marks.
"""


# 2.0 VALUES (OBJECTS) AND TYPES

# 2.1 NUMBERS: integer, float (decimal)

506

.25

# 2.2 SEQUENCES (ORDERED SET)

'Welcome to SI 506'

['arwhyte', 'bealsa', 'dsewhite', 'maxzhang', 'tkaress']

(506, 507, 618)


# 2.3 ASSOCIATIVE ARRAY (MAP): dictionary (key-value pairs)

{
    'course': 'SI 506',
    'instructor_count': 1,
    'gsi_count': 2,
    'ia_count': 2
}


# 2.4 BOOLEAN

True
False


# 2.5 NONE

None


# 3.0 VARIABLES

num = 506

welcome_message = 'Welcome to SI 506'

teaching_team = ['arwhyte', 'bealsa', 'dsewhite', 'maxzhang', 'tkaress']

chorus = """
Hail! to the victors valiant
Hail! to the conquering heroes
Hail! Hail! to Michigan
the leaders and best!
"""

# 4.0 VARIABLE NAMING RULES AND CONVENTIONS


# 4.1 Good

# Choose lowercase
uniqname = 'arwhyte'

# Separate words with underscore (_)
course_code = 'SI 506'

# Use plural form to indicate a set or sequence
course_codes = ['SI 506', 'SI 507', 'SI 618']

# Ok to use recognizable abbreviations like num[ber], val[ue] or var[iable].
num = 27

# "is_", "has_" Boolean true/false
is_enrolled = True
has_mask = True

# All caps designates a module level constant (special case)
BASE_URL = 'https://si506.org/'

# Function definition specifying two parameters x and y (a foreshadowing of the weeks ahead)
def multiply(x, y):
    return x * y # arithmetic

# Call the function and pass two numeric arguments
product = multiply(14, 27)

print(f"product = {product}") # formatted string literal (f-string)

# Built-in enumerate() function adds a counter < i > when looping over < course_codes >
for i, code in enumerate(course_codes, 1):
    print(f"{i}. {code}")


# 4.2 Bad (but legal)

# Opaque
c = 'SI 506'
cc = 'SI 506'

# Reserve CamelCase for class names.
CourseCode = 'SI 506'

# Unnecessarily verbose; difficult to read.
c_o_u_r_s_e_c_o_d_e = 'SI 506'

# Difficult to read; guaranteed to annoy.
cOUrsE_cOdE = 'SI 506'


# 4.3 Ugly (illegal)

# Illegal: keyword used as a variable name (language-specific identifiers reserved by Python)

# class = 'SI 506' # use clazz # TODO UNCOMMENT

# Illegal: variable name commences with a numeric value.

# 506_umsi = 'SI 506' # TODO UNCOMMENT

# Illegal: variable name commences with a special character (e.g., `@`, `%`, `$`, `&`, `!`)

# $number = 506 # TODO UNCOMMENT

# Illegal: variable name includes a dash (`-`).

# course-list = ['SI 506', 'SI 507', 'SI 618'] # TODO UNCOMMENT

# Illegal: variable name includes whitespace.

# course name = 'SI 506' # illegal; uncomment to test

# Avoid: built-in function names (a few examples) # TODO UNCOMMENT

# Shadowing; risk name clash with built-in functions
# id = 506
# str = 'Go Blue'
# min = 0
# max = 27
# len = 6 # See example TypeError below

# Alternative names
id_ = 506

str_ = 'Go Blue'
val = 'Go Blue'

min_ = 0
min_val = 0

max_ = 27
max_val = 27

len_ = 6
length = 6


# 5.0 BUILT-IN FUNCTIONS (print(), type(), len())

# 5.1 print(): print passed in object to the screen

# Passing a hard-coded string.
print('SI 506 rocks!')

# Passing a variable name which points to a string.
print(welcome_message)

# Passing a variable name which points to a multiline string.
print(chorus)


# 5.2 type(): determine object's data type

data_type = type(num)
print(data_type) # returns <class 'int'>

data_type = type(welcome_message)
print(data_type) # returns <class 'str'>

data_type = type(teaching_team)
print(data_type) # returns <class 'list'>


# 5.3 len(): check length of sequence (i.e., number of elements)

# TODO UNCOMMENT
# len = 10 # Shadowing built-in function name (avoid)
# Generates TypeError: 'int' object is not callable when len() is called below.

# Count characters in string (including whitespace).
chars_count = len(welcome_message)
print(chars_count)

# Count number of elements in list.
team_count = len(teaching_team)
print(team_count)


# 6.0. BASIC ARITHMETIC (addition, subtraction, multiplication, division)

# Counts
lecturer_count = 1
gsi_count = 2
ia_count = 2
lab_section_count = 8
student_count = 82

# Addition (+ operator)
teaching_team_count = lecturer_count + gsi_count + ia_count
print(f"teaching_team_count = {teaching_team_count}")

# Subtraction (- operator)
instructor_count = teaching_team_count - ia_count
print(f"instructor_count = {instructor_count}")

# Multiplication (* operator)
max_enrollment = lab_section_count * 25
print(f"max_enrollment = {max_enrollment}")

# Floating point division (/ operator)
avg_lab_size = student_count / lab_section_count
print(f"average lab size = {avg_lab_size}")

# Floor division a.k.a integer division (//)
avg_lab_size = student_count // lab_section_count
print(f"average lab size = {avg_lab_size}")
