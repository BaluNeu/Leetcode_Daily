# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

    #1. create a dummy node

        dummy  = ListNode(0,head)

    #2. left at dummy and right at n

        left = dummy

        right = head

        while n>0 and right:
            right = right.next
            n-=1

    #3. keep traversing untill right is none

        while right:
            left = left.next
            right = right.next

    #4. left will be at required position

        left.next = left.next.next

    #5 return dummy.next (head)

        return dummy.next









        