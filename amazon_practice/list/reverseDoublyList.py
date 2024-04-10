# class Node:
#     def __init__(self,data):
#         self.data = data
#         self.next = None
#         self.prev = None
#
# class DoublyLinkedList:
#     def __init__(self):
#         self.head = None
#
#     def append(self,data):
#         new_node = Node(data)
#         if(not self.head):
#             self.head = new_node
#             return
#         temp = self.head
#         while(temp):
#             temp = temp.next
#         temp.next = new_node
#         new_node.prev = temp
#
#     def reverse(self):
#         temp = None
#         curr = self.head
#         while(curr):
#             temp = curr.prev
#             curr = curr.next
#



class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node
        new_node.prev = last_node

    def reverse(self):
        temp = None
        current = self.head
        while current:
            temp = current.prev
            current.prev = current.next
            current.next = temp
            current = current.prev
        if temp:
            self.head = temp.prev

# Helper function to print the list
def print_doubly_linked_list(node):
    while node:
        print(node.data, end=' ')
        node = node.next
    print()

# Create the doubly linked list and append items
dll = DoublyLinkedList()
dll.append(1)
dll.append(2)
dll.append(3)
dll.append(4)

# Print the original list
print("Original List:")
print_doubly_linked_list(dll.head)

# Reverse the list
dll.reverse()

# Print the reversed list
print("Reversed List:")
print_doubly_linked_list(dll.head)


