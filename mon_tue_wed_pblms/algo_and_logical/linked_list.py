class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    def reverse(self):
        prev_node = None
        curr_node = self.head

        while curr_node is not None:
            next_node = curr_node.next
            curr_node.next = prev_node
            prev_node = curr_node
            curr_node = next_node

        self.head = prev_node


# Create a new linked list object
llist = LinkedList()
llist.head = ListNode(10)
llist.head.next = ListNode(20)
llist.head.next.next = ListNode(30)
llist.head.next.next.next = ListNode(40)

# Print the original list
print("Original list:")
curr_node = llist.head
while curr_node is not None:
    print(curr_node.val)
    curr_node = curr_node.next

# Reverse the linked list
llist.reverse()

# Print the reversed list
print("Reversed list:")
curr_node = llist.head
while curr_node is not None:
    print(curr_node.val)
    curr_node = curr_node.next
