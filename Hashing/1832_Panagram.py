# A pangram is a sentence where every letter of the English alphabet appears at least once.

# Given a string sentence containing only lowercase English letters, return true if sentence is a 
# pangram, or false otherwise.




class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        hashmap = {}
        alphabet = 'abcdefghijklmnopqrstuvwxyz'
        for letter in alphabet:
            hashmap[letter] = 0
        for letter in sentence:
            if letter in hashmap:
               hashmap[letter] +=1
            else:
                 hashmap[letter] = 1
        if 0 in hashmap.values():
            return False
        return True
        
# Create a hashmap that contains the alphabet and equate each key to Zero
# then loop through the string and each time we see a letter, we increment the hashmap value of that letter
# by one
# at the end just check which value is zero and return False, 
#     else return True