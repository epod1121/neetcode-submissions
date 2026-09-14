class Solution:
    def countSeniors(self, details: List[str]) -> int:
        
        count = 0

        for p in details:
            substring = p[11: 13: 1]
            if int(substring) > 60:
                count += 1

        return count