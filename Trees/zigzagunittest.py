import unittest
from Trees.ZigzagTraversal import Solution, TreeNode

class TestZigzagLevelOrder(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_empty_tree(self):
        self.assertEqual(self.solution.zigzagLevelOrder(None), [])

    def test_single_node_tree(self):
        root = TreeNode(1)
        self.assertEqual(self.solution.zigzagLevelOrder(root), [[1]])

    def test_two_level_tree(self):
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        self.assertEqual(self.solution.zigzagLevelOrder(root), [[1], [3, 2]])

    def test_three_level_tree(self):
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        root.left.left = TreeNode(4)
        root.left.right = TreeNode(5)
        root.right.left = TreeNode(6)
        root.right.right = TreeNode(7)
        self.assertEqual(self.solution.zigzagLevelOrder(root), [[1], [3, 2], [4, 5, 6, 7]])

    def test_unbalanced_tree(self):
        root = TreeNode(1)
        root.right = TreeNode(2)
        root.right.right = TreeNode(3)
        self.assertEqual(self.solution.zigzagLevelOrder(root), [[1], [2], [3]])

if __name__ == "__main__":
    unittest.main()