def isSameTree(p, q):
    if p == None and q == None:
        return True
    elif p and q:
        return p.value == q.value and isSameTree(p.left, q.left) and isSameTree(p.right, q.right)
    else:
        return False
