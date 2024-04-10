# Here's a Python script to define a linked list and test the `reverseList` function.

class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, value):
        if not self.head:
            self.head = ListNode(value)
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = ListNode(value)

    def to_list(self):
        result = []
        current = self.head
        while current:
            result.append(current.value)
            current = current.next
        return result

    def reverseList(self, head):
        temp = prev = None
        curr = head
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev

    def reverse(self):
        self.head = self.reverseList(self.head)

# Helper function to print list nodes for verification
def print_list(node):
    while node:
        print(node.value, end=" -> ")
        node = node.next
    print("None")

# Test the reverse function
ll = LinkedList()
ll.append(1)
ll.append(2)
ll.append(3)
ll.append(4)
ll.append(5)

print("Original linked list:")
print_list(ll.head)

ll.reverse()

print("Reversed linked list:")
print_list(ll.head)
