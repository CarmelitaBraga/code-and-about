from math import inf
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        l1, l2 = len(nums1), len(nums2)
        o = (l1 + l2)//2
        median_i, median_j = (o, -1) if (l1 + l2) % 2 != 0 else (o, o-1)
        inf_e = float(inf)
        nums1.append(inf_e)
        nums2.append(inf_e)
        i, j, x = 0, 0, 0
        new = []
        median = 0
        while i < len(nums1) and j < len(nums2):
            if nums1[i] <= nums2[j]:
                new.append(nums1[i])
                i += 1
            else:
                new.append(nums2[j])
                j += 1
            if median_j == -1:
                if x == median_i:
                    median = new[x]
                    break
            else:
                if x == median_j:
                    median = new[x]
                elif x == median_i:
                    print(new)
                    median += new[x]
                    median = median / 2
                    break
            x += 1
        return median
