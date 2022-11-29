from BinarySearchTree import BinarySearchTree

def menu():
    print("""Escolha a opção desejada:
        0 - Close Program
        1 - Insert an element in Binary Tree
        2 - Search an element in Binary Tree
        3 - Remove an element in Binary Tree
        4 - Show Tree
        5 - Tree Height
        ************************************""")
    return input()

#Instanciando a Classe
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
        else:
            print("Type a valid number")

    elif answer == "2":
        print("-"*20)
        search_element = input("Type an element: ")
        print("-"*20)
        if search_element.isdigit():
            node = tree.search(int(search_element))
            if node is None:
                print("Element does not exist")
            else:
                print(node)
        else:
            print("Type a valid number")
        
    
    elif answer == "3":
        element = input("Type an element: ")
        try:
            tree.removeNovo(int(element))
        except ValueError as e:
            print("Type a valid number")


    elif answer == "4":
        tree.showTree(tree.getRoot(), tree.getRoot())

    elif answer == "5":
        print("Altura da árvore: ", tree.altura(tree.getRoot()))

    
    else:
        print("ERROR! Enter a menu option")