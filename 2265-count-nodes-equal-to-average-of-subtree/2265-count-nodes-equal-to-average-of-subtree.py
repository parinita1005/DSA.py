# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root):
        
        self.count = 0
        
        def dfs(node):
            # Base case
            if not node:
                return 0, 0   # sum, number of nodes
            
            # Get sum and count from left subtree
            left_sum, left_count = dfs(node.left)
            
            # Get sum and count from right subtree
            right_sum, right_count = dfs(node.right)
            
            # Total sum and nodes in current subtree
            total_sum = left_sum + right_sum + node.val
            total_count = left_count + right_count + 1
            
            # Average rounded down
            average = total_sum // total_count
            
            # Check if current node equals subtree average
            if node.val == average:
                self.count += 1
            
            return total_sum, total_count
        
        dfs(root)
        return self.count
        