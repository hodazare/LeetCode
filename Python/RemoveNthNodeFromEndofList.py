"""
Given a linked list, remove the n-th node from the end of list and return its head. 
The algorithm makes one traversal of the list of LL nodes. Therefore time complexity is O(L)O(L).

Example:

Given linked list: 1->2->3->4->5, and n = 2.

After removing the second node from the end, the linked list becomes 1->2->3->5.
Note:

Given n will always be valid.
"""
def removeNthFromEnd(head, n):
        
        first = second = head
        
        i = 0
        while i <= n and second:
            second = second.next
            i += 1
            
        # remove head
        if i <= n:
            head = head.next
            return head
            
        while second:
            first = first.next
            second = second.next

        first.next = first.next.next
        return head
