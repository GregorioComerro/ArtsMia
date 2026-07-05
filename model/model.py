import networkx as nx

from database.DAO import DAO


class Model:
    def __init__(self):
        self._graph = nx.Graph()
        self._idMap = {}

    def buildGraph(self):
        self._graph.clear()

        objects = DAO.getAllNodes()
        self._graph.add_nodes_from(objects)

        for obj in objects:
            self._idMap[obj.object_id] = obj

        edges = DAO.getAllEdges()

        for edge in edges:
            id1 = edge["id1"]
            id2 = edge["id2"]
            peso = edge["peso"]
            if id1 in self._idMap and id2 in self._idMap:
                obj1 = self._idMap[id1]
                obj2 = self._idMap[id2]
                self._graph.add_edge(obj1, obj2, weight=peso)


    def getGraphdetails(self):
        return len(self._graph.nodes), len(self._graph.edges)

    def getComponenteConnessa(self, nodo):
        try:
            object_id = int(nodo)
        except ValueError:
            raise ValueError("Id oggetto non valido")

        if object_id not in self._idMap:
            raise ValueError("Oggetto non presente nel grafo")

        componente = nx.node_connected_component(self._graph, self._idMap[object_id])
        return componente

    def getGrado(self, nodo):
        object_id = int(nodo)
        oggetto = self._idMap[object_id]
        return self._graph.degree[oggetto]

    def getPrimoNodoConnesso(self):
        for nodo in self._graph.nodes:
            if self._graph.degree[nodo] > 0:
                return nodo.object_id, self._graph.degree[nodo]
        return None, 0



