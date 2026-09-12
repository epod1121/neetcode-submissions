class Solution:
    def isPalindrome(self, s: str) -> bool:

        import re

        clean = re.sub(r'[^a-zA-Z0-9]', '', s)
        
        lowered = clean.lower()

        if lowered == lowered[::-1]:
            return True

        return False