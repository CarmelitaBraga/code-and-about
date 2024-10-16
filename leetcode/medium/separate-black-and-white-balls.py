class Solution:
    def minimumSteps(self, s: str) -> int:
        x0, p0 = 0, []
        for i in range(len(s)):
            if s[i] == '0':
                x0 += 1
                p0.append(i)
        
        count = 0
        for i in range(len(p0)-1, -1, -1):
            count += abs(p0[i] - i)

        return count
    

# Optimized
# class Solution:
#     def minimumSteps(self, s: str) -> int:
#         swap, black = 0, 0

#         for i in range(len(s)):
#             if s[i] == '0':
#                 swap += black
#             else:
#                 black += 1
        
#         return swap