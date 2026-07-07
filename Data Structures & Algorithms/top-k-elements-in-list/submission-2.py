class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        buckets ={}
        result = []
        for i in nums:
            if i in counts:
                counts[i] +=1
            else:
                counts[i] = 1
        for num, freq in counts.items():
            if freq in buckets:
                buckets[freq].append(num)
            else:
                buckets[freq] = [num]
        for r in range(len(nums),0,-1):
            if r in buckets:
                result.extend(buckets[r])
            if len(result) >= k:
                return result
        



