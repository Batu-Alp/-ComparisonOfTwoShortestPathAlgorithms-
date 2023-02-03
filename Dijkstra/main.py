from dijkstra  import dijkstra_algorithm # import the dijkstra function from dijkstra_algorithm.py
import timeit

def main():
    # Read N, Source, and Destination from the user.
    N = int(input("Enter N: "))
    S = int(input("Enter Source: "))
    D = int(input("Enter Destination: "))
    
    # # Graph is created with weights according to the given rules in the report.
    graph = {}
    for i in range(1, N + 1):
        graph[i] = {}
        for j in range(1, N + 1):
            if i != j and abs(i-j) <= 3: # i and j cannot be eqaul and abs(i-j) must be equal or smaller than 3.
                graph[i][j] = i + j
                
    # Calculate the shortest path, distance and  repetitions
    start_time = timeit.default_timer()
    shortest_path, distance, repetitions = dijkstra_algorithm(graph, S, D)
    end_time = timeit.default_timer()
    print(f'Time: {((end_time)-(start_time) ) * 1000}')

    # Print shortest path, distance and  repetitions
    print("Shortest path: {0}".format(shortest_path))
    print("Cost: {0}".format(distance))
    print("Repetitions: {0}".format(repetitions))

main() # invoke main dunction
