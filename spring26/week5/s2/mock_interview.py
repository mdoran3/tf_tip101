class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

def remove_duplicates(head):
    freq = {}
    prev = None
    curr = head
    while curr:
        if curr.val not in freq:
            freq[curr.val] = 1
            prev = curr
            curr = curr.next
        else:
            freq[curr.val] += 1
            prev.next = curr.next
            curr = curr.next
    return head


def print_ll(head):
    curr = head
    values = []
    while curr:
        values.append(str(curr.val))
        curr = curr.next
    print(" -> ".join(values))

head = Node(1, Node(1, Node(2, Node(3))))
print_ll(remove_duplicates(head))