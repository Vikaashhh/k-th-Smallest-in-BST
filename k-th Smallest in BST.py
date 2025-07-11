'''
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None
'''

class Solution:
    # Return the kth smallest element in the given BST 
    def kthSmallest(self, root, k): 
        self.count = 0              # Kitne nodes visit kiye hain
        self.result = -1            # Result store karne ke liye

        def inorder(node):
            if node is None or self.count >= k:
                return
            
            # Left subtree
            inorder(node.left)
            
            # Node process karo
            self.count += 1
            if self.count == k:
                self.result = node.data
                return
            
            # Right subtree
            inorder(node.right)  # ✅ Corrected this line
        
        inorder(root)
        return self.result
