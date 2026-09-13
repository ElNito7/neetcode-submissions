class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        prev = {}
        for i in range(len(numbers)):
            if numbers[i] in prev:
                return [prev[numbers[i]], i+1]
            prev[target - numbers[i]] = i+1 
        return None
            