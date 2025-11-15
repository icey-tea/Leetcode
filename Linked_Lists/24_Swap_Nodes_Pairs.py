# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy

        while head and head.next:
            first  = head
            second = head.next
            nextnode = second.next

            #swap
            first.next = nextnode
            second.next = first
            prev.next = second
            
            
            #update pointers
            prev = first
            head = nextnode

        return dummy.next


##Lowkey the most confusing but i get it now
# The Swap Nodes in Pairs problem asks us to swap every two adjacent 
# nodes in a linked list, like turning 1 → 2 → 3 → 4 into 2 → 1 → 4 → 3. 
# To solve this cleanly, we use the cheeky linked list formula—protect the
# head, peek ahead, rewire, and move.

# We start by checking if the list is too short to swap; if so, we 
# return it. Then we create a dummy node before the head to keep track of the new start of the list. We set prev = dummy and use a loop that runs while both head and head.next exist. Inside the loop, we name our pointers: first = head, second = head.next, and next_pair = head.next.next.

# Next comes the swap:

# prev.next = second — connects the previous node to the second.

# first.next = next_pair — connects the first node to what follows.

# second.next = first — completes the swap.

# Then we move forward: prev = first and head = next_pair. When the 
# loop ends, we return dummy.next, which points to the new head.

# This method works for both even and odd-length lists and avoids 
# pointer confusion by always rewiring before moving. It’s an elegant, 
# reliable approach that captures the “cheeky” trick—save, swap, and slide.