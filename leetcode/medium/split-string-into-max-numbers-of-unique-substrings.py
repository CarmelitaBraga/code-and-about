class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        hashset = set()
        i, j = 0, 0
        count = 0
        while i < len(s) and j < len(s):
            if not s[i:j+1] in hashset:
                hashset.add(s[i:j+1])
                i = j+1
                count += 1
            j += 1

        return count

