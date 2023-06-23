class Node:
    def __init__(self, key, item, p = None, left = None, right = None):
        self.list = []
        self.item = item
        self.key = key
        self.p = p
        self.left = left
        self.right = right

class ABR:
    def __init__(self):
        self.root = None
        self.length = 0

    def getHeight(self, node: Node):
        if node is None:
            return 0
        else:
            return 1 + max(self.getHeight(node.left), self.getHeight(node.right))

    def search(self, k: int) -> Node:
        # Cerca un nodo con chiave k nell'albero
        return self.__search(self.root, k)

    def __search(self, x: Node, k: int) -> Node:
        # Metodo ricorsivo che cerca un nodo con chiave k nell'albero
        if x is None or x.key == k:
            return x
        if k < x.key:
            return self.__search(x.left, k)
        else:
            return self.__search(x.right, k)

    def max(self, start_node: Node = None):
        # Restiruisce la chiave massima dell'albero
        x = start_node if start_node is not None else self.root
        while x.right is not None:
            x = x.right

        return x

    def min(self, start_node: Node = None):
        # Restituisce la chiave minima dell'albero
        x = start_node if start_node is not None else self.root
        while x.left is not None:
            x = x.left

        return x
    
    def tree_insert(self, key: int, item: int):
        # Inserisce un nodo con chiave k nell'albero
        z = Node(key, item)
        self.__tree_insert(z)

    def __tree_insert(self, z: Node):
        # Inserisce un nodo z all'interno dell'albero
        y = None
        x = self.root
        while x is not None:
            y = x
            if z.key == x.key:
                break
            elif z.key < x.key:
                x = x.left
            else:
                x = x.right

        z.p = y
        if y is None:
            self.root = z
        elif z.key == y.key:
            y.list.append(z)
        elif z.key < y.key:
            y.left = z
        else:
            y.right = z

        self.length += 1

    def transplant(self, u: Node, v: Node):
        # Sostituisce il nodo u con il nodo v
        if u.p is None:
            self.root = v
        elif u == u.p.left:
            u.p.left = v
        else:
            u.p.right = v
        if v is not None:
            v.p = u.p

    def tree_delete(self, z: Node):
        # Elimina il nodo z dall'albero
        if z.left is None:
            self.transplant(z, z.right)
        elif z.right is None:
            self.transplant(z, z.left)
        else:
            y = self.min(z.right)
            if y.p != z:
                self.transplant(y, y.right)
                y.right = z.right
                y.right.p = y
            self.transplant(z, y)
            y.left = z.left
            y.left.p = y

        self.length -= 1

    def tree_delete_key(self, key: int):
        z = self.search(key)
        if z is not None:
            self.tree_delete(z)