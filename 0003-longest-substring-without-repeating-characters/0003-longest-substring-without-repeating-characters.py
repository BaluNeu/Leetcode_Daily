class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        hash_set = set()
        # j = 1
        size = 0
        i=0
        
        for j in range(0,len(s)):
            while s[j] in hash_set:
                hash_set.remove(s[i])
                i+=1
            hash_set.add(s[j])
            size = max(size, j-i+1)
        
        return size
        
                
                
                
        
        
        
        
        
        
        

        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         i = 0
#         j = 1
#         count = 1
        
#         s_list = list(s)
        
#         hash_map = {s_list[0]}
        
#         while i < len(s_list):
#             if s_list[j] not in hash_map:
#                 hash_map.add(s_list[j])
#                 j+=1
                
                
#             else:
#                 i+=1
#                 j+=1
                
#             return len(hash_map)
            

        