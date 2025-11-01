# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        # Convert nums to a set for O(1) lookups
        to_delete = set(nums)
        
        dummy = ListNode(0)
        dummy.next = head
        curr = dummy
        
        # Traverse and remove nodes whose values are in to_delete
        while curr.next:
            if curr.next.val in to_delete:
                curr.next = curr.next.next
            else:
                curr = curr.next
                
        return dummy.next
