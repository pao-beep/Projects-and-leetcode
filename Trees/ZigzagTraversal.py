from collections import deque
from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        result = []
        queue = deque([root])
        left_to_right = True
        
        while queue:
            level_size = len(queue)
            current_level = deque()
            
            for _ in range(level_size):
                node = queue.popleft()
                
                if left_to_right:
                    current_level.append(node.val)
                else:
                    current_level.appendleft(node.val)
                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            result.append(list(current_level))
            left_to_right = not left_to_right
        
        return result
    
soln = Solution()
tree = TreeNode(1)
tree.left = TreeNode(2)
tree.right = TreeNode(3)
tree.left.left = TreeNode(4)
tree.left.right = TreeNode(5)
tree.right.left = TreeNode(6)
tree.right.right = TreeNode(7)
tree.left.left.left = TreeNode(8)
tree.left.right.left = TreeNode(9)
print(soln.zigzagLevelOrder(tree))  # Output: [[1], [3, 2], [4, 5, 6, 7], [8, 9]]
# This code defines a binary tree and implements a zigzag level order traversal.
# Example Usage
#give a complex example tree


##redo
from collections import deque
from typing import List, Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    

class ZigZag:
    def __init__(self, root: Optional[TreeNode]):
        self.root = root

    def zigzagTraversal(self, root):
        if not root:
            return
        result = []
        queue = deque(root)
        left_to_right = True # right for true left for false
        while queue:
            level_szie = len(queue)
            current_level = deque()
            
            for i in range(level_szie):
                node = queue.popleft
                if left_to_right:
                    current_level.append(node.val)
                    
                else:
                    current_level.appendLeft(node.right)
                   
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            result.append(list(current_level))
            left_to_right = not left_to_right


    