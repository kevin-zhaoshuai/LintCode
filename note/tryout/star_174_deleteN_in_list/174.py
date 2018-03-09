"""
Definition of ListNode

class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    """
    @param head: The first node of linked list.
    @param n: An integer
    @return: The head of linked list.
    """
    def removeNthFromEnd(self, head, n):
        # O(n) and 遍历一次. 
        # Assume that n less than the length of the list
        # 算法的边界问题应该在一开始就考虑并实现

        index1 = head
        index2 = head

        if n == 1:
            # 只有一个节点
            if head.next == None:
                return None

        # 走n-1. 从0...n-2即可
        for i in xrange(n-1):
            index1 = index1.next

        # 遍历直到尾节点
        while (index1.next != None):
            index1 = index1.next
            index2 = index2.next
        # delete 的是头结点，返回头结点的next
        if index2 == head:
            return index2.next

        if index2.next != None:
            # delete 非尾节点,尾节点情况前面已经处理
            index2.val = index2.next.val
            index2.next = index2.next.next
        else:
            index3= head.next
            index4 = head
            while (index3.next!= None):
                index3 = index3.next
                index4 = index4.next
            index4.next = None
