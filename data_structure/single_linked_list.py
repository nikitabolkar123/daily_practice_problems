class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None  # next means reference of next node so for creating node we separate node  and give none


class SingleLinkedList:
    def __init__(self):
        self.head = None  # head stored reference of first node #empty linked list

    # traversal operations
    def display(self):
        if self.head is None:
            print("Linked list is empty")
        else:
            node = self.head  # node is for reference of head
            while node:  # node not none
                print(node.data, "--> ", end='')
                node = node.next  # for next node
            print('\n')

    def insert_at_head(self, data):
        new_node = Node(data)
        new_node.next = self.head  # i need to change new node reference to head
        self.head = new_node  # new node store data of head... i need to point head of new node

    #
    # def insert_at_tail(self, data):
    #     new_node = Node(data)
    #     if self.head is None:
    #         self.head=new_node
    #     else:
    #         n=self.head
    #         while n.ref is not None:
    #             n=n.ref
    #         n.ref = new_node
    def insert_at_tail(self, data):
        new_node = Node(data)
        node = self.head  # go to next node
        while node.next:  # node.next not none it reference to next node means not empty for loop move to next node
            node = node.next
        node.next = new_node

    def insert_at_index(self, index, data):
        new_node = Node(data)
        node = self.head
        for i in range(index - 1):  # i to ind-1
            node = node.next  #upto the index-1 pointed
        new_node.next = node.next
        node.next = new_node

    def delete_at_head(self):
        node = self.head
        self.head = node.next  # for remove 1st node we point head to 2nd node
        node.next = None

    def delete_at_tail(self):
        node = self.head.next  # to delete the tail we have to go 2nd last node neeed to change 2nd last node to null
        prev = self.head
        while node.next is not None:
            node = node.next
            prev = prev.next
        prev.next = None

    def delete_at_index(self, index):
        node = self.head.next  #
        prev = self.head
        for i in range(index - 1):  # we need to disconnect link index-1  we travel ind toind-1
            node = node.next  # ref to last node
            prev = prev.next  #
        prev.next = node.next  # disconnect value
        node.next = None  # node null


L = SingleLinkedList()
L.insert_at_head(20)
L.insert_at_tail(30)
L.insert_at_tail(40)
L.insert_at_tail(60)
L.insert_at_head(10)
L.insert_at_index(4, 50)
L.display()
L.delete_at_head()
L.display()
L.delete_at_tail()
L.display()
L.delete_at_index(3)
L.display()
