class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)

        result = right

        while left <= right:
            hours = 0
            mid = (left + right)//2

            for p in piles:
                hours += math.ceil(p/mid)
            
            if hours > h:
                
                left = mid + 1
            else:
                result = min(result,mid)
                right = mid - 1

        return result


            








        