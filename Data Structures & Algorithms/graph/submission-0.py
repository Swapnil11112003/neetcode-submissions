class Graph:
    
    def __init__(self):
        self.graph = {}


    def addEdge(self, src: int, dst: int) -> None:
        if src not in self.graph:
            self.graph[src] = []
        if dst not in self.graph:
            self.graph[dst] = []

        if dst not in self.graph[src]:
            self.graph[src].append(dst)

    def removeEdge(self, src: int, dst: int) -> bool:
        if src not in self.graph or dst not in self.graph:
            return False

        if dst in self.graph[src]:
            self.graph[src].remove(dst)
            return True
        
        return False
        
    def hasPath(self, src: int, dst: int) -> bool:
        q = deque([src])
        visit = set()
        visit.add(src)
    
        while q:
            for i in range(len(q)):
                node = q.popleft()
                if node == dst:
                    return True

                visit.add(node)
                for item in self.graph[node]:
                    if item not in visit:
                        q.append(item)                

        return False
