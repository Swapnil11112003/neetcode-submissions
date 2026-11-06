# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        d = {}
        def bfs(root):
            q = deque()
            if root:
                q.append(root)
            level = 0
            while len(q) > 0:
                level += 1
                for i in range(len(q)):
                    node = q.popleft()
                    if level in d:
                        d[level].append(node.val)
                    else:
                        d[level] = [node.val]
                    if node.left:
                        q.append(node.left)
                    if node.right:
                        q.append(node.right)
        bfs(root)

        for key, val in d.items():
            res.append(val[-1])

        return res

        