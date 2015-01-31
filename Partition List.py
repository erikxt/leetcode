# -*- coding: cp936 -*-
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param head, a ListNode
    # @param x, an integer
    # @return a ListNode
    def partition(self, head, x):
        if not head:
            return head
        
        last=ListNode(0)
        last.next=head
        vhead=last
    
        current=last.next    
        marker=None  # QSort way
    
        while True:
            if current==None:
                break    
            if current.val>=x:
                if not marker:
                    marker=last
                    print marker.val
            elif marker:
                tmp=marker.next
                marker.next=current
                last.next=current.next
                current.next=tmp
                marker=current
                current=last.next
                continue
            last=current
            current=current.next
        return vhead.next

    def showList(self, ret):
        restr = ""
        while ret <> None:
            restr += str(ret.val)
            restr += ", "
            ret = ret.next
        print restr
            
        
def main():
    data = (1, 4, 3, 2, 5, 2 )
    head, prev = None, None
    for x in data:
        node = ListNode(x)
        if head == None:
            head = node
            prev = node
        else:
            prev.next = node
            prev = prev.next
    s = Solution()
    ret = s.partition(head, 3)
##    s.showList(ret)
    
    
if __name__ == "__main__":
    main()
        
        
