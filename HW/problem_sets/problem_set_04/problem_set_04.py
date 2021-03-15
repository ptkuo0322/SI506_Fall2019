# SI 506 2019F - Problem Set 04


# PROBLEM 1:
#
# - Supplemental (Please Read!) -
#
# For this problem, we will be working with the "planets.txt" file.
#
# The first line of the file contains the headings for each column of data. As such, the
# first line is referred to as the "header line". Each line after the header line contains
# another "row" of data, where the data is separated by commas in the same order as the headers.
#
# For example, if the header line reads "Name,Color,Shape", and the
# next line reads "Apple,Red,Sphere", then "Apple" is the Name, "Red" is the Color, and "Sphere" is
# the Shape.
#
# One last thing: In this problem set, we ask you to build functions. The line that defines the
# function is given for you as a courtesy, and so are print statements that call the function.
# However, please be aware that the argument lists for both the function definitions and print
# statements have been redacted. You may need to edit both the function definition lines and the
# print statements by adding arguments for them to work properly.
#
# - End Supplemental -
#
# Write a function named 'num_chars_in_file' that takes a file name (a string) as the only argument.
# num_chars_in_file should open the file and return the number of characters within that file, *including*
# the header line. Then, use that function to print out the number of characters in "planets.txt"
#
# HINT: You will need to use the <open file object>.read() function.

# BEGIN PROBLEM 1 SOLUTION

def num_chars_in_file():
    pass

print(f"\nProblem 1: {num_chars_in_file()}")

# END PROBLEM 1 SOLUTION


# PROBLEM 2:
#
# Write a function named 'num_lines_in_file' that takes a file name (a string) as the only argument.
# num_lines_in_file should open the file and return the number of lines within that file.
# Then, use that function to print out the number of lines in "planets.txt", *including* the
# header line.

# BEGIN PROBLEM 2 SOLUTION

def num_lines_in_file():
    pass

print(f"\nProblem 2: {num_lines_in_file()}")

# END PROBLEM 2 SOLUTION


# PROBLEM 3:
#
# Now, write a function called create_nested_list with one argument, a file name with a default value of
# 'planets.txt'. In the function, record the data from each line as a list (i.e. split each line to just
# contain the data, not the commas).
#
# *Skip the first (header) line* but append the list of data from each other line in order to a new list,
# called whatever you like.
# Have your function return the completed nested list and save it as 'planet_data'.
#
# HINT: the returned list should look like this:
#
# [['Mercury', 'Rocky', '0', '2440', '57.9', 'Mercury is smaller than the largest natural satellites in
#   the solar system\n'], ['Venus', 'Rocky', '0', '6052', '107.2', 'Venus has a surface atmospheric pressure
#   more than 90 times greater than Earth\n'],...]

# BEGIN PROBLEM 3 SOLUTION

def create_nested_list():
    pass

planet_data = None

print(f"\nProblem 3:\n {planet_data}")

# END PROBLEM 3 SOLUTION


# PROBLEM 4
#
# Write a function named "middle_planets" that takes a nested list as the only argument (name
# the argument whatever you like!), with a default value of the variable planet_data.
# Within the function, loop through each planet and append the names
# of the planets that are between 200 million km from the sun and 1500 million km from the sun to a
# list (name this list whatever you like within the function!). Return that list.
#
# The format of the returned object should be : [<planet1>,<planet2>,<planet3,...etc] for however many
# planets fit the conditional criteria.
#
# NOTE: You may need to use the float() function to convert string representations of numbers to
# float representations of numbers -- float representation is how Python recognizes numbers with
# decimals, and you can only compare numbers in conditional statements to integers or floats.
# If you are unsure how to use float(), read the following page:
# https://www.programiz.com/python-programming/methods/built-in/float

# BEGIN PROBLEM 4 SOLUTION

def middle_planets():
    pass

print(f"\nProblem 4: {middle_planets()}")

# END PROBLEM 4 SOLUTION


# PROBLEM 5
#
# Write a function called "string_from_list" that takes as an argument any list of strings,
# (regardless of length) and join them together with a single comma ','. Then, add a new line
# character at the end of the string (represented by "\n", although the \n is usually invisible
# and only appears as a new line when printed to the terminal or written to a file)
#
# For example, string_from_list(['cat', 'dog', 'mouse']) should return "cat,dog,mouse\n"
#
# Print the output of string_from_list(planet_data[0]) (which is the mercury line) to be sure it
# works.

# BEGIN PROBLEM 5 SOLUTION

def string_from_list():
    pass


print(f"\nProblem 5: {string_from_list()}")

# END PROBLEM 5 SOLUTION


# PROBLEM 6
#
# Open a new file for writing, called "new_planets.txt". Then, loop through each line in "planets.txt".
# For each of the planets, write their names, type, and number of natural satellites to
# inner_planets.txt, separated by commas. Remember to skip the header line!
#
# Add a new line character ("\n") to the end of each line that you write to "new_planets.txt".
#
# In other words, each line written to "new_planets.txt" should look like the following:
#
# "<Name>,<Type>,<Number of Known Natural Satellites>\n"
#
# HINT: Remember to skip the header line in planets.txt!
# ANOTHER HINT: Use your function from problem 5 to create the string that you will write
# for each planet, if you first create a list of the necessary info from each planet and
# pass it to the function 'string_from_list'

# BEGIN PROBLEM 6 SOLUTION

fin = open("planets.txt",'r')
fout = open("new_planets.txt",'w')


# END PROBLEM 6 SOLUTION

# END PROBLEM SET
# SI 506 2019F - Problem Set 04
