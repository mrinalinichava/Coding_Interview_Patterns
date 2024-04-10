class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class Linked_list:
    def __init__(self):
        self.head = Node()

    def append(self, data):
        new_node = Node(data)
        curr = self.head
        while (curr.next != None):
            curr = curr.next
        curr.next = new_node

    def length(self):
        curr = self.head
        total = 0
        while (curr.next != None):
            total = total + 1
            curr = curr.next
        return total

    def display(self):
        elems = []
        curr_node = self.head
        while (curr_node.next != None):
            curr_node = curr_node.next
            elems.append(curr_node.data)
        print(elems)

    def get(self, index):
        curr = self.head
        i = 0
        if (index > self.length()):
            print("error")
            return None
        while (i < index):
            curr = curr.next
            i = i + 1
        return curr.next.data

    def delete(self, index):
        if (index >= self.length()):
            print('Error')
        i = 0
        curr_node = self.head
        if (self.length() == 1 and index == 0):
            curr_node.data = None
            curr_node.next = None
        elif (self.length() > 0):
            while (i < index):
                curr_node = curr_node.next
                i = i + 1
            t = curr_node.next
            curr_node.next = t.next

    def reverseList(self):
        temp = prev = None
        curr = self.head
        while (curr):
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev

my_list = Linked_list()
my_list.display()
my_list.append(1)
my_list.append(2)
my_list.append(3)
my_list.append(4)
my_list.append(14)
my_list.reverseList()
my_list.display()
