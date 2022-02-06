# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        if n==1 and head.next == None:
            return ListNode()

        left = head
        right = head
        for _ in range(n):
            left = left.next
        if not left:
            return head.next
        while left.next:
            left = left.next
            right = right.next
        right.next = right.next.next
        return head