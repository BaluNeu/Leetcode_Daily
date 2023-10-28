# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
            # if not head or not head.next or not head.next.next:
    #     return head

    # 1. Find the middle of the linked list
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

    # 2. Reverse the second half
        prev, curr = None, slow
        while curr:
            next_temp = curr.next
            curr.next = prev
            prev = curr
            curr = next_temp

    # 3. Merge the two halves
        first, second = head, prev
        while second.next:
            first_next = first.next
            first.next = second
            first = first_next

            second_next = second.next
            second.next = first_next
            second = second_next

        return head

        