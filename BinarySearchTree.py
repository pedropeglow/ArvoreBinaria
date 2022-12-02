from Node import Node

ROOT = 'root'
class BinarySearchTree: 
    def __init__(self):
        self.root = None
    
    #INSERT
    def insert(self, label):
        #cria um novo no
        node = Node(label) 

        #verifica se árvore está vazia, se sim - nó inserido é raiz
        if self.empty():
            self.root = node
        else: #senao, maos a obra 
            
            #- árvore não vazia - insere recursivamente

            #referencia do nodo pai
            dad_node = None
            current_node = self.root #comeca sempre da raiz

            while True: 

                # Primeira verificacao: currentnode != none (não é folha, nao estavazia) 
                    # -> deve continuar percorrendo 
                if current_node != None: 
                    # e atualizando a referencia do pai
                
                    dad_node = current_node

                    # Segunda Verificacao: verifica se vai para esquerda ou direita
                    if node.getLabel() < current_node.getLabel():
                        #vai para esquerda
                        current_node = current_node.getLeft()
                    else:
                        #vai para direita 
                        current_node = current_node.getRight()
                else:
                    #Terceira verificacao: se current node é none: então encontrou onde deve inserir 

                    #Quarta verificacao: depois de saber que deve inserir
                        # verifica  se vai ser inserido na esquerda ou na direita
                    if node.getLabel() < dad_node.getLabel():
                        dad_node.setLeft(node)
                    else:
                        dad_node.setRight(node)
                    
                    break #insercao realizada
    
    #VERIFICA SE ÁRVORE ESTÁ VAZIA
    def empty(self):
        # Raiz vazia: árvore vazia
        if self.root == None:
            return True
        else:
            return False

    #PEGA RAIZ DA ÁRVORE
    def getRoot(self):
        return self.root

    #PREORDER TRAVERSAL
    def showPreOrderTraversal(self, root):
        if root:
            print(root.getLabel())
            self.showPreOrderTraversal(root.getLeft())
            self.showPreOrderTraversal(root.getRight())
    
    #INORDER TRAVERSAL
    def showInOrderTraversal(self, node=None):
         if node != None:
              self.showInOrderTraversal(node.getLeft())
              print(node.getLabel(),end=" " + "\n")
              self.showInOrderTraversal(node.getRight())
    
    #POSTORDER TRAVERSAL
    def showPostOrderTraversal(self, root):
        if root:
            self.showPostOrderTraversal(root.getLeft())
            self.showPostOrderTraversal(root.getRight())
            print(root.getLabel())

    #SHOW TREE PREORDER
    def showTreePre(self, parent, current_node):
        if current_node != None:
            if parent != current_node:
                print('%d' % parent.getLabel(), "->", '%d' % current_node.getLabel())
            self.showTreePre(current_node, current_node.getLeft())
            self.showTreePre(current_node, current_node.getRight())

    def showTreePos(self, node=None):
        if node is None:
            node = self.root
        if node.getLeft():
            self.showTreePos(node.getLeft())
        if node.getRight():
            self.showTreePos(node.getRight())
        print(node.getLabel(), ' -> ', end=" ")

    

    # METODO DE BUSCA AUXILIAR
    def search_aux(self, node, label):

        if node.getLabel() == label:
            return node
        else:
            if node.getLabel() < label and node.getRight() is not None:
                node_search = self.search_aux(node.getRight(), label)
                if node_search is not None:
                    return node_search

            if node.getLabel() > label and node.getLeft() is not None:
                node_search = self.search_aux(node.getLeft(), label)
                if node_search is not None:
                    return node_search

        return None

    ### MÉTODO DE BUSCA
    def search(self, label):
        if self.empty():
            return "Empty Tree"
        else:
            node_busca = self.search_aux(self.root, label)
            if node_busca is None:
                return "Node not found"
            return node_busca
    '''
        Caso 1: nó a ser inserido nao tem filhos. Caso simples, basta setar a ligacao do pai para NONE
        
        Caso 2: nó a ser removido tem somente 1 filho. Basta colocar o seu filho no lugar dele

        Caso 3: nó a ser removido possui dois filhos, basta pegar o menor elemento da subarvore a direita e substituir

    '''
     # Encontrando o MAIOR e o MENOR elemento numa ÁRVORE Binária de Busca
    def min(self, node=ROOT):
        if node == ROOT:
            node = self.root
        while node.left:
            node = node.left
        return node.label

    # MÉTODO DE REMOÇÃO
    def remove(self, value, node=ROOT):
        if node == ROOT:
            node = self.root
        if node is None:
            return node
        if value < node.label:
            node.left = self.remove(value, node.left)
        elif value > node.label:
            node.right = self.remove(value, node.right)
        else:
            # CASO 1
            if node.left is None and node.right is None:
                return None
            # Caso 2
            if node.left is None:
                return node.right
            # Caso 2
            elif node.right is None:
                return node.left
            else:
                # Caso 3
                substituto = self.min(node.right)
                node.label = substituto
                node.right = self.remove(substituto, node.right)
        return node

    def altura(self, label):
          if label == None or label.getLeft() == None and label.getRight() == None:
               return 0
          else:
             if self.altura(label.getLeft()) > self.altura(label.getRight()):
                return  1 + self.altura(label.getLeft()) 
             else:
                return  1 + self.altura(label.getRight()) 
        