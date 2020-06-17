class Node:
    def __init__(self,key):
        self.right=None
        self.left=None
        self.val=key


def maxdepth(root):
    if root==None:
        return 0

    # recursively getting height    
    leftDepth=maxdepth(root.left)
    rightDepth=maxdepth(root.right)    

    if leftDepth>rightDepth:
        return leftDepth+1
    else:
        return rightDepth+1    






if __name__ == "__main__":
    
    # root node level 0
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.right.left = Node(5)
    root.right.right = Node(6)
    root.right.right.left = Node(8)
    root.right.left.right = Node(7)

    print("max depth is : " ,maxdepth(root))


