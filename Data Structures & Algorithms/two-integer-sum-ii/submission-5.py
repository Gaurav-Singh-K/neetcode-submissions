class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i in range(len(numbers)):
            a = target-numbers[i]
            n = len(numbers)-1
            j = i+1
            while j <= n:
                mid = (j+n)//2
                if numbers[mid] == a:
                    return[i+1, mid+1]
                elif numbers[mid] > a:
                    n = mid-1
                else:
                    j = mid+1

        return []
        