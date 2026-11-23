class Solution:
    def tribonacci(self, n: int) -> int:
        a=0
        b=1
        c=1
        for i in range(n):
            d=a+b+c
            a=b
            b=c
            c=d
        return a
        