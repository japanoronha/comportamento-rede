"""
Dictionary that describes the graph
"""

graph = {'A': ['A0','A1','A2','A3','A4','B','D'],
         'B': ['B0','B1','B2','B3','B4','A','C'],
         'C': ['C0','C1','C2','C3','C4','B','D'],
         'D': ['D0','D1','D2','D3','D4','A','C'],
         'A0': ['A','A00','A01','A02','A03','A04'],
         'A1': ['A','A10','A11','A12','A13','A14'],
         'A2': ['A'],'A3': ['A'],'A4': ['A'],
         'B0': ['B','B00','B01','B02','B03','B04'],
         'B1': ['B','B10','B11','B12','B13','B14'],
         'B2': ['B'],'B3': ['B'],'B4': ['B'],
         'C0': ['C','C00','C01','C02','C03','C04'],
         'C1': ['C','C10','C11','C12','C13','C14'],
         'C2': ['C'],'C3': ['C'],'C4': ['C'],
         'D0': ['D','D00','D01','D02','D03','D04'],
         'D1': ['D','D10','D11','D12','D13','D14'],
         'D2': ['D'],'D3': ['D'],'D4': ['D'],
         'A00': ['A0'],'A01': ['A0'],'A02': ['A0'],'A03': ['A0'],'A04': ['A0'],
         'A10': ['A1'],'A11': ['A1'],'A12': ['A1'],'A13': ['A1'],'A14': ['A1'],
         'B00': ['B0'],'B01': ['B0'],'B02': ['B0'],'B03': ['B0'],'B04': ['B0'],
         'B10': ['B1'],'B11': ['B1'],'B12': ['B1'],'B13': ['B1'],'B14': ['B1'],
         'C00': ['C0'],'C01': ['C0'],'C02': ['C0'],'C03': ['C0'],'C04': ['C0'],
         'C10': ['C1'],'C11': ['C1'],'C12': ['C1'],'C13': ['C1'],'C14': ['C1'],
         'D00': ['D0'],'D01': ['D0'],'D02': ['D0'],'D03': ['D0'],'D04': ['D0'],
         'D10': ['D1'],'D11': ['D1'],'D12': ['D1'],'D13': ['D1'],'D14': ['D1'],
         }

class Graph:

    #Linha com comentário úncio 
    def __init__(self, graph = {}):
        self.__graph = graph

    #Retorna todas as ligações
    def edges(self):
        return [(node, neighbor)
                for node in self.__graph
                for neighbor in self.__graph[node]]

    #Retorna todos os nós
    def node(self):
        return list(self.__graph.keys())

    #Retorna os nós isolados
    def isolated_nodes(self):
        return [node for node in self.__graph if not self.__graph[node]]

    #Adiciona um nó ao grafo
    def add_node(self, node):
        if node not in self.__graph:
            self.__graph[node] = []
    
    #Adiciona um ligação entre dois nós
    def add_edge(self, node1, node2):
        if node1 not in self.__graph:
            self.add_node(node1)
        if node2 not in self.__graph:
            self.add_node(node2)
    
        self.__graph[node1].append(node2)
        self.__graph[node2].append(node1)
    
    #Retorna todos os caminhos possíveis entre dois nós
    def all_paths(self, node1, node2, path = []):
        path = path + [node1]
        if node1 not in self.__graph:
            return []
        if node1 == node2:
            return [path]
        
        paths = []

        for node in self.__graph[node1]:
            if node not in path:
                subpaths = self.all_paths(node, node2, path)

                for subpath in subpaths:
                    paths.append(subpath)
        return paths

    #Retorna o caminho mais curto
    def shortest_path(self, node1, node2):
        return sorted(self.all_paths(node1, node2), key = len)[0]

g = Graph(graph)

print(g.shortest_path('A02','C03'))