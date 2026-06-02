class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def merge_lists(list1, list2):
    temp = ListNode()
    cur = temp
    while list1 and list2:
        if list1.val <= list2.val:
            cur.next = list1
            list1 = list1.next
        else:
            cur.next = list2
            list2 = list2.next
        cur = cur.next
    cur.next = list1 or list2
    return temp.next


def make_list(values):
    dummy = ListNode()
    cur = dummy
    for v in values:
        cur.next = ListNode(v)
        cur = cur.next
    return dummy.next


def to_list(node):
    result = []
    while node:
        result.append(node.val)
        node = node.next
    return result

# Test 1: interleaved merge
l1 = make_list([1, 2, 3, 5])
l2 = make_list([4, 6, 7])
print(to_list(merge_lists(l1, l2)))  # [1, 2, 3, 4, 5, 6, 7]

# Test 2: one empty list
l3 = make_list([])
l4 = make_list([1, 2, 3])
print(to_list(merge_lists(l3, l4)))  # [1, 2, 3]