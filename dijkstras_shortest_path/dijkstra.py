import heapq # for heap


class Vertex():
    def __init__(self, name):
        self.name = name

        self.minDistanceToNode = float('inf') # Min distance from start node to
                                              # this node at this moment. Can
                                              # change(reduce) during the course
                                              # of the algorithm.

        self.previousNode = None # previous pointer to reconstruct shortest path
                                 # once the algorithm is complete

        self.adjacencyList = []  # List of (vertex,weight) tuples that can be
                                 # reached from this node

        self.visited = False # Once we greedily pick the vertex with the min distance
                             # we are done with that node. We cannot have a
                             # shorter path to that vertex than the one we
                             # already have (because no negative edge weights).



    # Object comparison functions that enable us to use 'heapq' 
    # module to maintain a heap for us.

    def __lt__(self, otherVertex):
        return self.minDistanceToNode < otherVertex.minDistanceToNode
    def __le__(self, otherVertex):
        return self.minDistanceToNode <= otherVertex.minDistanceToNode
    def __gt__(self, otherVertex):
        return self.minDistanceToNode > otherVertex.minDistanceToNode
    def __ge__(self, otherVertex):
        return self.minDistanceToNode >= otherVertex.minDistanceToNode
    def __eq__(self, otherVertex):
        return self.minDistanceToNode == otherVertex.minDistanceToNode



# We can calculate shortest path from startVertex to all other vertices in one go.
def calculate_shortest_path(startVertex):
    heap = []
    startVertex.minDistanceToNode = 0
    heapq.heappush(heap, startVertex)

    while len(heap) > 0:
        next_nearest_vertex = heapq.heappop(heap)

        if next_nearest_vertex.visited:
            continue

        next_nearest_vertex.visited = True

        # Update min distances for all neighbors
        for v, weight in next_nearest_vertex.adjacencyList:
            if v.minDistanceToNode > next_nearest_vertex.minDistanceToNode + weight:
                v.minDistanceToNode = next_nearest_vertex.minDistanceToNode + weight
                v.previousNode = next_nearest_vertex

                # If the min distance was updated to a shorter one, add it to
                # the heap once again. Note that now the heap will contain multiple
                # entries for the same vertex (albeit with the same (new) min distance
                # because it is the same vertex object that is added multiple times).
                # Hence, we should have logic to skip vertex if already visited.
                heapq.heappush(heap, v)







# Once the algorithm is complete, we will have the shortest path from startVertex
# to all other vertices.
#
# Then, it is just a matter of traversing the previousNode pointers to
# reconstruct the shortest path to a given targetVertex.
def get_shortest_path(targetVertex):
    tmp = targetVertex
    while tmp:
        print(tmp.name + "<-", end="")
        tmp = tmp.previousNode




v1 = Vertex('A')
v2 = Vertex('B')
v3 = Vertex('C')

v1.adjacencyList = [(v2, 1), (v3, 10)]
v2.adjacencyList = [(v3, 2)]

calculate_shortest_path(v1)
get_shortest_path(v3)
