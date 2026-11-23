class Solution:
    def sumOfUnique(self, nums):
        ans = 0
        
        for i in nums:
            if nums.count(i) == 1:
                ans += i
                
        return ans