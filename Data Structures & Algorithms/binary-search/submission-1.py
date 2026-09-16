class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start, end = 0, len(nums)-1
        while start <= end:
            middle = (start + end) // 2
            if nums[middle] == target:
                return middle
            if nums[start] == target:
                return start
            if nums[end] == target:
                return end
            if nums[middle] < target:
                start = middle + 1
            if nums[middle] > target:
                end = middle - 1
        return -1