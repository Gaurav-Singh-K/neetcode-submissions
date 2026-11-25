class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        ct = "".join(char for char in s if char.isalnum())

        for i in range(len(ct)//2):
            if ct[i] != ct[len(ct)-i-1]:
                return False
        return True
        