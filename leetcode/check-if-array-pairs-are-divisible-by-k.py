class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        freq = [0] * k

        for num in arr:
            rem = num%k
            freq[rem] += 1

        if freq[0] % 2 != 0:
            return False

        for i in range(1, (k//2)+1):
            if freq[i] != freq[k-i]:
                return False
        
        return True


# Also works, but the above one is more optimized
# from collections import defaultdict

# class Solution:
#     def canArrange(self, arr: List[int], k: int) -> bool:
#         freq = defaultdict(list)

#         if k == 1:
#             return True
        
#         if sum(arr) % k != 0:
#             return False

#         for i in range(len(arr)):
#             m = arr[i] % k
#             if m != 0:
#                 freq[m].append(i)

#         enough = True

#         if len(freq.keys()) > 1:
#             for r in freq.keys():
#                 comp = k-r
#                 list_r = freq.get(r)
#                 list_c = freq.get(comp)
#                 if not list_r or not list_c or len(list_r) != len(list_c):
#                     enough = False
            
#             return enough
        
#         else:
#             i, j = 0, (len(arr)-1)
#             while i < len(arr):
#                 while i < j:
#                     if (arr[i] + arr[j]) % k == 0:
#                         arr.remove(arr[j])
#                         arr.remove(arr[i])
#                         i = 0
#                         j -= 2
#                     else:
#                         j -= 1
#                 i += 1
#                 j = len(arr)-1

#         if len(arr) == 2 and (arr[0] + arr[1]) % k == 0:
#             arr = []
   
#         return len(arr) == 0 and sum(arr) % k == 0
