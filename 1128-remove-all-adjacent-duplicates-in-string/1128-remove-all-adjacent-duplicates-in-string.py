class Solution:
    def removeDuplicates(self, s: str) -> str:
        char_stack = []
    
        for char in s:

            if char_stack and char_stack[-1] == char:
                char_stack.pop()
        
            else:
                char_stack.append(char)

        return "".join(char_stack)
        