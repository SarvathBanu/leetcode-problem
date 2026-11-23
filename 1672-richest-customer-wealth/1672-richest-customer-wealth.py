class Solution:
    def maximumWealth(self, accounts):
        max_money = 0

        for customer in accounts:
            total = 0

            for money in customer:
                total += money

            if total > max_money:
                max_money = total

        return max_money