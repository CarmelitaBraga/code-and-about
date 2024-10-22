class Solution:
    def reverse_and_invert(s):
        rs = ''
        for i in range(len(s)-1,-1,-1):
            if s[i] == '0':
                rs += '1'
            else:
                rs += '0'

        return rs

    def findKthBit(self, n: int, k: int) -> str:
        s = '0'
        for _ in range(n):
            sn = Solution.reverse_and_invert(s)
            s += '1' + sn

        return s[k-1]