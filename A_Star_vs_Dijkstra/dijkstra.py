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
  
  # Repeat until heap is empty
  while heap:
    # Extract node with smallest distance
    distance, node = heapq.heappop(heap)
    repetitons += 1
    # Skip node if it has been visited
    if distance > distances[node]:
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
  current = destination
  while current is not None:
    path.append(current)
    current = previous[current]
  path.reverse()
  #print("distances : ", distances)
  return path, distances[destination],repetitons

  