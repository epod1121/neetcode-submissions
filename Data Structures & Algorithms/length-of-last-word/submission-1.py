class Solution:
    def lengthOfLastWord(self, s: str) -> int:

        if not s:
            return 0
        if not(" " in s):
            return len(s)

        found = False
        count = 0
        
        for i in range(len(s)-1, 0, -1):
            if s[i] != " ":
                found = True
                count += 1
            if s[i] == " ":
                found = False
            if count > 0 and not found:
                return count

        return count