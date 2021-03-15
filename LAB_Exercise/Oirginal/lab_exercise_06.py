# START LAB EXERCISE 06
print('Lab Exercise 06 \n')

# [IMPORTANT NOTE]
# This Lab Exercise briefly covers the topics you have learned in the past few weeks and tries to make you familiar
# with different types of questions you might encounter in the midterm exam
# More detailed review questions are in this week's Problem Set


# PROBLEM 1A (5 Points)
# Multiple-Choice Question
# Read the instruction and all the given answers carefully
# Assign your answer (i.e., "AB") to the variable "answer1A"

# You might use the following concepts and operations to solve this this problem
# 1) built-in functions (i.e., type(), len())
# 2) list indexes and list element

'''
Which of the following boolean expressions will be evaluated as False?
Given letters = ['a','b','c','d']

A type(letters) == list
B len(letters[-2:]) == 2
C "".join(letters) == 'a b c d'
D letters[-2] == 'c'

'''

# BEGIN PROBLEM 1A SOLUTION
answer1A = None
# END PROBLEM 1A SOLUTION


# PROBLEM 1B (5 Points)
# Multiple-Choice Question
# Read the instruction and all the given answers carefully
# Assign your answer (i.e., "ABC") to the variable "answer1B"

# You might use the following concepts and operations to solve this this problem
# 1) loops
# 2) conditional statement
# 3) built-in functions (i.e., split())
# 4) string indexes and list indexes

'''
Which of the following code snippets contain syntax errors?
A. print(len(var.split(“,”)[1])
B. print(var[1][2].split())
C. For x In var:
       print(x)
D. if len(var) <= 5
        print(var)

'''

# BEGIN PROBLEM 1B SOLUTION
answer1B = None
# END PROBLEM 1B SOLUTION


# PROBLEM 2 (10 Points)
# Coding Question
# Read the instruction carefully and write code to solve this question

# You might use the following concepts and operations to solve this this problem
# 1) loops
# 2) conditional statement
# 3) list operations

'''
Write a function named char_not_in_string(string)
char_not_in_string(string) takes one arguments: <string>, a string
char_not_in_string(string) should return True if char "a" is not in <string> and False if char "a" is in <string>

Loop over str_list, apply the function char_not_in_string, write the string into 
the list answer2 if char_not_in_string returns True

Sample case
str_list = ["aaa", "bb", "cccc", "d"]

Expected answer
answer2 = ["bb", "cccc", "d"]

Explanation
string  return value of "char_not_in_string"
"aaa"   False
"bb"    True
"cccc"  True
"d"     True

So if we loop over str_list, answer2 should be ["bb", "cccc", "d"]
Note that ["bb", "d", "cccc"] is not correct. Since we loop over str_list, the order of element 
in the list should not change.
'''


# BEGIN PROBLEM 2 SOLUTION
def char_not_in_string(string):
    pass


str_list = ["aaaa", "sse", "kgeakkk", "qweww", "", "l", "asdew"]
answer2 = []

# END PROBLEM 2 SOLUTION


# PROBLEM 3 (5 Points)
# Coding Question - Fix Bugs

# Bugs are mistakes in the code that will create erroneous behaviors or produce unexpected results.
# For instance, the syntax might be incorrect, and the Python environment will complain.
# Another example will be trying to get the last item in the list while using 0 as the index to access the list items

# Read the instruction and given code snippet carefully
# There are TWO bugs in the code snippet.
# Please identify and fix them to make the function run correctly
# You need to directly change the original code in the function answer3(numbers)

# You might use the following concepts and operations to solve this this problem
# 1) built-in functions (i.e., range(), len())
# 2) list indexes and list element
# 3) operator (i.e., +)

'''
# The function answer3(numbers) takes one argument: <numbers>, a list of integers
# "answer3" should return the sum of the integers in <numbers>.
# You are required to use a for loop and arithmetic operators, as provided, to perform the addition, 
# without using built-in functions (e.g., sum()).

Sample input
<numbers> = [1,2,3]

Sample output
6

Explanation
1+2+3 = 6
'''

# BEGIN PROBLEM 3 SOLUTION
def answer3(numbers):
    s = 0
    for i in range(len(numbers)-1):
        s = s + i
    return s


# You can use "numbers_test1", "numbers_test2" to test your function
# Note: passing these two tests doesn't guarantee your function is correct.
# We will use other test cases to verify the correctness of your implementation
numbers_test1 = [1,2,8]
numbers_test2 = [4,3,1,5,6]


# END PROBLEM 3 SOLUTION

# END LAB EXERCISE
