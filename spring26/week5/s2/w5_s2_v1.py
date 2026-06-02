#############################
# PROBLEM 1: BATTLE POKEMON
#############################

#Given the Pokemon class below, copy the code and add it to your IDE.

# Then, write a method attack() that takes in a Pokemon object opponent and 
# decreases opponent's hp by their self's damage amount.

# If damaging the opponent leads to the opponent having an hp of 0 or less, 
# the function should set the opponent's hp to 0 and print out "<Opponent name> fainted>.

# Otherwise, the function should print out 
# "<Pokemon name> dealt <damage> damage to <opponent name>".

### U - Understand 
# 1. Share 2 questions you would ask to help understand the question:
    # In this ne function, how many objects are we dealing with?
    # How do we know how much to decrement the opponent's damage by?

### P - Plan
# 2. Write out in plain English what you want to do: 
    # Write a def called attack that takes in a self object and an opponent object
    # subtract self's damage from the opponents hit points (hp)
    # create and if/else statement
    # if the opponents hp is less than zero:
        # print the statement that they fainted
    # else:
        # print the other statement

# 3. Translate each sub-problem into pseudocode:
    # def attack(self, opponent):
        # opponent_hp -= self.damage
        # if opponent_hp < = 0
            # print(<Opponent name> fainted>
        # else:
            # print(<Pokemon name> dealt <damage> damage to <opponent name>)

### I - Implement
# 4. Translate the pseudocode into Python and share your final answer:
class Pokemon():
	def  __init__(self, name, hp, damage):
		self.name = name
		self.hp = hp # hit points
		self.damage = damage # The amount of damage this pokemon does to its opponent every attack
		
	def attack(self, opponent):
		opponent.hp -= self.damage
		if opponent.hp <= 0:
			print(f"{opponent.name} fainted")
		else:
		    print(f"{self.name} dealt {self.damage} damage to {opponent.name}")
	
pikachu = Pokemon("Pikachu", 35, 20)
bulbasaur = Pokemon("Bulbasaur", 45, 30) 

opponent = bulbasaur
pikachu.attack(opponent)

#####################################
# PROBLEM 2: Convert to Linked List
#####################################

# A linked list is a new data type that, similar to a normal list or array, 
# allows us to store pieces of data sequentially. The difference between a 
# linked list and a normal list lies in how each element is stored in a 
# computer’s memory.

# In a normal list, individual elements of the list are stored in adjacent 
# memory locations according to the order they appear in the list. If we 
# know where the first element of the list is stored, it’s really easy to 
# find any other element in the list.

# In a linked list, the individual elements called nodes are not stored in 
# sequential memory locations. Each node may be stored in an unrelated memory 
# location. To connect nodes together into a sequential list, each node stores 
# a reference or pointer to the next node in the list.

# Using the provided Node class below, create the normal Python list 
# ["Jigglypuff", "Wigglytuff"] as a linked list.

### U - Understand 
# 1. Share 2 questions you would ask to help understand the question:
    # How many objects are instantiated in this problem?
    # When creating a new object, what attributes must be specified?

### P - Plan
# 2. Write out in plain English what you want to do: 
    # create an object called node_1 and set it equal to Node with "Jigglypuff" as an attribute
    # create an object called node_2 and set it equal to Node with "Wigglytuff" as an attribute
    # set node_1's next attribute equal to node_2

# 3. Translate each sub-problem into pseudocode:
    # node_1 = Node(<name>)
    # node_2 = Node(<name)
    # node_1.next = node_2

### I - Implement
# 4. Translate the pseudocode into Python and share your final answer:
class Node:
	def __init__(self, value, next=None):
		self.value = value
		self.next = next
		
node_1 = Node("Jigglypuff")
node_2 = Node("Wigglytuff")
node_1.next = node_2
		
print(node_1.value, "->", node_1.next.value)
print(node_2.value, "->", node_2.next)

#######################
# PROBLEM 3: Add First
#######################

# Write a function add_first() that takes in a head of a 
# linked list and a new_node from the Node class as parameters.

# It should insert new_node as the new head of the linked_list. 
# The function returns new_node.

# Note: The "head" of a linked list is the first element in 
# the linked list. Equivalent to lst[0] of a normal list.

### U - Understand 
# 1. Share 2 questions you would ask to help understand the question:
    # How does inserting a node differ from adding to an array?
    # What is the head of a linked list?
    # Are linked list coniguous blocks in memory?

### P - Plan
# 2. Write out in plain English what you want to do: 
    # Take in head and new_node as parameters
    # set new_node's next value to head
    # now technically new_node will be head 
    # return new_node

# 3. Translate each sub-problem into pseudocode:
    # new_node.next = head
    # return new_node

### I - Implement
# 4. Translate the pseudocode into Python and share your final answer:
class Node:
	def __init__(self, value, next=None):
		self.value = value
		self.next = next
		
		
def add_first(head, new_node):
	new_node.next = head
	return new_node

# Using the Linked List from Problem 2
node_1 = Node("Jigglypuff")
node_2 = Node("Wigglytuff")
node_1.next = node_2

print(node_1.value, "->", node_1.next.value)

new_node = Node("Ditto")
node_1 = add_first(node_1, new_node)

print(node_1.value, "->", node_1.next.value)

######################
# PROBLEM 4: GET TAIL
######################

# Write a function get_tail() that takes in the head of a 
# linked list as a parameter.

# Return the value of the tail. If the list is empty, 
# return None.

# Note: The "tail" of a list is the last element in the 
# linked list. Equivalent to lst[-1] in a normal list.

### U - Understand 
# 1. Share 2 questions you would ask to help understand the question:
    # What kind of loop is best to iterate through nodes in a linked list?
    # How do we return a specific attribute of a node

### P - Plan
# 2. Write out in plain English what you want to do: 
    # set a variable current = head
    # create a while loop that keeps iterating while current.next is equal to True
    # in while loop, set current equal to current's next node
    # outside the while loop (when there is no more next node), return the current node's value

# 3. Translate each sub-problem into pseudocode:
    # def get_tail(head):
        # current = head
        # while current has next node:
            # current = the next node
        # return current.value

### I - Implement
# 4. Translate the pseudocode into Python and share your final answer:
class Node:
	def __init__(self, value, next=None):
		self.value = value
		self.next = next

def get_tail(head):
	current = head
	while current.next:
		current = current.next
	return current.value

# Build: num1 -> num2 -> num3
num1 = Node("num1")
num2 = Node("num2")
num3 = Node("num3")
num1.next = num2
num2.next = num3

head = num1
tail = get_tail(head)   # or get_tail(num1)
print(tail)             # expected: num3

##########################
# PROBLEM 5: REPLACE NODE
##########################

# Using the Node class, write a function ll_replace() that 
# updates in place every node whose value == original to 
# have value = replacement. The function returns None.

### U - Understand 
# 1. Share 2 questions you would ask to help understand the question:
    # What is the space complexity of this kind of algorithm? 
    # What is the time complexity?
    # What is the to_string function?

### P - Plan
# 2. Write out in plain English what you want to do: 
    # Iterate through the linked list with a while loop
    # if the current node's value is equal to the original, update the value to replacement

# 3. Translate each sub-problem into pseudocode:
    # current = head
    # while current:
        # if current.value is equal to original paramater
            # current.value equals replacement parameter
        # current = current.next

### I - Implement
# 4. Translate the pseudocode into Python and share your final answer:
class Node:
	def __init__(self, value, next=None):
		self.value = value
		self.next = next
		
def ll_replace(head, original, replacement):
	current = head
	while current:
		if current.value == original:
			current.value = replacement
		current = current.next
 
def to_string(head): # to test your list
    parts, cur = [], head
    while cur:
        parts.append(str(cur.value))
        cur = cur.next
    return " -> ".join(parts) if parts else "EMPTY"

num3 = Node(5)
num2 = Node(6, num3)
num1 = Node(5, num2)
# initial linked list: 5 -> 6 -> 5

head = num1
ll_replace(head, 5, "banana")
# updated linked list: "banana" -> 6 -> "banana"
print(to_string(head))