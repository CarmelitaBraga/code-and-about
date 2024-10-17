class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        shortest = word1 if len(word1) <= len(word2) else word2
        longest = word1 if len(word1) > len(word2) else word2
        merged = ''
        for i in range(len(shortest)):
            merged += word1[i]
            merged += word2[i]
        
        if len(longest) > i:
            merged += longest[i+1:]

        return merged