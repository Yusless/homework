#task2
from collections import defaultdict

class Graph:
    def __init__(self, vert):
        self.V = vert
        self.graph = defaultdict(list)

    def add_node(self, u, v):
        self.graph[u].append(v)

    def print_graph(self):
        print(self.graph)

    def rope(self):
        sampo=1
        dis=0
        for key in self.graph.items():
            letters=self.graph[key[0]]
            pairs=len(letters)
            for j in range(len(letters)):
                for keisy in self.graph.items():
                    print(f'Первая проверка {letters[j],keisy[0]}')
                    if letters[j]==keisy[0]:
                        pairs-=1
                    print(f'Нецелых пар 1 {pairs}')
            if pairs>0:
                dis+=1
            pairs=len(letters)
            for keys in self.graph.items():
                print(f' Вторая проверка {key[0],self.graph[keys[0]][0]}')
                if key[0]==str(self.graph[keys[0]][0]):
                    pairs-=1
                print(f'Нецелых пар 2 {pairs}')
            if pairs>0:

                dis+=1
            print(dis)
            if dis > 2:
                sampo=0
        if sampo == 1:
            print(True)
        else: print(False)
                

n=int(input()) #число слов
g=Graph(n)
cities=[]
for i in range(n):
    a=str(input())
    cities.append(a)
for i in range(n):
    city=cities[i]
    first=city[0]
    last=city[-1]
    g.add_node(first,last)
g.print_graph()
g.rope()