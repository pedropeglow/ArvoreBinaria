from BinarySearchTree import BinarySearchTree

def menu():
    print("""Escolha a opção desejada:
        [0] - Close Program
        [1] - Insert an element in Binary Tree
        [2] - Remove an element in Binary Tree
        [3] - Show Tree Pre
        [4] - Show Tree In Order
        [5] - Show Tree Pos
        [6] - Search an element in Binary Tree
        [7] - Tree Height
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
            print("Node inserted successfully!")
            print('-'*20)
        else:
            print("Type a valid number")

    elif answer == "2":
        element = input("Type an element: ")
        try:
            tree.remove(int(element))
        except ValueError as e:
            print("Type a valid number")
    
    elif answer == "3":
        print("*"*20 + " Tree Pre Order "  + "*"*20)
        tree.showTreePre(tree.getRoot(), tree.getRoot())

    elif answer == "4":
        print("*"*20 + " Tree InOrder "  + "*"*20)
        tree.showTreeInOrder(tree.getRoot())

    elif answer == "5":
        print("*"*20 + " Tree Pos Order "  + "*"*20)
        tree.showTreePos(tree.getRoot())

    elif answer == "6":
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
            print("Type a valid number")

    elif answer == "7":
        print("Tree Height: ", tree.altura(tree.getRoot()))

    else:
        print("ERROR! Enter a menu option")