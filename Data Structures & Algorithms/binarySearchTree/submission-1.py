class TreeNode:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.left = None
        self.right = None

class TreeMap:
    
    def __init__(self):
        self.root = None

    def insert(self, key: int, val: int) -> None:
        node = TreeNode(key, val)
        
        if not self.root:
            self.root = node
            return

        cur = self.root
        while True:
            if key < cur.key:
                if not cur.left:
                    cur.left = node
                    return
                cur = cur.left
            elif key > cur.key:
                if not cur.right:
                    cur.right = node
                    return
                cur = cur.right
            else:
                cur.val = node.val
                return


    def get(self, key: int) -> int:
        cur = self.root

        while cur:
            if cur.key > key:
                cur = cur.left
            elif cur.key < key:
                cur = cur.right
            else:
                return cur.val

        return -1


    def getMin(self) -> int:
        if not self.root:
            return -1

        cur = self.root
        while cur and cur.left:
            cur = cur.left

        return cur.val



    def getMax(self) -> int:
        if not self.root:
            return -1

        cur = self.root
        while cur and cur.right:
            cur = cur.right

        return cur.val

    def findMin(self, root):
        cur = root
        while cur and cur.left:
            cur = cur.left

        return cur


    def remove(self, key: int) -> None:
        if not self.root:
            return
        self.root = self.removeHelper(self.root, key)


    def removeHelper(self, root, key):
        if not root:
            return 

        cur = root
        if key > root.key:
            cur.right = self.removeHelper(cur.right, key)
        elif key < root.key:
            cur.left = self.removeHelper(cur.left, key)
        else:
            if not cur.left:
                return cur.right
            elif not cur.right:
                return cur.left
            else:
                mini = self.findMin(root.right)
                cur.key = mini.key
                cur.val = mini.val
                root.right = self.removeHelper(root.right, mini.key)

        return root

            
    def getInorderKeys(self) -> List[int]:
        l = []
        self.inorderTrav(self.root, l)
        return l


    def inorderTrav(self, root, res):
        if not root:
            return

        cur = root
        if cur.left:
            self.inorderTrav(cur.left, res)
        res.append(cur.key)
        if cur.right:
            self.inorderTrav(cur.right, res)




