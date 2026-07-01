class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diffs ={}
        for idx, num in enumerate(nums):
            diff = target - nums[idx]
            if diff in diffs:
                if idx < diffs[diff]:
                    return [idx, diffs[diff]]
                elif idx > diffs[diff]:
                    return [diffs[diff],idx]
            diffs[num] = idx
