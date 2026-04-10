from bigtree import Node, print_tree


raiz = Node("Raiz")

hijo1 = Node("Hijo 1", parent=raiz)
hijo2 = Node("Hijo 2", parent=raiz)
hijo3 = Node("Hijo 3", parent=raiz)


hijo1_1 = Node("Hijo 1.1", parent=hijo1)
hijo1_2 = Node("Hijo 1.2", parent=hijo1)

hijo2_1 = Node("Hijo 2.1", parent=hijo2)

hijo3_1 = Node("Hijo 3.1", parent=hijo3)
hijo3_2 = Node("Hijo 3.2", parent=hijo3)
hijo3_3 = Node("Hijo 3.3", parent=hijo3)


print_tree(raiz)