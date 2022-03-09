# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        root = dummy = ListNode()
        
        # While there are values remaining to be added
        while l1 or l2 or carry==1:
            l1_val = 0
            l2_val = 0
            if l1:
                l1_val = l1.val
                l1 = l1.next
            if l2:
                l2_val = l2.val
                l2 = l2.next
            
            sum = l1_val + l2_val + carry
            if sum >= 10:
                carry = 1
                sum = sum % 10
            else:
                carry = 0
                
            root.next = ListNode(sum)
            root = root.next
            
        return dummy.next
                
            
            
            
            
                 
        