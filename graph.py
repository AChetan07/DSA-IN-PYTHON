# # # graph data structure
# # graph is a linear data structure that consists of nodes connected by edges
# # it is  collection of vertices and edges the vertices are the nodews and the edges are the connection between nodes
# # the graph is a widely used daya structurein cs and used in various applications sucha s sociaal networks web pages and transportation systems
# # the graph is a versatile data structure used to represent relationships between data elements
# it is a pwerfull data structure that can used for simple and complex problems to be solved in an efficient way
class Graph:
        def __init__(self):
            self.graph={} 
        
        
        def add_edge(self,u,v):
          if u not in self.graph:   
                self.graph[u]=[]
          if v not in self.graph:
                self.graph[v]=[]
          
          self.graph[u].append(v)
          self.graph[u].append(u)
        
        
        def remove_edge(self,u,v):
             if u in self.graph and v in self.graph[u]:
                  self.graph[u].remove(v)
             if v in self.graph and u in self.graph[v]:
                  self.graph[v].remove(u)
        
        
        def dfs(self,start,visited=None):
             if visited is None:
                  visited=set()
             visited.add(start)
             print(start,end="")
             for neighbour in self.graph.get(start,[]):
                  if neighbour not in visited:
                       self.dfs(neighbour,visited)
        def bfs(Self,start):
             visited =set()
             queue=[start]
             visited.add(start)
             while queue:
                  vertex =  queue.pop()
                  print(vertex,end="")
                  for neighbour in self.graph.get(vertex,[]):
                       visited.add(neighbour)
                       queue.append(neighbour)
        
                  