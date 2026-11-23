
from typing import List

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        ans = []

        if len(p) > len(s):
            return ans

        p_count = [0] * 26
        s_count = [0] * 26

        for ch in p:
            p_count[ord(ch) - ord('a')] += 1

        k = len(p)

        for i in range(len(s)):
            s_count[ord(s[i]) - ord('a')] += 1

            if i >= k:
                s_count[ord(s[i-k]) - ord('a')] -= 1

            if s_count == p_count:
                ans.append(i - k + 1)

        return ans
