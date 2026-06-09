##############################
# Problem 6: Calculate GPA   #
##############################

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