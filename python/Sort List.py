__author__ = 'erica'


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param {ListNode} head
    # @return {ListNode}
    def sortList(self, head):
        if not head or not head.next:
            return head

        fast, slow = head, head
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next

        prev.next = None

        head1 = self.sortList(head)
        head2 = self.sortList(slow)
        return self.merge(head1, head2)

    def merge(self, head1, head2):
        ptr = ListNode(None)
        ptr1, ptr2, prePtr = head1, head2, ptr
        while ptr1 and ptr2:
            if ptr1.val < ptr2.val:
                ptr.next = ptr1
                ptr1 = ptr1.next
            else:
                ptr.next = ptr2
                ptr2 = ptr2.next
            ptr = ptr.next
        if ptr1:
            ptr.next = ptr1
        if ptr2:
            ptr.next = ptr2
        return prePtr.next

if __name__ == '__main__':
    a = ListNode(3)
    b = ListNode(2)
    c = ListNode(4)
    l = a
    a.next = b
    b.next = c
    s = Solution()
    l = s.sortList(l)
    while l:
        print l.val
        l = l.next
