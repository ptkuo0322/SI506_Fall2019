import pathlib

# This lab exercise is designed to confirm that you have installed both Python 3 and a text editor
# or IDE on your machine.

# We recommend installing Python 3.8.0 and VS Code (https://code.visualstudio.com/).


# Start set up
op_systems = ['macOS', 'Linix-flavored distro', 'Windows 10', 'Other']
tools = ['VS Code', 'Atom', 'IDLE', 'PyCharm', 'PyDev (Eclipse)', 'Sublime Text', 'Thonny', 'Vim', 'Wing', 'Other']
# End set up


# INSTRUCTIONS: do the following:
# 1) install Python 3.7 or 3.8 if not already installed.
# 2) install a source-code editor or IDE if not already installed.
# 3) update the assignment statements below with your details.
# 4) run the updated lab_exercise_07.py file from your source-code editor or IDE.
# 5) take a screenshot of the source-code editor or IDE and its output
# 6) upload the screenshot to the Canvas Lab Exercise 07 page.

# Do all of the above and you will earn 50 bonus points (that's right, double bonus points)
# if submitted on or before the due date. Late penalties apply thereafter.

# Points will be deducted if any of the requested information is missing.

# Below are listed a number of variables:
# full_name
# uniqname
# op_sys (operating system)
# py_version (Python version)
# tool (source-code editor or IDE installed)

# Assign your details (replace values or indexes as appropriate)
full_name = None # FIX ME your full name
uniqname = None # FIX ME your uniqname
op_sys = op_systems[None] # FIX ME your OS by list index position
py_version = '3.8.0' # FIX ME your version
tool = tools[None] # FIX ME your tool by list index position

# Below are listed a second set of variables
# path
# home_directory
# current_working_directory
# file_name
# file_name_extension
# file_path_absolute

# Use pathlib.Path(<arg>) to return a path object.
# Pass name of this file as the argument <arg> and assign path object to path variable.
# Then use the path object methods to assign the appropriate value to each variable.
path = pathlib.Path('') # FIX ME (add file name)
home_directory = None # FIX ME use path to return the home directory
current_working_directory = None # FIX ME use path to return the current working directory
file_name = None # FIX ME use path to return the file name
file_name_extension = None # FIX ME use path to return the file name extension (e.g., '.py')
file_path_absolute = None # FIX ME use path to print out this file's absolute path

# Print each value on its own line by specifying a separator
print(
    f"Name = {full_name}",
    f"uniqname = {uniqname}",
    f"Operating system = {op_sys}",
    f"Python version installed = {py_version}",
    f"Tool installed = {tool}",
    f"Home directory = {home_directory}",
    f"Current working directory = {current_working_directory}",
    f"File name = {file_name}",
    f"File name extension = {file_name_extension}",
    f"Absolute file path = {file_path_absolute}",
    sep='\n'
)