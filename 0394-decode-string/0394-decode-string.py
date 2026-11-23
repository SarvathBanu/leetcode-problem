class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        num = 0
        cur = ""

        for ch in s:
            if ch.isdigit():
                num = num * 10 + int(ch)
            elif ch == "[":
                stack.append((cur, num))
                cur = ""
                num = 0
            elif ch == "]":
                prev, k = stack.pop()
                cur = prev + cur * k
            else:
                cur += ch

        return cur