class ListNode:
    def __init__(self,val= 0,next =None):
        self.val = val
        self.next = next

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

    def findNthNode(self,n):

        fast = self.head
        slow = self.head
        prev = None
        for _ in range(n):
            fast = fast.next

        while(fast):
            slow = slow.next
            fast = fast.next
        print(slow.val)

    def removeNthNode(self,n):
        fast = slow = self.head
        for _ in range(n):
            fast = fast.next

        while(fast and fast.next):
            slow = slow.next
            fast= fast.next

        print("slow")
        print(slow.val)
        slow.next = slow.next.next
        return self.head.next

    def printList(self):
        temp = self.head
        while(temp):
            print(str(temp.val) + "-->")
            temp = temp.next



list1 = LinkedList()

list1.append(1)
list1.append(2)
list1.append(3)
list1.append(4)
list1.append(5)
list1.append(6)
list1.append(7)
list1.removeNthNode(3)
list1.printList()


