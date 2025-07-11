# 🌿 Day 90 — GFG 160 Days DSA Challenge
### 📌 Problem: k-th Smallest Element in BST
### 📋 Problem Statement:
Given a Binary Search Tree (BST) and an integer k, return the k-th smallest element in the tree.
A classic example of leveraging BST's in-order traversal to retrieve nodes in sorted order.

## 🧠 Approach Explained:
🔹 Utilized recursive in-order traversal
🔹 Maintained a global counter to track how many nodes have been visited
🔹 As soon as count == k, recorded the node’s value as the result and terminated recursion early
🔹 The beauty of BST: In-order traversal = Sorted node access ✅

## 💻 Code Insight:
if self.count == k:
    self.result = node.data
    return
This condition enables an early exit as soon as we reach the desired k-th smallest node—efficient and elegant!

## 📊 Output Snapshot:
✅ Test Cases Passed: 1111 / 1111

⚡ Time Taken: 0.12 sec

🏆 Accuracy: 100%

🎯 Score: 4 / 4

📈 Total Score: 345

## 🪄 Key Takeaway:
“In a BST, structure gives rise to order. And order brings predictability.” 🌿

## 🔖 Hashtags:
#gfg160 #geekstreak2025 #Day90
#Python #DSA #BinarySearchTree
#1001DaysOfCode #Programming
#InOrderTraversal #framesbyvikash
