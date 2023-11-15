class Node: 
    def __init__(self, item):
        if not isinstance(item, (int, float, str)):
            raise TypeError("Item must be numeric (int or float).")
        self.right = None
        self.left = None
        self.item = item
    
    """retorna o item como uma string para visualizar e não o espaço de memoria"""
    def __str__(self) -> str:
        return str(self.item)


class BinaryTree:
    def __init__(self, item=None):
        if item:
            node = Node(item)
            self.root = node
        self.root = None

    def symmetrical_route(self, node=None):
        if node == None:
            node = self.root

        if node.left:
            print('(', end='')
            self.symmetrical_route(node.left)
            """ 'end' attribute to break line """
        print(node, end='')

        if node.right:
            self.symmetrical_route(node.right)
            print(')', end='')

            #      '+'
            #    /     \
            #  'a'      '*'
            #          /   \
            #        'b'    '-'
            #              /    \
            #            '/'    'e' 
            #           /   \
            #         'c'   'd'

            # (a + (b * ((c/d) - e)))

if __name__ == "__main__":
    # tree = BinaryTree(7)
    # tree.root.left = Node(14)
    # tree.root.right = Node(18)

    # print(tree.root)
    # print(tree.root.left)
    # print(tree.root.right)

    tree = BinaryTree()
    n1 = Node('a')
    n2 = Node('+')
    n3 = Node('*')
    n4 = Node('b')
    n5 = Node('-')
    n6 = Node('/')
    n7 = Node('c')
    n8 = Node('d')
    n9 = Node('e')

    n6.left = n7
    n6.right = n8
    n5.left = n6
    n5.right = n9
    n3.left = n4
    n3.right = n5
    n2.left = n1
    n2.right = n3
    tree.root = n2

    tree.symmetrical_route()
    print(end='')
     
