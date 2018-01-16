# Prim-Jarnik MST.
#
# Unlike Kruskal's MST, requires a starting vertex (Can be any random vertex.
# You'll get the same result irrespective of the starting vertex chosen).


import heapq

class Vertex():
    def __init__(self, name):
        self.name = name
        self.edgeList = None


class Edge():
    def __init__(self, startVertex, endVertex, weight):
        self.startVertex = startVertex
        self.endVertex   = endVertex
        self.weight      = weight

    # comparison functions for sorting edges based on weight
    def __eq__(self, otherEdge):
        return self.weight == otherEdge.weight
    def __lt__(self, otherEdge):
        return self.weight < otherEdge.weight
    def __le__(self, otherEdge):
        return self.weight <= otherEdge.weight
    def __gt__(self, otherEdge):
        return self.weight > otherEdge.weight
    def __ge__(self, otherEdge):
        return self.weight >= otherEdge.weight
    def __ne__(self, otherEdge):
        return self.weight != otherEdge.weight



class Prim():
    def __init__(self, unvisitedVertices, startVertex):
        self.unvisitedVertices = unvisitedVertices # To begin with, this is a list of all the vertices in the graph
                                                   # If a vertex is removed from this list, it means that it has
                                                   # been added to the MST. The algorithm is complete when there
                                                   # are no more vertices in this list.

        self.nextVertex = startVertex              # Starting vertex for Prim's algorithm

        self.heap = []

        self.MST()


    # Since we are dealing with undirected graphs, the vertex we are currently
    # looking at might be the startVertex or endVertex of the edge.
    def getOtherVertex(self, vertex, edge):
        if vertex is edge.startVertex:
            return edge.endVertex
        else:
            return edge.startVertex


    def MST(self):
        self.unvisitedVertices.remove(self.nextVertex) # This vertex is not part of the MST


        # We are looping until all vertices have been visited.
        # This implementation assumes that the given graph is connected.
        # If it is a disconnected graph, then this implementation won't work
        # because we will be looping forever.
        while self.unvisitedVertices:

            # We have to pick min edge such that one vertex is in MST and the
            # other vertex is not in the MST (unvisitedVertices).
            for edge in self.nextVertex.edgeList:
                otherVertex = self.getOtherVertex(self.nextVertex, edge)
                if otherVertex in self.unvisitedVertices:
                    heapq.heappush(self.heap, edge)


            # In this loop, we pick the min edge such that one vertex is in MST
            # and the other vertex is not. We may have edges in the heap which
            # were inserted in previous iterations but now have both vertices
            # already in the MST. We should skip those edges.
            #
            # We cannot have an edge in the heap where both vertices are not
            # in the MST because an edge is added to the heap only when one
            # of the vertex is already in the MST.
            while True:
                edge = heapq.heappop(self.heap)
                if edge.startVertex not in self.unvisitedVertices and edge.endVertex not in self.unvisitedVertices:
                    # Skip edge with both vertices already in MST.
                    print("Skipping edge %s-%s" % (edge.startVertex.name, edge.endVertex.name))
                else:
                    # Edge with one vertex in MST and the other vertex not in MST.
                    print("Picking  edge %s-%s" % (edge.startVertex.name, edge.endVertex.name))
                    break


            self.nextVertex = edge.startVertex if edge.startVertex in self.unvisitedVertices else edge.endVertex
            self.unvisitedVertices.remove(self.nextVertex)



v1 = Vertex("A")
v2 = Vertex("B")
v3 = Vertex("C")
v4 = Vertex("D")

e1 = Edge(v1, v2, 1)
e2 = Edge(v2, v3, 2)
e3 = Edge(v1, v3, 1.5)
e4 = Edge(v3, v4, 3)
e5 = Edge(v2, v4, 11)

v1.edgeList = [e1, e3]
v2.edgeList = [e1, e2, e5]
v3.edgeList = [e2, e3, e4]
v4.edgeList = [e4, e5]

p = Prim([v1,v2,v3,v4], v1)
