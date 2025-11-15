# In a linked list of size n, where n is even, the ith node 
# (0-indexed) of the linked list is known as the twin of the (n-1-i)th 
# node, if 0 <= i <= (n / 2) - 1.

# For example, if n = 4, then node 0 is the twin of node 3, and node 
# 1 is the twin of node 2. These are the only nodes with twins for n = 4.
# The twin sum is defined as the sum of a node and its twin.

# Given the head of a linked list with even length, return the
#  maximum twin sum of the linked list.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        fast = head
        slow = head
        prev = None
        twin_sum = 0
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        #Reverse second half
        curr = slow
        nextnode = slow.next
        while curr:
            nextnode = curr.next
            curr.next = prev
            prev = curr
            curr = nextnode
        
        twinHalf = prev
        slow = head
        while twinHalf:
            twin_sum = max(slow.val + twinHalf.val, twin_sum)
            slow = slow.next
            twinHalf = twinHalf.next
        return twin_sum
    
###
# What you do here is find the middle of the linked list,
# Then you reverse the second half of the linked list and 
# after that as you go through the two halfs of the likned lists, you 
# add up the values and compare them to the max of the prevoius one