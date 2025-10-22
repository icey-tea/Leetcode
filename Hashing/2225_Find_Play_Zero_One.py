# You are given an integer array matches where matches[i] = [winneri, loseri] indicates that the player 
# winneri defeated player loseri in a match.

# Return a list answer of size 2 where:

# answer[0] is a list of all players that have not lost any matches.
# answer[1] is a list of all players that have lost exactly one match.
# The values in the two lists should be returned in increasing order.



from collections import defaultdict
class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        answer = [[],[]]
        total_app = defaultdict(int)
        status = defaultdict(int)
        for match in matches:
            for i, person in enumerate(match):
                if i == 0 :
                    status[person] +=1
                else:
                    status[person] -=1
                total_app[person] +=1
        for key in total_app:
            if total_app[key] == status[key]:
                answer[0].append(key)
            elif total_app[key] - status[key] == 2:
                answer[1].append(key)
        answer[1] = sorted(answer[1])
        answer[0] = sorted(answer[0])
        return answer
    
#Brute force method was used here
#Take note of all the appearances that the person made and also calculate their stauts (+1 win, -1 loss)
# Then check if the total appearances are equals to the status and append it to answer[0]
#     or chceck if there is a difference of two between the two and just append it to answer[1]


##############
This is a better Solution

class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        OnlyWins , MoreLosses , OneLoss = set(),set(),set()
        for match in matches:
            winner = match[0]
            loser = match[1]
            if winner not in MoreLosses and winner not in OneLoss:
                OnlyWins.add(winner)

            if loser in OnlyWins:
                OnlyWins.remove(loser)
                OneLoss.add(loser)
            elif loser in OneLoss:
                OneLoss.remove(loser)
                MoreLosses.add(loser)
            elif loser in MoreLosses:
                continue
            else:
                OneLoss.add(loser)
        answer = [sorted(list(OnlyWins)), sorted(list(OneLoss))]
        return answer
            
            
