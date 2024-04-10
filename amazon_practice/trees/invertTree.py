# Python3 implementation of above approach

# A class to create a new node
from collections import deque


class newNode:
    def __init__(self, data):
        self.value = data
        self.left = None
        self.right = None


def spiralPrint(root):
    dq = deque()
    dq.append(root)
    reverse = True
    output = []
    while (dq):
        size = len(dq)
        l=[]
        if (not reverse):
            while (size > 0):
                ele = dq.popleft()
                size -= 1
                if (ele.left):
                    dq.append(ele.left)

                if (ele.right):
                    dq.append(ele.right)

                l.append(ele.value)
            output.append(l)
            # print(output)
            reverse = not reverse
        else:

            while (size > 0):
                size -= 1
                # Insert the child in the front of the deque
                # Right child first
                ele = dq.pop()

                if (ele.right != None):
                    dq.appendleft(ele.right)

                if (ele.left != None):
                    dq.appendleft(ele.left)

                l.append(ele.value)
            output.append(l)
            # print(output)
            reverse = not reverse
    return output
def inorder(root):
    if(not root):
        return
    inorder(root.left)
    print(root.value)
    inorder(root.right)

def invertTree(root):
    if(not root):
        return

    root.left,root.right = root.right,root.left
    invertTree(root.left)
    invertTree(root.right)
    return root



# Driver Code
if __name__ == '__main__':
    root = newNode(1)
    root.left = newNode(2)
    root.right = newNode(3)
    root.left.left = newNode(4)
    root.left.right = newNode(5)
    root.right.left = newNode(6)
    root.right.right = newNode(7)
    print("Inverting a tree :")
    root = invertTree(root)
    print(inorder(root))
