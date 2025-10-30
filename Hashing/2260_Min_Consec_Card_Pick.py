# You are given an integer array cards where cards[i] represents the 
# value of the ith card. A pair of cards are matching if the cards have
# the same value.

# Return the minimum number of consecutive cards you have to pick up to 
# have a pair of matching cards among the picked cards. If it is 
# impossible to have matching cards, return -1.



class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        ans  = float('inf')
        count = {}
        for i in range(len(cards)):
            if cards[i] in count:
                check = max(count[cards[i]])
                ans = min(ans, i - check +1 )
                count[cards[i]].append(i)

            else:
               count[cards[i]] = [i]
        if ans != float('inf'):
            return ans
        else:
            return -1
        
# Use a count to take note of the occurences of cards, using a list 
#     to store of the values for the key value pair
# Loop through the list of cards and if the card has appeared in the count
#     compare the curr ans and the difference between the current index
#     and the the index of the last occurence of the card

# if it is not in count then just append the index it occured at to count
