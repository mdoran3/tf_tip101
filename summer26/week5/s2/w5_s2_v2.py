##################################
# Problem 1: Poker Two-Pair Hand #
##################################

'''
In poker, players are given a hand of five cards. A player has a 
"two-pair" hand if they have two cards of the same rank and another 
two cards of another rank. The fifth card isn’t used here.

Given the Card class below, write a function is_two_pair() that takes 
in a list player_hand that contains 5 Card objects.

The function returns True if the player has a two pair hand and False 
otherwise.

Cards in the hand are guaranteed to be unique and are guaranteed to 
have on the following suits and ranks:

The suit is one of the following values: 
"Hearts", "Spades", "Clubs", "Diamonds"

The rank is one of the following values: 
'2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace'
'''

### U - Understand
# 1. What does a "two-pair" hand look like vs. a hand that is NOT two-pair?
#    Two-pair: exactly 2 cards share one rank AND 2 other cards share another rank (e.g. two Aces + two 4s + any 5th card).
#    NOT two-pair: only one pair (e.g. two 4s + Ace + 6 + 7), three-of-a-kind, four-of-a-kind, or no matching ranks at all.

# 2. What data from each Card object do we actually need to determine two-pair?
#    Only card.rank — the suit is irrelevant. We need to count how many ranks appear exactly twice.

### P - Plan
# 1. Create a dictionary `ranks` to track how many times each rank appears in the hand.
# 2. Initialize a `pairs` counter to 0.
# 3. Loop through each card in player_hand:
#    - If the rank is not in `ranks`, add it with count 1.
#    - If the rank is already in `ranks` with count 1, increment to 2 and increment `pairs`.
#    - If `pairs` reaches 2, we've found two pairs — return True immediately.
# 4. After the loop, return False (fewer than 2 pairs found).

# 3. Translate each sub-problem into pseudocode:
'''
ranks = empty dictionary
pairs = 0

for each card in player_hand:
    if card.rank not in ranks:
        ranks[card.rank] = 1
    else if ranks[card.rank] == 1:
        ranks[card.rank] = 2
        pairs += 1
    if pairs == 2:
        return True

return False
'''

### I - Implement
# 4. Translate the pseudocode into Python and share your final answer:
class Card():
	def  __init__(self, suit, rank):
		self.suit = suit
		self.rank = rank

def is_two_pair(player_hand):
	ranks = {}
	pairs = 0
	for card in player_hand:
		if card.rank not in ranks:
			ranks[card.rank] = 1
		elif card.rank in ranks and ranks[card.rank] == 1:
			ranks[card.rank] += 1
			pairs += 1
		if pairs == 2:
			return True
	return False
		

card_one = Card("Hearts", "Ace")
card_two = Card("Hearts", "4")
card_three = Card("Diamonds", "Ace")
card_four = Card("Diamonds", "4")
card_five = Card("Diamonds", "6")
card_six = Card("Diamonds", "7")

player_one_hand = [card_one, card_two, card_three, card_four, card_five]
print(is_two_pair(player_one_hand))

player_two_hand = [card_two, card_three, card_four, card_five, card_six]
print(is_two_pair(player_two_hand))

'''
Example Output:

True  # Two Aces + Two 4s (+ Unused 6)
False # Two 4s (+ Ace + 6 + 7)
'''


##################################
# Problem 2: Barbie Linked List  #
##################################

'''
A linked list is a new data type that, similar to a normal 
list or array, allows us to store pieces of data sequentially. 
The difference between a linked list and a normal list lies 
in how each element is stored in a computer’s memory.

In a normal list, individual elements of the list are stored 
in adjacent memory locations according to the order they appear 
in the list. If we know where the first element of the list is 
stored, it’s really easy to find any other element in the list.

In a linked list, the individual elements called nodes are not 
stored in sequential memory locations. Each node may be stored 
in an unrelated memory location. To connect nodes together into 
a sequential list, each node stores a reference or pointer to 
the next node in the list.

Using the provided Node class below, recreate the list 
['Barbie', 'President Barbie', 'Weird Barbie', 'Ken'] as a 
linked list.
'''

### U - Understand
# 1. What does each Node store, and how do nodes connect to each other?
#    Each Node holds a `value` (the data) and a `next` pointer to the next Node in the sequence.
#    The last node's `next` is None, marking the end of the list.

# 2. What is the order we need, and how do we link them together?
#    We need: Barbie -> President Barbie -> Weird Barbie -> Ken
#    We create each node separately, then set node_1.next = node_2, node_2.next = node_3, etc.


### P - Plan
# 1. Create node_1 with value "Barbie".
# 2. Create node_2 with value "President Barbie", then set node_1.next = node_2.
# 3. Create node_3 with value "Weird Barbie", then set node_2.next = node_3.
# 4. Create node_4 with value "Ken", then set node_3.next = node_4.
#    node_4.next stays None (default) — it's the tail of the list.

# 3. Translate each sub-problem into pseudocode:
'''
node_1 = Node("Barbie")
node_2 = Node("President Barbie")
node_1.next = node_2

node_3 = Node("Weird Barbie")
node_2.next = node_3

node_4 = Node("Ken")
node_3.next = node_4

# node_4.next is None by default — end of list
'''

### I - Implement
# 4. Translate the pseudocode into Python and share your final answer:
class Node:
	def __init__(self, value, next=None):
		self.value = value
		self.next = next
		
node_1 = Node("Barbie")
node_2 = Node("President Barbie")
node_1.next = node_2
node_3 = Node("weird Barbie")
node_2.next = node_3
node_4 = Node("Ken")
node_3.next = node_4
		
print(node_1.value, "->", node_1.next.value)
print(node_2.value, "->", node_2.next.value)
print(node_3.value, "->", node_3.next.value)
print(node_4.value, "->", node_4.next)

'''
Example Output:

Barbie -> President Barbie
President Barbie -> Weird Barbie
Weird Barbie -> Ken
Ken -> None

Result Linked list: Barbie -> President Barbie -> Weird Barbie -> Ken
'''

#################################
# Problem 3: Insert Value First #
#################################

'''
Using the Node class, write a function add_first() that takes 
in the head of a linked list and a value object val as parameters.

The function should insert a new Node object with value val as 
the new head of the linked list and return the new node.

Note: The "head" of a linked list is the first element in the 
linked list. Equivalent to lst[0] of a normal list.
'''

### U - Understand
# 1. What should be returned — the new node itself, or the full updated list?
# 2. What should happen if the head is None (empty list) — does val become the only node?

### P - Plan
# 1. Create a new Node with value val
# 2. Set the new node's next pointer to the current head
# 3. Return the new node as the new head

# 3. Translate each sub-problem into pseudocode:
'''
new_node = Node(val)
new_node.next = head
return new_node
'''

### I - Implement
# 4. Translate the pseudocode into Python and share your final answer:
class Node:
	def __init__(self, value, next=None):
		self.value = value
		self.next = next
			
def add_first(head, val):
	if not head:
		node = Node(val)
		return node
	else:
		new_node = Node(val, head)
		return new_node

def print_ll(ll):
	lst_str = ""
	head = ll
	while head:
		lst_str = lst_str + head.value + " -> "
		head = head.next
	return lst_str

node1 = Node("A")
node2 = Node("B")
node1.next = node2
node3 = Node("C")
node2.next = node3

ll = add_first(node1, "0")
print(print_ll(ll))

'''
Example Usage:

# Linked List: A -> B -> C
new_list = add_first(node_a, 0)
# New List: 0 -> A -> B -> C
'''