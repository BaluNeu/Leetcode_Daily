class Solution:
    def maxArea(self, height: List[int]) -> int:

        i = 0 
        j = len(height) - 1
        max_area = 0

        while i < j:

            if height[i] < height[j]:
                area = height[i]*(abs(j-i))
                i+=1
            else:
                area = height[j]*(abs(j-i))
                j-=1

            max_area = max(max_area,area)
        return max_area
            















        # max_area = 0

        # for i in range(0,len(height)):

        #     for j in range(i,len(height)):

        #         if height[i] > height[j]:
        #             area = height[j]*(abs(j-i))
                    
        #         else:
        #             area = height[i]*(abs(j-i))

        #         max_area = max(max_area,area)

        # return max_area


                
                    
        