class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        
        max = 0
        count = 0

        for n in nums:
            if n == 1:
                count += 1
            if n == 0:
                if count > max:
                    max = count
                count = 0

        if count > max: max = count
        return max