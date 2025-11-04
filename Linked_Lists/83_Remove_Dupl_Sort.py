# Given the head of a sorted linked list, delete all duplicates 
# such that each element appears only once. Return the linked list 
# sorted as well

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def del_node(self, node_to_del, prev_node):
        prev_node.next = node_to_del.next

    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        previous = None
        check = set()
        ptr = head
        while ptr:
            if ptr.val in check:
                self.del_node(ptr, previous)
            else:
                check.add(ptr.val)
                previous = ptr
            ptr = ptr.next
        
        return head
    
# This is a combersome Solution
# What you should have done was this

    current = head 
            while current and current.next:
                if current.val == current.next.val:
                    current.next = current.next.next
                else:
                    current = current.next
            return head

# this is much better