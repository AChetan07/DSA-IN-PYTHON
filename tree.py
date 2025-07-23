#  trees have root node  and graphs do not and graphs are cyclic in nature
# 
# 
# /* tree data structure   \*
#  tree is a non linear data structure that consists of nodes connected by edges

# it is a hierarchical structure with a root node and child nodes

# each node can have zero or more child nodes.The top node is called root node,the nodes with no children are called leaf nodes

# the tree is a recursive data structure, meaning that each node can be considered a tree itself.

# the tree is a widely used data structure in cs and it is used in various apllication such as file systems,databases and network routing.

# The tree is a versatile data structure that can be used to  represent    hierarchical relationships between data elements.

# it is powerful data structure that cab ve used to solbe complex problems in a simple and efficient way

# There are many types in trees such as binary trees ,binary seaarch trees,avl trees,red-black trees,b-trees and heaps

#readable format
class Node:
    def __init__(self,value):
        self.value=value
        self.children=[]

    def add_child(self,child_node):
        self.children.append(child_node)
    def remove_child(self,child_node):
        self.children.remove(child_node)

#using recursion

class Node:
      def __init__(self,value):
        self.value=value
        self.left=None
        self.right=None
      def insert(self,root):
        if root is None:
            return Node(self.value)
        if self.value<root.value:
            root.left=self.insert(root.left)
        else:
            root.right=self.insert(root.right)
        return root
      def deletion(self,root,value):
          if self is None:
              return self
          if value < root.value:
              root.left=self.deletion(root.left,value)
          elif value > root.value:
              root.right = self.deletion(root.right,value)
          else:
              if root.left is None:
                  return root.right
              elif root.right is None:
                  return root.left
              temp=self.min_value_node(root.right)
              root.value=temp.value
              root.right=self.deletion(root.right,temp.value)

              

      def inorder_traversal(self,root):
          if root:
               self.inorder_traversal(root.left)
               print(root.value,end="")
               self.inorder_traversal(root.right)
      def preorder_traversal(self,root):
          if root:
              print(root.value,end="")
              self.preorder_traversal(root.left)
              self.preorder_traversal(root.right)
                        
          











