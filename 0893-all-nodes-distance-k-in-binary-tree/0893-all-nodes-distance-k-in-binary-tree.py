from collections import deque

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        # Function to add parent pointers
        def addParents(node, parent=None):
            if node:
                node.parent = parent
                addParents(node.left, node)
                addParents(node.right, node)

        # Add parent pointers to each node
        addParents(root)

        # BFS starting from target node
        queue = deque([(target, 0)])
        seen = {target}
        while queue:
            if queue[0][1] == k:
                return [node.val for node, d in queue]
            node, d = queue.popleft()
            for neighbor in (node.left, node.right, node.parent):
                if neighbor and neighbor not in seen:
                    seen.add(neighbor)
                    queue.append((neighbor, d + 1))

        return []

# Example usage
# Assuming TreeNode class is defined elsewhere as per your existing code
# solution = Solution()
# root, target, k = [construct your tree and target node here]
# print(solution.distanceK(root, target, k))
