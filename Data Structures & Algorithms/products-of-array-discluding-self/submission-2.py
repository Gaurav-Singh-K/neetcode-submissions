class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l = []        
        r = [0]*len(nums)
        ans = []
        a = 1
        for i in range(len(nums)):
            if i == 0:
                l.append(a)
            else:
                a = a*nums[i-1]
                l.append(a)
        a = 1
        for i in range(len(nums)-1, -1, -1):
            if i == len(nums)-1:
                r[i] = 1
            else:
                a = a*nums[i+1]
                r[i] = a
        for i in range(len(l)):
            ans.append(l[i] *r[i])
        return ans