# Problem #1
# Given the head of a singly linked list,
#  reverse the list in-place and return the new head.
# Input: 1 → 3 → 5 → 7 → 9 # head = [1, 3, 5, 7, 9]
# Output: 9 → 7 → 5 → 3 → 1 # [9, 7, 5, 3, 1]
# Constraints: O(n) time, O(1) space.


class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


def reverse_linked_list(head):
    prev = None
    curr = head
    while curr:
        next_node = curr.next
        curr.next = prev
        prev = curr
        curr = next_node
    return prev


def to_list(head):
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result


def build_list(vals):
    if not vals:
        return None
    head = Node(vals[0])
    curr = head
    for v in vals[1:]:
        curr.next = Node(v)
        curr = curr.next
    return head


if __name__ == "__main__":
    head = build_list([1, 3, 5, 7, 9])
    new_head = reverse_linked_list(head)
    print(to_list(new_head))  # [9, 7, 5, 3, 1]
