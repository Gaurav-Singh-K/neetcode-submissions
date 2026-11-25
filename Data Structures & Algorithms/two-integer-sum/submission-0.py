class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        l = []
        for i in range(len(nums)):
            x = target-nums[i]
            for j in range(i+1, len(nums)):
                if x == nums[j]:
                    l.append(i)
                    l.append(j)
                    break
        return l
        