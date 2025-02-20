from collections import defaultdict

class Graph:
    def __init__(self, vert):
        self.V = vert
        self.graph = defaultdict(list)

    def add_node(self, u, v):
        self.graph[u].append(v)

    def print_graph(self):
        print(self.graph)
    
    def check_for_judge(self):
        self.a=-1
        for i in range(1,self.V+1):
            for j in range(1,self.V+1):
                #print(i, j, self.graph[j], self.graph[i])
                if i in self.graph[j] and j not in self.graph[i]:
                    self.a=i
                elif i != j:
                    self.a=-1
                    break
        print(self.a)
        
                

n=int(input())
g = Graph(n)
l=int(input()) #число элементов trust
trust=[[j for i in range(2)] for j in range(l)] 
for i in range(l):
    trust[i]=list(map(int, input().split()))
for i in range(len(trust)):
    nums=trust[i]
    g.add_node(nums[0],nums[1])
#g.print_graph()
g.check_for_judge()

