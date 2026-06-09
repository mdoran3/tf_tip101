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