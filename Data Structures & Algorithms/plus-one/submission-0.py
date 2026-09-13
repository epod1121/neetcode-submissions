class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        num = 0
        count = 0

        for i in range(len(digits)-1, -1, -1):
            num += (digits[i] * (10**count))
            count += 1

        num += 1
        output = []

        for c in str(num):
            output.append(c)

        return output