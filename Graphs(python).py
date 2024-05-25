class Graph:
    def __init__(self):
        self.graph = {}

    def addEdge(self,a,b):
        if a not in self.graph:
            self.graph[a]=[]
            self.graph[a].append(b)
        else:
            self.graph[a].append(b)

    def dfs(self):
        a=self.graph
        queue=[1]
        visited=set()
        visited.add(1)
        while queue:
            s=queue.pop(0)
            print(s,end=" ")
            for i in a[s]:
                if i not in visited:
                    visited.add(i)

    def bfs(self):
        a=self.graph
        queue=[1]
        visited=set()
        visited.add(1)
        while queue:
            s=queue.pop(0)
            print(s,end=" ")
            if s in a:
                for i in a[s]:
                    if i not in visited:
                        visited.add(i)
                        queue.append(i)

    def printMatrix(self):
        matrix = [[0 for _ in range(len(self.graph))] for _ in range(len(self.graph))]
        for i in self.graph:
            for j in self.graph[i]:
                if i-1 < len(matrix) and j-1 < len(matrix[i-1]):
                    matrix[i-1][j-1] = 1
        for row in matrix:
            print(*row)

    #def nums_islands(grid):


g=Graph()
g.addEdge(1,2)
g.addEdge(1,1)
g.addEdge(2,1)
print(g.graph)
g.dfs()
print()
g.bfs()
print()
g.printMatrix()