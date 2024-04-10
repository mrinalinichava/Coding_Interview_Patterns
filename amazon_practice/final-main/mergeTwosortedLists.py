class ListNode:
    def __init__(self,val = 0,next = None):
        self.val = val
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None


    def mergeTwoSortedLists(self,head1,head2):
        dummy = ListNode()
        temp = dummy
        temp1,temp2 = head1,head2

        while(temp1 and temp2):
            if(temp1.val<temp2.val):
                temp= temp1
                temp1=temp1.next
            else:
                temp= temp2
                temp2=temp2.next
            temp=temp.next

        if(temp1):
            temp.next = temp1
        if(temp2):
            temp.next = temp2
        return dummy.next