class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ''' Brute Force approach '''
        # res = 0
        # for i in range(len(prices)-1):
        #     for j in range(i + 1, len(prices)):
        #         res = max(prices[j] - prices[i],res)
        # return res

        ''' two pointers '''
        res = 0
        l, r = 0, 1
        profit = 0
        while r < len(prices):
            if prices[l] < prices[r]:
                profit = max(profit,prices[r]-prices[l])
            else:
                l = r
            r += 1
        return profit
    


                



