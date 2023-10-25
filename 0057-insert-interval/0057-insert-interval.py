class Solution(object):
    def insert(self, intervals, new_interval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        if not intervals:
            return [new_interval]
    
        result = []
        i = 0
    
    # add intervals that comes before new_interval 
    
        while i < len(intervals) and intervals[i][1] < new_interval[0]:
            result.append(intervals[i])
            i+=1
    
    
    # merge overlapping intervals with new_interval
    
        while i < len(intervals) and intervals[i][0] <= new_interval[1]:
            new_interval[0] = min(intervals[i][0], new_interval[0])
            new_interval[1] = max(intervals[i][1], new_interval[1])
            i+=1
        result.append(new_interval)
    
    # append remaining intervals to the result
    
        while i< len(intervals):
            result.append(intervals[i])
        
            i+=1
        
        
        return result
            
    
    
    
    
                    
                    
        