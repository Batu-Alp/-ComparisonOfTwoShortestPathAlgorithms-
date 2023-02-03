import heapq

def dijkstra_algorithm(graph, source, destination):
  # Initialize distances and previous nodes for each node
  repetitons = 0

  distances = {node: float("inf") for node in graph}
  previous = {node: None for node in graph}
  distances[source] = 0
  
  # Initialize min-heap with all nodes and their distances
  heap = []
  for node in graph:
    heap.append((distances[node], node))
  heapq.heapify(heap)
  
  while heap: # Loop runs until the min_heap is empty
    distance, node = heapq.heappop(heap)     # Update distances and previous nodes of neighbors
    repetitons += 1
    if distance > distances[node]: # Skip the node if it is already visited
      continue
    

    # Update distances and previous nodes of neighbors
    for neighbor in graph[node]:
      alt = distance + graph[node][neighbor]
      if alt < distances[neighbor]:
        distances[neighbor] = alt
        previous[neighbor] = node
        heapq.heappush(heap, (alt, neighbor))
  
  # Construct shortest path
  path = []
  current = destination # shortest path list.
  while current is not None: # It works until current is None.
    path.append(current) # the current node is added to the shortest path.
    current = previous[current] # update current node
  path.reverse() # shortest path is reversed

  return path, distances[destination],repetitons  # Return the shortest path and distance


