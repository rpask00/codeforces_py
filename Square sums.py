import sys
 
sys.setrecursionlimit(10 ** 6)  # this is a recursive solution that creates n stacks for solve(n), raise the ceiling
 
 

def square_sums(n):  # this function runs all the code and returns a hamiltonian path
    return findHamiltonianPath(getSquareSumsGraph(n))
 
 
# generate undirected graph of numbers in a range
# connect all vertices v1 and v2 that sum to a perfect square, where sqrt(v1 + v2) = an integer
# example: given 6 and 10, sqrt(6 + 10) = 4, therefore connect vertex(6) to vertex(10)
def getSquareSumsGraph(n):
    squares = {x for x in range(4, 2 * n) if (x ** (1 / 2)).is_integer()}  # generate perfect squares in range 2n
    graph = {}  # initialize an empty dictionary
 
    for vertex in range(1, n + 1):  # iterate the range 1 -> n, each is a vertex (v1)
        subVertices = []  # this empty array will represent the vertices connected to vertex
        for square in squares:  # iterate the pre-calculated squares
            candidate = square - vertex  # since v1 + v2 (candidate) = square; v2 = square - v1
            if 0 < candidate <= n and candidate != vertex:  # confirm that candidate exists in the range and != v1
                subVertices.append(candidate)  # keep candidate (v2)
        graph[vertex] = subVertices  # all vertices connected to vertex have been collected, store them in the graph
 
    return graph
 
 
# return the first hamiltonian path found in the graph
# if no path found, return False
def findHamiltonianPath(graph):
    graphLength = len(graph)  # store the graph length for optimization
    subGraph = graph.copy()  # copy the graph. subGraph will be used to add and remove connections as we iterate
    path = []  # path will store our final result
 
    # recursive child function handles searching for the path
    def search(options):
        if len(path) == graphLength:  # if path and graph are the same length, Hamiltonian Path has been found
            return path  # return the Hamiltonian Path
        options = sorted(options, key=lambda option: len(graph[option]))  # sort by shortest subVertices - optimization
        for option in options:  # iterate all the options. we are starting with the vertices that have the least options
            path.append(option)  # add the option to the path
            for vertex in graph[option]:  # now that option is in the path, remove it from connected subVertices
                subGraph[vertex].remove(option)
            if search(subGraph[option]):  # recurse from the next vertex of position option
                return path  # a member of the stack has found a path, return the path
            path.pop()  # path was not found with that option, remove it from the path
            for vertex in graph[option]:  # put the option back in all the subVertices it should be connected to
                subGraph[vertex].append(option)
        return False  # no path was found, return False
 
    return search([*range(1, graphLength + 1)])  # seed the search with the full range of options
    
    

print(square_sums(15))