from Node import Node

ROOT = 'root'
class BinarySearchTree: 
    def __init__(self):
        self.root = None
    
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

    def empty(self):
        # Raiz vazia: árvore vazia
        if self.root == None:
            return True
        else:
            return False 

    def showTree(self, parent, current_node):
        if current_node != None:
            if parent != current_node:
                print('%d' % parent.getLabel(), "->", '%d' % current_node.getLabel())
            self.showTree(current_node, current_node.getLeft())
            self.showTree(current_node, current_node.getRight())

    #pega raiz
    def getRoot(self):
        return self.root 

    #remover nodo
    '''
        Caso 1: nó a ser inserido nao tem filhos. Caso simples, basta setar a ligacao do pai para NONE
        
        Caso 2: nó a ser removido tem somente 1 filho. Basta colocar o seu filho no lugar dele

        Caso 3: nó a ser removido possui dois filhos, basta pegar o menor elemento da subarvore a direita e substituir

    '''

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

        # verifica se a arvore esta vazia antes de iniciar a busca
        if self.empty():
            return "Empty Tree"
        else:
            # arvore nao esta vazia - inicia a busca
            node_busca = self.search_aux(self.root, label)
            if node_busca is None:
                return "Node not found"
            return node_busca

      # MÉTODO DE AUXÍLIO PARA EXCLUIR NODO, PROCURANDO O NÓ MAIS A DIREITA
    def aux_nodo(self, parent, node):

        # Verifica se o nodo a direita existe e de forma recursiva caminha para direita.
        if node.getRight() is not None:
            node = self.aux_nodo(node, node.getRight())
        else:
            parent.setRight(None)

        return node

    # MÉTODO DE REMOÇÃO AUXILIAR
    def remove_aux(self, parent_node, node, label):
        if node.getLabel() == label:
            # Folha - Faz a verificação se o nodo da esquerda e o nodo da direita é NONE
            if node.getLeft() is None and node.getRight() is None:
                # Verifica se é filho da esquerda ou da direita
                if parent_node.getLabel() < label:
                    parent_node.setRight(None) # Se for filho a direita do pai
                else:
                    parent_node.setLeft(None) # Se for filho a esquerda do pai

            # 1 filho a direita
            # Se possui um filho a direita, irá substituir pela subÁrvore a esquerda
            if node.getLeft() is None and node.getRight() is not None:
                if parent_node.getLabel() < node.getLabel():
                    parent_node.setRight(node.getRight()) # Se for filho a direita do pai
                else:
                    parent_node.setLeft(node.getRight()) # Se for filho a esquerda do pai

            # 1 filho a esquerda
            # Se possui um filho a esquerda, irá substituir pela subÁrvore a direita
            if node.getLeft() is not None and node.getRight() is None:
                if parent_node.getLabel() < node.getLabel():
                    parent_node.setRight(node.getLeft())
                else:
                    parent_node.setLeft(node.getLeft())

            # Se possui 2 filhos
            if node.getLeft() is not None and node.getRight() is not None:
            
            # Precisamos encontrar um substituto para o nodo que estamos removendo, e seu substituto ideal é seu SUCESSOR dentro desta árvore

                if node.getLeft().getRight() is None:
                    nodo_aux = node.getLeft()
                    nodo_aux.setRight(node.getRight())

                else:
                    nodo_aux = self.aux_nodo(node, node.getLeft())
                    nodo_aux.setRight(node.getRight())
                    if nodo_aux.getLeft() is not None:
                        node.getLeft().setRight(nodo_aux.getLeft())
                        nodo_aux.setLeft(node.getLeft())
                    else:
                        nodo_aux.setLeft(node.getLeft())

                if parent_node.getLabel() < node.getLabel():
                    parent_node.setRight(nodo_aux)
                else:
                    parent_node.setLeft(nodo_aux)

            return None

        else:
            if node.getLabel() < label and node.getRight() is not None:
                node_b = self.remove_aux(node, node.getRight(), label)
                if node_b is not None:
                    return node_b

            if node.getLabel() > label and node.getLeft() is not None:
                node_b = self.remove_aux(node, node.getLeft(), label)
                if node_b is not None:
                    return node_b

        return None

    def remove(self, label):

        # verifica se a arvore esta vazia antes de iniciar
        if self.empty():
            return "Empty Tree"
        else:
            # Inicia a busca para remoção de nodo
            node_busca = self.remove_aux(self.root, self.root, label)
            if node_busca is None:
                return "Node does not exist in the tree"
            return node_busca

     # Encontrando o MAIOR e o MENOR elemento numa ÁRVORE Binária de Busca
    def min(self, node=ROOT):
        if node == ROOT:
            node = self.root
        while node.left:
            node = node.left
        return node.label

    # MÉTODO DE REMOÇÃO
    def removeNovo(self, value, node=ROOT):
        # Se for o valor padrão, node começa a ser a RAIZ da árvore.
        if node == ROOT:
            node = self.root
        # Tratando o caso base, se o Nó for nulo.
        if node is None:
            return node
        # Se o valor do Nó for menor, caminha para esquerda de forma recursiva.
        if value < node.label:
            node.left = self.removeNovo(value, node.left)
        # Se o valor do Nó for maior, caminha para direita de forma recursiva.
        elif value > node.label:
            #Substitui a subárvore a direita pelo o que a função recursiva irá retornar
            node.right = self.removeNovo(value, node.right)
        # Cai no else quando o valor é igual, onde inicia a REMOÇÃO
        else:
            # NÓ não tem filho a esquerda nem a direita = FOLHA, retorna NONE
            if node.left is None and node.right is None:
                return None
            # TRATANDO SEPARADAMENTE OS CASOS = Não tem filho à esquerda, então retorna o ramo da direita.
            if node.left is None:
                return node.right
            # Não tem filho à direita, então retorna o ramo da esquerda.
            elif node.right is None:
                return node.left
            else:
                # Cai no else quando TEM FILHO A ESQUERDA E FILHO A DIREITA.
                # Substituto é o sucessor do valor a ser removido, DEVEMOS BUSCAR O MENOR ELEMENTO DO RAMO A DIREITA
                # Para isso será utilizado a função min, onde encontra o menor elemento.
                substituto = self.min(node.right)
                # Ao invés de trocar a posição dos nós, troca o valor
                node.label = substituto
                # Depois, remove o substituto da subárvore à direita
                node.right = self.removeNovo(substituto, node.right)

        # Caso não encerre a função
        return node

            

    def altura(self, label):
          if label == None or label.getLeft() == None and label.getRight() == None:
               return 0
          else:
             if self.altura(label.getLeft()) > self.altura(label.getRight()):
                return  1 + self.altura(label.getLeft()) 
             else:
                return  1 + self.altura(label.getRight()) 
        