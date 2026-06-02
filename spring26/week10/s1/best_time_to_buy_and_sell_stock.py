###############################################
# PROBLEM 2: BEST TIME TO BUTY AND SELL STOCK #
###############################################

# You are given a list of integers prices where prices[i] 
# is the price of a given stock on the ith day.

# You want to maximize your profit by choosing a single 
# day to buy one stock and choosing a different day in the 
# future to sell that stock.

# Return the maximum profit you can achieve from this 
# transaction. If you cannot achieve any profit, return 0.

### U - Understand 
# 1. Share 2 questions you would ask to help understand the question:
    # How should we iterate through prices? For loop? While loop? 
    # How mamy pointers should we use?

### P - Plan
# 2. Write out in plain English what you want to do: 
    # Initialize some variables like:
        # an initial buy price at the 0th index of prices
        # an initial sell price at the last index of prices
        # front pointer to 0
        # back pointer to the length of prices - 1
        # initial profit to sell - buy ( which is the highest prices minus the largest price)
    # Use a while loop while the two pointers do not cross
    # Check profit for if you increment front pointer and check profit for if the back pointer decremented
    # which ever one is greater, update the profit by comparing that result to the current profit
    # increment the front or decrement the back accordingly
    # return profit if above 0, else just return 0

# 3. Translate each sub-problem into pseudocode:
    # buy = prices[0]
    # sell = prices[last index]
    # front = 0
    # back = last index
    # profit = sell - buy
    # while front < back
        # forward_profit = prices[back] - prices[front + 1]
        # backward_profit = prices[back - 1] - prices[front]
        # if forward_profit > backward_profit
            # profit = max(profit, forward_profit)
            # increment front
        # else
            # profit = max(profit, backward_profit)
            # decrement back
    # if profit > 0
        # return profit
    # return 0


### I - Implement
# 4. Translate the pseudocode into Python and share your final answer:
def max_profit(prices):
    buy = prices[0]
    sell = prices[len(prices)-1]
    front = 0
    back = len(prices) - 1
    profit = sell - buy
    while front < back:
        forward = prices[back] - prices[front+1]
        backward = prices[back-1] - prices[front]
        if forward > backward:
            profit = max(profit, forward)
            front += 1
        else:
            profit = max(profit, backward)
            back -= 1
    if profit > 0:
        return profit
    return 0
    
# Example #1:
# Input: prices = [7,1,5,3,6,4]
# Expected Output: 5
# Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
# Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
prices = [7,1,5,3,6,4]
print(max_profit(prices))

# Example #2:
# Input: prices = [7,6,4,3,1]
# Expected Output: 0
# Explanation: In this case, no transactions are done and the max profit = 0.
prices1 = [7,6,4,3,1]
print(max_profit(prices1))