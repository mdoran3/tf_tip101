############################
# Problem 5: Calculate Tip #
############################

# Write a function calculate_tip() that takes in a float bill and a string service_quality as parameters.
# If service_quality is "poor", the function should return 10% of the bill value.
# If service_quality is "average", the function should return 15% of the bill value.
# If service_quality is "excellent", the function should return 20% of the bill value.
# If service_quality is any other value, the function should return None.

### U - Understand 
# 1. Share 2 questions you would ask to help understand the question:
#   How many conditinal branches are in this problem?
#   Instead of simply printing statements in each branch, what are we doing instead?

### P - Plan
# 2. Write out in plain English what you want to do: 
#   if service is poor, return the bill * 0.10
#   if service is average, return the bill * 0.15
#   if service is excellent, return the bill * 0.20
#   else, just return None

# 3. Translate each sub-problem into pseudocode:
#   func(bill, service):
#       if service is poor: return bill * 0.10
#       if service is average: return bill * 0.15
#       if service is excellent: return bill * 0.20
#       if service is a different value : return None

### I - Implement
# 4. Translate the pseudocode into Python and share your final answer:
def calculate_tip(bill, service_quality):
    if service_quality == "poor":
        return bill * 0.10
    elif service_quality == "average":
        return bill * 0.15
    elif service_quality == "excellent":
        return bill * 0.20
    else:
        return None


tip1 = calculate_tip(44.53, "average")
print(tip1)
tip2 = calculate_tip(44.53, "poor")
print(tip2)
tip3 = calculate_tip(44.53, "excellent")
print(tip3)