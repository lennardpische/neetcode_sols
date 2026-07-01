class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diffs ={}
        for idx, num in enumerate(nums):
            diff = target - nums[idx]
            if diff in diffs:
                return [diffs[diff],idx]
            diffs[num] = idx
