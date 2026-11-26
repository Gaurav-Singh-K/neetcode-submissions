class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        s = set(nums)
        max_len = 0

        for x in s:
            if x - 1 not in s:
                count = 1
                while x + count in s:
                    count += 1

                max_len = max(max_len, count)

        return max_len
        
        