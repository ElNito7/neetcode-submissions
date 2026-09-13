class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ans = {}
        for i in range(len(nums)):
            j = target - nums[i]
            if j in ans:
                return [ans[j], i]
            ans[nums[i]] = i
