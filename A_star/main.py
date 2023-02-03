import timeit
from a_star import a_star_algorithm

def main():
    # Read N, Source, and Destination from the user
    N = int(input("Enter N: "))
    S = int(input("Enter Source: "))
    D = int(input("Enter Destination: "))
    
    #  Graph is created with weights according to the given rules in the report.
    adjacency_matrix = [[float("inf")] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if i != j and abs(i-j) <= 3:
                adjacency_matrix[i][j] = i + j

                
    # Calculate the shortest path, distance and  repetitions
    start_time = timeit.default_timer()
    shortest_path, cost, repetitions = a_star_algorithm(N , S, D , adjacency_matrix)
    end_time = timeit.default_timer()
    print(f'Time: {((end_time)-(start_time) ) * 1000}')
    
    # Print shortest path, distance and  repetitions
    print("Shortest path: {0}".format(shortest_path))
    print("Cost: {0}".format(cost))
    print("Repetitions: {0}".format(repetitions))


main() # Invoke the main function