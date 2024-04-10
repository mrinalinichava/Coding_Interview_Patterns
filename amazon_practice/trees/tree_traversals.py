import Tree
from collections import deque

arr = [1,2,3,4,5,6,7,8]
root = Tree.construct_tree(arr)

def inorder(root):
    if(root is None):
        return None
    if(root):
        inorder(root.left)
        print(root.value)
        inorder(root.right)
print(inorder(root))


def levelOrder(root):
    if(not root):
        return

    queue = []
    output = []
    queue.append(root)
    while(queue):
        size = len(queue)
        level = []
        while(size):
            ele = queue.pop(0)
            level.append(ele.value)
            if(ele.left):
                queue.append(ele.left)
            if(ele.right):
                queue.append(ele.right)
            size-=1
        output.append(level)
    return output

print(levelOrder(root))



def spiralLevelOrder(root):

    dq = deque()
    dq.append(root)
    reverse = True
    output = []
    while dq:
        size = len(dq)
        level = []
        if(not reverse):
            while(size>0):
                ele = dq.popleft()
                level.append(ele.value)
                if(ele.left):
                    dq.append(ele.left)
                if(ele.right):
                    dq.append(ele.right)
                size-=1
            reverse = not reverse
            output.append(level)

        else:
            while(size>0):
                ele = dq.pop()
                level.append(ele.value)
                if(ele.right):
                    dq.append(ele.right)
                if(ele.left):
                    dq.append(ele.left)
                size-=1
            reverse = not reverse
            output.append(level)

    return output


print(spiralLevelOrder(root))







