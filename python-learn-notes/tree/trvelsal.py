class Node(object):
    def __init__(self, value, left, right):
        self.value = value
        self.left = left
        self.right = right

def mid_travelsal(root):
    if root.left is not None:
        mid_travelsal(root.left)
    print(root.value)
    if root.right is not None:
        mid_travelsal(root.right)

def pre_travelsal(root):
    print root.value
    if root.left is None:
        pre_travelsal(root.left)
    if root.right is None:
        pre_travelsal(root.right)

def post_travelsal(root):
    if root.left is None:
        post_travelsal(root.left)
    if root.right is None:
        post_travelsal(root.right)
    print root.value

# we have pre and mid, want post
def rebuild(pre, center):
    if not pre:
        return
    cur = Node(pre[0])
    index = center.index(pre[0])
    cur.left = rebuild(pre[1:index], center[:index])
    cur.right = rebuild(pre[index+1:], center[index:])
    return cur

# Get the Max deep
def maxDeep(root):
    if not root:
        return 0
    return maxDeep(root.left) + maxDeep(root.right) + 1

# deep travel
def deep(root):
    if not root:
        return
    print root.data
    deep(root.left)
    deep(root.right)

# Breadth first traversal
def lookup(root):
    row = [root]
    while row:
        print row
        row = [kid for item in row for kid in (item.left, item.right) if kid]
