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
        # 只有一个节点
        if head.next == None:
            return None
        index1 = head
        index2 = head
        # 删除尾节点
        if n == 1:
            while(index1.next.next != None):
                index1 = index1.next
            index1.next = None
            return head
        # 遍历到n-1位置，
        for i in xrange(n):
            index1 = index1.next

        # 遍历直到尾节点
        while (index1.next != None):
            index1 = index1.next
            index2 = index2.next
        print index2.val
        # delete 非尾节点,尾节点情况前面已经处理
        index2.val = index2.next.val
        index2.next = index2.next.next
            
        return head

