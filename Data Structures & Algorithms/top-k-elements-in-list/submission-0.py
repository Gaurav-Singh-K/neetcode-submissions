class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        l = []
        for num in nums:
            if num not in d.keys():
                d[num] = 1
            else:
                d[num] += 1
        l = [key for key, val in sorted(d.items(), key=lambda item: item[1], reverse= True)]
        return l[:k]
            