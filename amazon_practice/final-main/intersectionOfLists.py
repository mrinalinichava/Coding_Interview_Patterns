

class ListNode:
    def __init__(self,val):
        self.val = val
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self,val):
        if(not self.head):
            self.head = ListNode(val)
        else:
            temp = self.head
            while(temp.next):
                temp = temp.next
            temp.next = ListNode(val)

    def getLength(self,head):
        temp = head
        count = 0
        while(temp):
            count += 1
            temp = temp.next
        return count

    def intersection(self,head1,head2):
        len1 = self.getLength(head1)
        len2 = self.getLength(head2)

        diff = abs(len1-len2)
        if(len1>len2):
            return self.getIntersection(head1,head2,diff)
        else:
            return self.getIntersection(head2, head1, diff)


    def getIntersection(self,head1,head2,diff):
        for _ in range(diff):
            head1 = head1.next

        while(head1 and head2):
            if(head1==head2):
                return True
            head1= head1.next
            head2= head2.next

        return False

    def printList(self):
        temp = self.head
        while(temp):
            print(str(temp.val) + "-->")
            temp = temp.next

list1 = LinkedList()
list2 = LinkedList()

# Populate the first list (1 -> 2 -> 3)
list1.append(1)
list1.append(2)
list1.append(3)

# Populate the second list (4 -> 5) and then intersect it with list1 (at value 3)
list2.append(4)
list2.append(5)
# Manually create an intersection; for this example, let's intersect at node with value 3 from list1
list2.head.next.next = list1.head.next.next  # This makes node with value 3 the intersection

print(list1.printList())
print(list2.printList())

# Find the intersection
intersection_node = list1.intersection(list1.head, list2.head)

if intersection_node:
    print(f"Intersection found ")
else:
    print("No intersection found")