class Solution:
    def findTheDifference(self, s, t):
        for ch in t:
            if t.count(ch) != s.count(ch):
                return ch