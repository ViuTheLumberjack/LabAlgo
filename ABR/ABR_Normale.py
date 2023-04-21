class Node:
    def __init__(self, key, parent = None, left = None, right = None):
        self.key = key
        self.parent = parent
        self.left = left
        self.right = right

class ABR:
    def __init__(self):
        self.root = None
        self.length = 0

    def inorder_tree_walk(self, node: Node):
        # Stampa in ordine crescente le chiavi dell'albero
        if node is not None:
            self.inorder_tree_walk(node.left)
            print(node.key)
            self.inorder_tree_walk(node.right)

    def preorder_tree_walk(self, node: Node):
        # Stampa le chiavi dell'albero in ordine di visita, prima il ramo sinistro, poi il ramo destro
        if node is not None:
            print(node.key)
            self.preorder_tree_walk(node.left)
            self.preorder_tree_walk(node.right)

    def postorder_tree_walk(self, node: Node):
        # Stampa le chiavi dell'albero in ordine decrescente
        if node is not None:
            self.postorder_tree_walk(node.left)
            self.postorder_tree_walk(node.right)
            print(node.key)

    def search(self, k: int) -> Node:
        # Cerca il primo nodo con chiave k nell'albero
        return self.__search(self.root, k)

    def __search(self, x: Node, k: int) -> Node:
        # Metodo ricorsivo che cerca un nodo con chiave k nell'albero
        if x is None or x.key == k:
            return x
        if k < x.key:
            return self.search(self, x.left, k)
        else:
            return self.search(self, x.right, k)

    def max(self):
        # Restiruisce la chiave massima dell'albero
        x = self.root
        while x is not None:
            x = x.right

        return x.key

    def min(self):
        # Restituisce la chiave minima dell'albero
        x = self.root
        while x is not None:
            x = x.left

        return x.key

    def tree_insert(self, z: Node):
        # Inserisce un nodo z all'interno dell'albero
        y = None
        x = self.root
        while x is not None:
            y = x
            if z.key < x.key:
                x = x.left
            else:
                x = x.right

        z.parent = y
        if y is None:
            self.root = z
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
            y = self.tree_minimum(z.right)
            if y.p != z:
                self.transplant(y, y.right)
                y.right = z.right
                y.right.p = y
            self.transplant(z, y)
            y.left = z.left
            y.left.p = y

        self.length -= 1