class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        count = {}
        ans = 0

        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                product = nums[i] * nums[j]

                if product in count:
                    ans += count[product] * 8

                count[product] = count.get(product, 0) + 1

        return ans