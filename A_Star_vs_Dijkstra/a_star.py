import heapq

def a_star_algorithm(N, start, goal, graph):
    # Set of nodes already evaluated
    closed_set = set()
    # Set of currently discovered nodes that are not evaluated yet.
    # Initially, only the start node is known.
    open_set = set([start])
    # For each node, which node it can most efficiently be reached from.
    # If a node can be reached from many nodes, came_from will eventually contain the
    # most efficient previous step.
    came_from = {}
    # For each node, the cost of getting from the start node to that node.
    g_score = {node: float('inf') for node in range(N)}
    g_score[start] = 0
    # For each node, the total cost of getting from the start node to the goal
    # by passing by that node. That value is partly known, partly heuristic.
    f_score = {node: float('inf') for node in range(N)}
    f_score[start] = heuristic_estimate(start, goal)

    # The heapq module implements a priority queue using a heap data structure
    heap = []
    heapq.heappush(heap, (f_score[start], start))
    repetitions = 0

    while heap: # This loops runs until heap is empty.
        current = heapq.heappop(heap)[1] # It removes and returns the smallest element from the heap.
        repetitions += 1 # Increase the repetition
        if current == goal:  # if current node reaches the destination node.
            return reconstruct_path(came_from, goal), g_score[goal], repetitions # It reconstruct the path and return the shortest path.
        open_set.remove(current) # current node is removed from open_set
        closed_set.add(current) # current node is added to the closed_path
        
        for neighbor in range(N): 
            if graph[current][neighbor] == float('inf'): 
                continue
            if neighbor in closed_set: # If neighbor node is in closed_set
                continue
            tentative_g_score = g_score[current] + graph[current][neighbor]
            if neighbor not in open_set: # if neighbor is not in open_set
                open_set.add(neighbor) # add neighbor to open_set
            elif tentative_g_score >= g_score[neighbor]:
                continue
            came_from[neighbor] = current
            g_score[neighbor] = tentative_g_score
            f_score[neighbor] = g_score[neighbor] + heuristic_estimate(neighbor, goal)
            heapq.heappush(heap, (f_score[neighbor], neighbor))

    return [], float('inf'), repetitions

# reconstruct_path function creates the shortest path. It starts from the last node and following previous nodes back to the beginning
def reconstruct_path(came_from, current):
    path = [current]
    while current in came_from:
        current = came_from[current]
        path.append(current) # add current to shortest path
    path.reverse() # reverse the shortest path
    return path

def heuristic_estimate(node, destination):
    # This function should return an estimate of the cost to get from the given node to the goal.
    return abs(destination - node)



