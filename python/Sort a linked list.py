__author__ = 'erik'


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param {ListNode} head
    # @return {ListNode}
    def sortList(self, head):
        size = 0
        p = head
        while p:
            size += 1
            p = p.next

    def mergeSort(self, head, nums):
        pass

if __name__ == '__main__':
    s = Solution()
    print s.sortList()
