# Given an array of strings strs, group the anagrams together. 
# You can return the answer in any order.

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = []
        lookup = {}
        for word in strs:
            if ''.join(sorted(word)) in lookup:
                lookup[''.join(sorted(word))].append(word)
            else:
                lookup[''.join(sorted(word))] = [word]
        for key, value in lookup.items():
            ans.append(value)
        return ans

# best way to check if words is an anagram is to sort the word and
# just check if they match

# Better way to do this is by saving the keys as a tuple because just
# saving them as a list(becasue you used sorted) wont work because it is 
# muttable.

# ''.join(sorted(word)) --> tuple((sorted(word)))