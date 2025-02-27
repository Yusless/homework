def dipart(graph, node, colors=None, color=0):

    if colors is None:
        colors = {}

    '''if node in colors:
        return colors[node]==color'''
    
    colors[node] = color
    #print(colors)
    for neighbor in graph[node]:
        if not dipart(graph,neighbor,colors, 1-color):
            return False
        
    return True

def check(graph):

    colors={}
    for node in graph:
        if node not in colors:
            if not dipart(graph, node, colors):
                return False
    return True
graph = {
    0: [1, 3],
    1: [0, 2],
    2: [ 1, 3],
    3: [0, 2]
}

print("Граф двудольный" if check(graph) else "Граф не двудольный")
