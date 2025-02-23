from collections import deque

def bfs(graph, start):
    visited = set()  
    queue = deque([start]) 

    while queue:
        node = queue.popleft()  
        if node not in visited:
            print(node, end=" ")  
            visited.add(node) 
            for neighbor in graph[node]:
                if neighbor not in visited:
                    queue.append(neighbor) 

graph = {
    0: [1, 2],
    1: [0, 3, 4],
    2: [0, 5],
    3: [1],
    4: [1],
    5: [2]
}

bfs(graph, 0)  # Start BFS from node 0