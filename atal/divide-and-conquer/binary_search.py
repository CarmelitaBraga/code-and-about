class Solution:
    @staticmethod
    def binary_search(conjunto, left, right, x):
        if left <= right:
            middle = (left + right) // 2
            mid = conjunto[middle]

            if mid == x:
                return middle
            elif mid > x:
                return Solution.binary_search(conjunto, left, middle-1, x)
            else:
                return Solution.binary_search(conjunto, middle+1, right, x)
        return -1

    def search(self, nums: List[int], target: int) -> int:
        return self.binary_search(nums, 0, len(nums)-1, target)