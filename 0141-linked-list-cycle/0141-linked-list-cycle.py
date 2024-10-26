class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head
        
        while fast and fast.next:
            slow = slow.next       # Move slow pointer by 1 step
            fast = fast.next.next  # Move fast pointer by 2 steps
            
            if slow == fast:       # Cycle detected
                return True
        
        return False               # No cycle detected
