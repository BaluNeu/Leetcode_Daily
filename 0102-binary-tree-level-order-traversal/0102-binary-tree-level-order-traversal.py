# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        queue = collections.deque()

        result = []

        queue.append(root)

        while queue:

            level = []
            level_size = len(queue)

            for i in range(level_size):
                current = queue.popleft()

                if current:

                    level.append(current.val)
                    queue.append(current.left)
                    queue.append(current.right)

            if level:
                result.append(level)

        return result

            

        

        