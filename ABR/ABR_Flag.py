class Node:
    def __init__(self, key, item, p = None, left = None, right = None):
        # con flag = False, l'inserimento viene effettuato nel sottoalbero sinistro, altrimenti nel sottoalbero destro
        self.flag = False
        self.item = item
        self.key = key
        self.p = p
        self.left = left
        self.right = right

class ABR:
    def __init__(self):
        self.root = None
        self.length = 0

    def __init__(self, values: list):
        self.root = None
        self.length = 0

        for value in values:
            self.tree_insert(value, chr(value))

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
            
    def getHeight(self, node: Node):
        if node is None:
            return 0
        else:
            return 1 + max(self.getHeight(node.left), self.getHeight(node.right))

    def search(self, k: int) -> Node:
        # Cerca il primo nodo con chiave k nell'albero
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
                # Cambio il flag
                x.flag = not x.flag
                # Controllo il flag con logica inversa per decidere se inserire il nodo nel sottoalbero sinistro o destro
                if not x.flag:
                    x = x.right
                else:
                    x = x.left
            elif z.key < x.key:
                x = x.left
            else:
                x = x.right

        z.p = y
        if y is None:
            self.root = z 
        elif z.key == y.key:
            # Controllo il flag per decidere se inserire il nodo nel sottoalbero sinistro o destro del padre
            if y.flag:
                y.right = z
            else:
                y.left = z
            # Cambio il flag
            y.flag = not y.flag
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
        self.__tree_delete_key(key, z)

    def __tree_delete_key(self, key: int, node: None) -> bool:
        # Elimina i nodo con chiave k dall'albero, per ini
        if node is None:
            return
        else:
            if node.flag:
                u = node.left
                v = node.right
            else:
                u = node.left
                v = node.right

            if u is not None and u.key == key:
                self.__tree_delete_key(key, u)
            if v is not None and v.key == key:
                self.__tree_delete_key(key, v)
            self.tree_delete(node)              