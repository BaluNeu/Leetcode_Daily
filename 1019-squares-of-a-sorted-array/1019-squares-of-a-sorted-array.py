class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
    
        result = []
    
        i,j = 0,len(nums)-1

        while i<=j:
        
            if nums[i]*nums[i] >= nums[j]*nums[j]:
                result.append(nums[i]*nums[i])
                i+=1
            
            else:
                result.append(nums[j]*nums[j])
                j-=1
            
        return result[::-1]