def getHAmiltonPath(graph):
    graphCopy = graph.copy()
    path = []
    n = len(graph.keys())

    def solve(options):
        if n == len(path):
            return True

        options = sorted(options, key=lambda opt: len(graphCopy[opt]))

        for opt in options:
            path.append(opt)

            for vertex in graph[opt]:
                graphCopy[vertex].remove(opt)

            if solve(graphCopy[opt]):
                return path

            path.pop()
            for vertex in graph[opt]:
                graphCopy[vertex].append(opt)

        return False

    res = solve(range(1, n+1))
    return path if res else False