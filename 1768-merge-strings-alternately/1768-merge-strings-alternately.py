class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        greaterString = len(word1) + len(word2)
        empty_string = ""
        i =0 
        while i < (greaterString):
            if i < len(word1):
                empty_string = empty_string + word1[i]
                print("iter word1",i)

            if i < len(word2):
                empty_string = empty_string + word2[i]
                print("iter word2",i)

            
            i+=1
        return empty_string