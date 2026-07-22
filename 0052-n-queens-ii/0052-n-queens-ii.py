class Solution:
    def totalNQueens(self, n: int) -> int:
        col = set()
        d1 = set()
        d2 = set()

        def solve(r):
            if r == n:
                return 1

            count = 0
            for c in range(n):
                if c in col or r-c in d1 or r+c in d2:
                    continue

                col.add(c)
                d1.add(r-c)
                d2.add(r+c)

                count += solve(r+1)

                col.remove(c)
                d1.remove(r-c)
                d2.remove(r+c)

            return count

        return solve(0)