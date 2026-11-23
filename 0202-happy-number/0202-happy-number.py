class Solution:
    def isHappy(self, n: int) -> bool:

        visited = set()

        while n != 1:

            if n in visited:
                return False

            visited.add(n)

            sum = 0

            while n > 0:
                rem = n % 10
                sum = sum + rem * rem
                n = n // 10

            n = sum

        return True