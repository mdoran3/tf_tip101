#############################
# Problem 6: Calculate GPA  #
#############################

# Write a function calculate_gpa() that calculates the grade point 
# average (GPA) for a student based on their course grades and 
# returns the gpa as a float. The function takes in a dictionary 
# report_card as a parameter where each key-value pair represents 
# a course and the grade received in that course respectively. 
# The grades are represented as strings ("A", "B", "C", "D", "F") 
# and each grade corresponds to a certain number of grade points:

# "A" = 4
# "B" = 3
# "C" = 2
# "D" = 1
# "F" = 0

# A GPA is calculated by finding the average of all grade points.

### U - Understand 
# 1. Share 2 questions you would ask to help understand the question:
#   What dictionary could be created to help with solving the problem?
#   While conditioning logic could be used, is there a way to solve the 
    # problem with conditons?

### P - Plan
    # create a var for count - this is the amount of grades
    # create a var to accumlate the total grade points from report card
    # create a dictionary that holds letter grades and their numeric values
    # use a for loop and access the grade point value for each grade in the 
        # report card and add it to the total grade points
    # divide total grade points by the count to get gpa and return gpa

# 3. Translate each sub-problem into pseudocode:
    # func(report_card):
        # count, total_grade_points = 0
        # grade_points dict = {"A" : 4, etc}
        # for each grade, add its grade point to total_grade_points
        # divide total_grade_points by count and set equal to gpa
        # return gpa 

### I - Implement
# 4. Translate the pseudocode into Python and share your final answer:
def calculate_gpa(report_card):
    count = 0
    total_grade_points = 0
    grade_points = {"A" : 4, "B" : 3, "C" : 2, "D" : 1, "F" : 0}
    for grade in report_card:
        total_grade_points += grade_points[report_card[grade]]
        count += 1
    gpa = total_grade_points / count
    return gpa

report_card = {"Math": "A", "Science": "C", "History": "A", "Art": "B", "English": "B", "Spanish": "A"}
print(calculate_gpa(report_card))


########################
# Problem 7: Best Book #
########################

# Imagine you are working on a book review software like Goodreads. 
# Write a function named highest_rated() that returns the book with 
# the highest rating.

# The function should take in a list of dictionaries named books as 
# a parameter. Each dictionary represents data associated with a book, 
# including its title, author, and rating. The function should return 
# the dictionary for the book with the highest rating.

### U - Understand 
# 1. Share 2 questions you would ask to help understand the question:
#   When look for a mx value, what's a good amount to initialize the max var at?
#   How many loops are need and what kind?

### P - Plan
#   set a max var to negative infinity
#   set a best_book var to None
#   iterate through each book in the books dicitonary 
#   return the book with the best rating

# 3. Translate each sub-problem into pseudocode:
#   func(books):
#       highest_rated = -infinity
#       best_book = None
#       for each book
#           if book's rating > highes_rated
#               highest_rated = book's rating
#               best_book = book
#       return best_book

### I - Implement
# 4. Translate the pseudocode into Python and share your final answer:
def highest_rated(books):
    highest_rated = float('-inf')
    best_book = None
    for book in books:
        if book["rating"] > highest_rated:
            highest_rated = book["rating"]
            best_book = book
    return best_book

books = [
    {"title": "Tomorrow, and Tomorrow, and Tomorrow",
     "author": "Gabrielle Zevin",
     "rating": 4.18
    },
    {"title": "A Fortune For Your Disaster",
     "author": "Hanif Abdurraqib",
     "rating": 4.47
    },
    {"title": "The Seven Husbands of Evenlyn Hugo",
     "author": "Taylor Jenkins Reid",
     "rating": 4.40
    }
]

print(highest_rated(books))

# EXPECTED OUTPUT
# {"title": "A Fortune For Your Disaster",
#  "author": "Hanif Abdurraqib",
#  "rating": 4.47
# }

##############################
# Problem 8: Index-Value Map #
##############################

# Write a function index_to_value_map() that takes in a 
# list lst and returns a dictionary that maps the index 
# of each element in lst to its value.

### U - Understand 
# 1. Share 2 questions you would ask to help understand the question:
#   How does the enumerate feature work in Python?
#   How do I add the key and value to a function in Python?

### P - Plan
#   create an empty dict
#   iterate through list and enumerate
#   add key,value pair to empty dict
#   return dict

# 3. Translate each sub-problem into pseudocode:
#   func(lst):
#       enumerated_dict = {}
#       for index, item in enumerate(lst):
#           add key,value to enumerate_dict{}
#       return enumerated_dict

### I - Implement
# 4. Translate the pseudocode into Python and share your final answer:
def index_to_value_map(lst):
    fruits = {}
    for i, item in enumerate(lst):
        fruits[i] = item
    return fruits

# Example Input:
lst = ["apple", "banana", "cherry"]
print(index_to_value_map(lst))

# Example Output: {0: "apple", 1: "banana", 2: "cherry"}