# SI 506 2019F - Problem Set 02

# SETUP - Define list of UNESCO heritage sites in China, 1987-1992. In the future, such data
# will be provided in a file which you will read into python with some useful functions. However,
# for today, the teaching team has provided this list for you to use.
#
# Data description:
#
# Each item in the china_unesco_sites list is a string containing the country of the site,
# name of the site, type of the site (Natural, Cultural, or Mixed - for both natural and cultural),
# and the year that the site was formally registered by UNESCO. Each of these pieces of information
# are separated by commas. Data stored this way are referred to as "comma-delimited" or, more simply,
# "comma-separated." If you have ever heard of a .csv file: csv means "comma-separated values," and
# data in .csv files are stored in a manner very similar to the below list.

china_unesco_sites = ['China,Huanglong Scenic and Historic Interest Area,Natural,1992',
 'China,Jiuzhaigou Valley Scenic and Historic Interest Area,Natural,1992',
 'China,Wulingyuan Scenic and Historic Interest Area,Natural,1992',
 'China,Mount Huangshan,Mixed,1990',
 'China,Imperial Palaces of the Ming and Qing Dynasties in Beijing and Shenyang,Cultural,1987',
 'China,Mausoleum of the First Qin Emperor,Cultural,1987',
 'China,Mogao Caves,Cultural,1987',
 'China,Mount Taishan,Mixed,1987',
 'China,Peking Man Site at Zhoukoudian,Cultural,1987',
 'China,The Great Wall,Cultural,1987']

# END SETUP


# PROBLEM 1
# Use list slicing to assign the last item of the china_unesco_sites list to the
# variable "great_wall" (replace the placeholder None)

# BEGIN PROBLEM 1 SOLUTION

great_wall = None

# END PROBLEM 1 SOLUTION


# PROBLEM 2
# Now, turn the string saved in great_wall into a list, "great_wall_list". To do so,
# use a python standard library string function to separate the string wherever there
# are commas.

# BEGIN PROBLEM 2 SOLUTION

great_wall_list = None

# END PROBLEM 2 SOLUTION


# PROBLEM 3
# Loop through each item in the great_wall_list. Append the number of characters of
# each item to the great_wall_item_length list (provided here as an empty list to start).

# BEGIN PROBLEM 3 SOLUTION

great_wall_item_length = []

# END PROBLEM 3 SOLUTION


# PROBLEM 4
# Use list slicing and string functions to save only the country and heritage site name for
# the great_wall to a new string, in the following format (pay attention to spaces!):
#
# "<heritage site name> is in <country>" (the <> names are placeholders that your code should replace)
#
# Save this string to the variable "great_wall_string"

# BEGIN PROBLEM 4 SOLUTION

great_wall_string = None

# END PROBLEM 4 SOLUTION


# PROBLEM 5
# Use list slicing to create a new list ("new_list") that comprises of the last 5 entries in the
# china_unesco_sites list.

# BEGIN PROBLEM 5 SOLUTION

new_list = None

# END PROBLEM 5 SOLUTION


# PROBLEM 6
# Finally, put all you've learned together.
#
# Loop over all of china_unesco_sites, and using lists and string functions,
# produce a new list named "unesco_sites". For each item in china_unesco_sites,
# if the item is a Cultural site, append the information about that item to
# unesco_sites with the following format:

#
# "<country> - <heritage site name> - <year>" (NOTE the spaces before and after each hyphen!)

# BEGIN PROBLEM 6 SOLUTION


# END PROBLEM 6 SOLUTION

# END PROBLEM SET
