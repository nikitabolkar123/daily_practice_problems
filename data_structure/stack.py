# linear data structure
# elements are arranged in sequential manner
# follow ---LIFO last in first out
# example--plates in a tray,arranging the coins,books
# opeartion
# push---inserting an elements into the stack
# pop---delete an elements from stack
# top stack ---push and pop
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:  # last in first out or first in last out
    def __init__(self):
        self.head = None

    def traverse(self):  # get the value of each node
        if self.head is None:
            print("Linked list is empty")
        else:
            n = self.head
            while n is not None:
                print(n.data)
                n = n.next

    def push(self, data):
        new_node = Node(data)
        new_node.next=self.head
        self.head = new_node

    def pop(self):  # remove topmost elem
        if self.head is Node:
            print("stack is empty")
        else:
            temp = self.head
            self.head = self.head.next  # to get the reference of 2nd node present in the "next" part of thr 1st node
            return temp.data

    def peek(self):  # The peek() method is used to look at the object at the top of this stack
        if self.head is None:     # without removing it # from the stack.
            print("stack is empty")
        return self.head.data


if __name__ == "__main__":
    obj = Stack()
    obj.push(10)
    obj.push(20)
    obj.push(30)
    obj.push(40)
    obj.push(50)
    obj.traverse()
    print("pop() ====> ", obj.pop())
    obj.traverse()

    print("peek() ====> ", obj.peek())
