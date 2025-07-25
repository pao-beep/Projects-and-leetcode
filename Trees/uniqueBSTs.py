# Definition for a binary tree node.
from typing import Dict, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        if n == 0:
            return []
        return self.generate_trees(1, n)
    
    def generate_trees(self, start, end):
        if start > end:
            return [None]
        all_trees = []
        for i in range(start, end + 1):
            left_trees = self.generate_trees(start, i - 1) #start doesn't change
            right_trees = self.generate_trees(i + 1, end) #end doesn't change
            for l in left_trees:
                for r in right_trees:
                    current_tree = TreeNode(i)
                    current_tree.left = l
                    current_tree.right = r 
                    all_trees.append(current_tree)
        return all_trees
    

#redo
class UniqueBSTsMemo:


    def __init__(self):
        pass

    def generateTress(self, n: int):
        if n == 0 :
            return []
        self.memo: Dict[tuple, List[TreeNode]] = {}
        return self.generate_trees(1,n)
    
    def generate_trees(self,start,end):
        if (start,end) in self.memo:
            return self.memo[(start,end)]

        if start > end:
            return [None]
        all_trees = []
            # Generate left and right subtrees recursively
        for i in range(start, end +1):
            left_subtree = self.generate_trees(start,i-1)
            right_subtree = self.generate_trees(i+1,end)
# Combine left and right subtrees with the current root
            for k in left_subtree:
                for j in right_subtree:
                    current_node = TreeNode(i)
                    current_node.left = left_subtree
                    current_node.right = right_subtree
                    all_trees.append(current_node)
        # Store the result in the memoization dictionary
        self.memo[(start,end)] = all_trees
        return all_trees