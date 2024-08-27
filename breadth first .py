graph = {
    'P': ['Q','R','S'],
    'Q': ['R' , 'T'],
    'R': ['T'],
    'S': [],
    'T': []
}

visited = []                                   # visited = ()
queue = []
def dfs(visited, graph, node):
  visited.append(node)
  queue.append(node)


  while queue:
    m=queue.pop(0)
    print(m)

    for neighbour in graph[m]:
      if neighbour not in visited:
        visited.append(neighbour)
        queue.append(neighbour)


print('Here is the Breadth first: ')
dfs(visited, graph, 'P')


