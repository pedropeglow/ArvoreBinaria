from BinarySearchTree import BinarySearchTree

def menu():
    print("""Escolha a opção desejada:
        [0] - Close Program
        [1] - Insert an element in Binary Tree
        [2] - Remove an element in Binary Tree
        [3] - Tree Traversals Preorder
        [4] - Tree Traversals Inorder
        [5] - Tree Traversals Postorder
        [6] - Show Tree Pre
        [7] - Show Tree Pos
        [8] - Search an element in Binary Tree
        [9] - Tree Height
        ************************************""")
    return input()

tree = BinarySearchTree()

while True:
    answer = menu()

    if answer == "0":
        print("Finished program")
        exit()

    elif answer == "1":
        print("-"*20)
        insert_element = input("Type an element: ")
        print("-"*20)
        if insert_element.isdigit():
            tree.insert(int(insert_element))
            print('\033[42m' + "Node inserted successfully!" + '\033[0;0m')
            print('-'*20)
        else:
            print('\033[41m' + "Type a valid number" + '\033[0;0m')

    elif answer == "2":
        print("-"*20)
        element = input("Type an element: ")
        print("-"*20)
        try:
            tree.remove(int(element))
            print('\033[42m' + "Node removed successfully!" + '\033[0;0m')
            print('-'*20)
        except ValueError as e:
            print('\033[41m' + "Type a valid number" + '\033[0;0m')

    elif answer == "3":
        print("*"*20 + '\033[43m' + " Preorder Traversal " + '\033[0;0m' + "*"*20)
        tree.showPreOrderTraversal(tree.getRoot())
    
    elif answer == "4":
        print("*"*20 + '\033[43m' + " Inorder Traversal "  + '\033[0;0m' + "*"*20)
        tree.showInOrderTraversal(tree.getRoot())

    elif answer == "5":
        print("*"*20 + '\033[43m' " Postorder Traversal "  + '\033[0;0m' + "*"*20)
        tree.showPostOrderTraversal(tree.getRoot())

    elif answer == "6":
        print("*"*20 + '\033[44m' + " Tree Pre Order " + '\033[0;0m' + "*"*20)
        tree.showTreePre(tree.getRoot(), tree.getRoot())

    elif answer == "7":
        print("*"*20 + '\033[44m' + " Tree Pos Order " + '\033[0;0m' + "*"*20)
        tree.showTreePos(tree.getRoot())

    elif answer == "8":
        print("-"*20)
        search_element = input("Type an element: ")
        print("-"*20)
        if search_element.isdigit():
            node = tree.search(int(search_element))
            if node is None:
                print("Element does not exist")
            else:
                print(f"Found node address: {node}")
                print("-"*20)
        else:
            print('\033[41m' + "Type a valid number" + '\033[0;0m')

    elif answer == "9":
        print("Tree Height: ", tree.altura(tree.getRoot()))

    else:
        print("ERROR! Enter a menu option")