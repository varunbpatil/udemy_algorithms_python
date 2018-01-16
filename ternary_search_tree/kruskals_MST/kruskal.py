# Kruskal's MST
# Sort edge by weights. Keep picking the minimum edge weight that doesn't introduce a cycle.
# How do we check whether picking an edge will introduce a cycle ? Ans = (Union-find) / (disjoint sets) data structure.
#
# Union-find has two optimizations:
# 1. union by rank: This optimization is done during the "union" operation.
# 2. path compression: This optimization is done during the "find" operation.
#
# Notice the use of "is" comparison instead of "==" in implementation of union-find.


# Vertices of the graph
class Vertex():
    def __init__(self, name):
        self.name = name
        self.node = None # maps vertex to its node in the union-find data structure
                         # This is a one-way mapping from vertex (of graph) to
                         # node (of union-find tree). We don't need a mapping
                         # in the other direction.

# Edges of the graph
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



# union-find data structure is implemented as a "sort of" tree structure.
# This class represents the union-find data structure.
# One node is associated with one vertex in the graph.
class Node():
    def __init__(self):
        self.rank = 0  # Required for "union by rank" optimization
        self.parentNode = None # Used to get to the representative/root node
                               # in the "find" operation.
                               # For the root node, its parentNode points to itself.



class Kruskal():
    def __init__(self, vertexList, edgeList):
        self.vertexList = vertexList
        self.edgeList   = edgeList
        self.setCount = 0 # At the end of MST construction, if setCount > 1,
                          # it means we have a disconnected graph. i.e, no MST.

        self.makeSet() # This is one of the operations of the union-find data structure
                       # This adds each of the vertices of the graph into its own set.
                       # i.e, each set contains just one item (one vertex) after this.
        self.MST()


    def makeSet(self):
        for vertex in self.vertexList:
            vertex.node = Node()
            vertex.node.parentNode = vertex.node # Initially, parentNode points to itself
            self.setCount += 1


    # Return the set representative node for the given node
    def find(self, node):
        # This is the "find" implementation without "path compression" optimization
        #
        # if node.parentNode is node:
        #     return node
        # else:
        #     return self.find(node.parentNode)


        # This is the "find" implementation with "path compression" optimization
        #
        # If any node is not directly attached to the set representative/root node,
        # attach it directly to the root node so that subsequent find's will be
        # faster.
        if node.parentNode is not node:
            node.parentNode = self.find(node.parentNode)

        return node.parentNode


    def union(self, u_root, v_root):
        # "Union by rank" optimization: Attach the root with the lower rank
        # to the root with the higher rank to maintain balance.
        #
        # If rank are same, need to increment rank, otherwise no.
        if u_root.rank > v_root.rank:
            v_root.parentNode = u_root
        elif u_root.rank < v_root.rank:
            u_root.parentNode = v_root
        else:
            # You can attach any way, but you need to increment rank.
            u_root.parentNode = v_root
            v_root.rank += 1

        self.setCount -= 1


    def MST(self):
        for edge in sorted(self.edgeList):
            u = edge.startVertex
            v = edge.endVertex

            u_set_root = self.find(u.node) # Find the set representative for 'u'
            v_set_root = self.find(v.node) # Find the set representative for 'v'

            if u_set_root is v_set_root:
                # Vertices are already in the same set.
                # Adding this edge will introduce a cycle. So, skip it.
                print("Skipping edge %s-%s" % (edge.startVertex.name, edge.endVertex.name))
                continue
            else:
                # Pick this edge for the MST.
                # We have to do a union operation on the two vertices.
                print("Picking  edge %s-%s" % (edge.startVertex.name, edge.endVertex.name))
                self.union(u_set_root, v_set_root)

        if (self.setCount > 1):
            print("Disconnected graph. No MST.")


            


v1 = Vertex("A")
v2 = Vertex("B")
v3 = Vertex("C")
v4 = Vertex("D")

e1 = Edge(v1, v2, 1)
e2 = Edge(v2, v3, 2)
e3 = Edge(v1, v3, 1.5)
e4 = Edge(v3, v4, 3)
e5 = Edge(v2, v4, 11)


k = Kruskal([v1,v2,v3,v4], [e1,e2,e3,e4,e5])
