from collections import defaultdict
def dipart(graph, node, colors=None, color=0):

    if colors is None:
        colors = {}

    if node in colors:
        return colors[node]==color
    
    colors[node] = color
    #print(colors)
    for neighbor in graph[node]:
        if not dipart(graph,neighbor,colors, 1-color):
            return False
        
    return True

def check(graph,n):

    colors={}
    for i in range(1,n+1):
        node=i
        #print(node)
        if node not in graph:
            return False
        if node not in colors:
            if not dipart(graph, node, colors):
                return False
    return True

n=int(input('Введите число человек:'))
g=defaultdict(list)
l=int(input('Введите число элементов dislike:')) #число элементов dislike
dis=[[j for i in range(2)] for j in range(l)] 
for i in range(l):
    dis[i]=list(map(int, input(f'Введите через пробел {i+1} элемент dislike:').split()))

for i in range(len(dis)):
    nums=dis[i]
    g[nums[0]].append(nums[1])

#print(g)
print(True if check(g,n) else False)

