class Solution:
    def isPalindrome(self, s: str):
        new = ""

        for i in s:
            if i.isalnum():
                new += i.lower()

        return new == new[::-1]
        