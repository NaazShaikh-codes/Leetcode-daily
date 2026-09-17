class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        count = 0

        def dfs(node):
            nonlocal count

            if node is None:
                return 0, 0

            left_size, left_sum = dfs(node.left)
            right_size, right_sum = dfs(node.right)

            size = 1 + left_size + right_size
            total = node.val + left_sum + right_sum

            if total // size == node.val:
                count += 1

            return size, total

        dfs(root)

        return count