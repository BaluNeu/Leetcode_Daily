# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        curr = head
        end = head
        # count = 0

        while k > 1:
            curr = curr.next
            k-=1

        front = curr
        print(front.val)

        while curr.next:
            curr = curr.next
            end = end.next
        print(end.val)

        temp = front.val
        front.val = end.val
        end.val = temp

        return head
        