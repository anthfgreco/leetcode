# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow, fast = head, head
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next
        return slow
    
"""
Slow and fast pointers approach

slow moves ahead 1 node per iteration
fast moves ahead 2 nodes per iteration

when fast either doesn't exist or has no next to point to,
slow is at the middle of the list, so return it
"""
        