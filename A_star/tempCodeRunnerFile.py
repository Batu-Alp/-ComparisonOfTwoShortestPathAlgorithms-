import timeit
from a_star import a_star_algorithm
import matplotlib.pyplot as plt

S = 1
actual_times = []
theoretical_times = []

def run_a_star():
    N= [10,50,100,200,500,1000,1500,2000]
    for i in N:
        graph = create_graph(i)
        start = timeit.default_timer()
        path, distances, repetitions = a_star_algorithm(i, S, i-1, graph)
        end = timeit.default_timer()
        actual_times.append((end - start) * 1000)
        theoretical_times.append(repetitions)
    
    f1 = plt.figure()
    ax1 = f1.add_subplot(111)
    ax1.plot(N, actual_times, label = "actual_times", color = "b")
    ax2 = ax1.twinx()
    ax2.plot(N, theoretical_times, label = "theoretical_times", color = "r")
    ax1.set_xlabel("N")
    ax1.set_ylabel("Running Time (microsecends)")
    ax1.legend(['Actual Running Time'])
    ax2.legend(['Theoretical Running Time'], loc = "upper right")
    plt.show()

def create_graph(n):

    
    #  Graph is created with weights according to the given rules in the report.
    adjacency_matrix = [[float("inf")] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if i != j and abs(i-j) <= 3:
                adjacency_matrix[i][j] = i + j

    return adjacency_matrix        

run_a_star()