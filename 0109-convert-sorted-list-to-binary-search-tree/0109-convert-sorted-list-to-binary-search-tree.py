# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def sortedListToBST(self, head):
        if not head:
            return None

        values = []
        while head:
            values.append(head.val)
            head = head.next

        def build(left, right):
            if left > right:
                return None

            mid = (left + right) // 2

            root = TreeNode(values[mid])

            root.left = build(left, mid - 1)
            root.right = build(mid + 1, right)

            return root

        return build(0, len(values) - 1)

    