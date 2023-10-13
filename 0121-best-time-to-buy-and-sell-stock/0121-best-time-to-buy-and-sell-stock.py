class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        j = 1
        i = 0

        max_profit = 0

        while j < len(prices):

            if prices[j] > prices[i]:
                profit = prices[j] - prices[i]

                max_profit = max(max_profit, profit)

            else:
                i = j
            j+=1
        return max_profit
            
        

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
