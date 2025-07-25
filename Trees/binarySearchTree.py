class Node:

    def __init__(self,data):
        self.data = data
        self.height = 0
        self.lhsNode = None
        self.rhsNode= None


class BinarySearchTree:

    def __init__(self, node):
        self.root = node

    def insertRHSTree(self,root,node):
        if node.data > self.root.data and self.root.rhsNode is None:
            self.root.rhsNode = node
            return None
        elif node.data < self.root.data and self.root.lhsNode is not None:
            return self.root.lhsNode
        else:
            self.insertRHSTree(self.root.rhsNode, node)

    def insertLHSTree(self,root,node):
        if node.data < self.root.data and self.root.lhsNode is None:
            self.root.lhsNode = node
            return None
        elif node.data > self.root.data and self.root.rhsNode is not None:
            return self.root.rhsNode
        elif self.root.lhsNode is not None:
            self.insertLHSTree(self.root.lhsNode, node)

    def insertTree(self,root, node):
        if node is not None:
            s_node =self.insertLHSTree(root.next,node)
            s_node =self.insertRHSTree(s_node, node)

            return self.insertTree(s_node,node)


    def search(self, root, node):
        if root is None:
            return None
        if node.data == root.data:
            return root

        if node.data < root.data:
           return self.search(root.lhsNode, node)
        if node.data > root.data:
            return self.search(root.rhsNode, node)

    def delete(self,root,node):
        if root is None:
            return None
        if node.data == root.lhsNode.data:
            root.lhsNode = root.lhsNode.rhsNode
            self.insertLHSTree(root,root.lhsNode.lhsNode)
        if node.data == root.rhsNode.data:
            root.rhsNode = root.rhsNode.lhsNode
            self.insertRHSTree(root,root.rhsNode.rhsNode)
        if node.data < root.lhsNode.data:
            self.delete(root.lhsNode,node)
        if node.data > root.rhsNode.data:
            self.delete(root.rhsNode,node)
        return None


root = None
root = insert(root, 8)
root = insert(root, 3)
root = insert(root, 1)
root = insert(root, 6)
root = insert(root, 7)
root = insert(root, 10)
root = insert(root, 14)
root = insert(root, 4)

print("Inorder traversal: ", end=' ')
inorder(root)

print("\nDelete 10")
root = deleteNode(root, 10)
print("Inorder traversal: ", end=' ')
inorder(root)



