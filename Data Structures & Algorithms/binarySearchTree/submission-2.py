class TreeMap:
    
    def __init__(self):
        self.root = None

    def insert(self, key: int, val: int) -> None:
        if not self.root:
            self.root = TreeNode(key, val)
            return
        cn = self.root
        while cn:
            if cn.key == key:
                cn.value = val
                return
            if key > cn.key:
                if cn.right:
                    cn = cn.right
                else:
                    cn.right = TreeNode(key, val)
                    return
            else:
                if cn.left:
                    cn = cn.left
                else:
                    cn.left = TreeNode(key, val)
                    return

    def get(self, key: int) -> int:
        curr_node = self.root
        while curr_node:
            if curr_node.key == key:
                return curr_node.value
            if key < curr_node.key:
                curr_node = curr_node.left
            else:
                curr_node = curr_node.right
        return -1

    def getMin(self) -> int:
        cn = self.root
        if not cn:
            return -1
        while cn.left:
            cn = cn.left
        return cn.value


    def getMax(self) -> int:
        cn = self.root
        if not cn:
            return -1
        while cn.right:
            cn = cn.right
        return cn.value


    def remove(self, key: int) -> None:
        def findMin(node):
            while node.left:
                node = node.left
            return node

        def _remove(node, key):
            if not node:
                return None
            if key < node.key:
                node.left = _remove(node.left, key)
            elif key > node.key:
                node.right = _remove(node.right, key)
            else:
                if not node.left:
                    return node.right
                if not node.right:
                    return node.left
                
                temp = findMin(node.right)
                node.key = temp.key
                node.value = temp.value
                node.right = _remove(node.right, temp.key)
            return node
        
        self.root = _remove(self.root, key)

    def getInorderKeys(self) -> List[int]:
        def dfs(node, res):
            if not node:
                return
            dfs(node.left, res)
            res.append(node.key)
            dfs(node.right, res)

        res = []
        dfs(self.root, res)
        return res


class TreeNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.right = None
        self.left = None