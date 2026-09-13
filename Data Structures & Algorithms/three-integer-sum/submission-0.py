class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        for i in range(len(nums)):
            j, k = i+1, len(nums)-1
            target = -nums[i]
            while j < k:
                if nums[j] + nums[k] < target:
                    j += 1
                if nums[j] + nums[k] > target:
                    k -= 1
                if nums[j] + nums[k] == target and i<j<k: 
                    new = [nums[i], nums[j], nums[k]]
                    if new not in res:
                        res.append([nums[i], nums[j], nums[k]])
                    k -= 1
        
        return res