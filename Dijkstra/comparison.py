import timeit
from dijkstra import dijkstra_algorithm 
import matplotlib.pyplot as plt
import math

S = 1
N = [10, 50, 100, 200, 500, 1000, 2000]  # Values of N to test
actual_times = []
theoretical_times = []


def graph_dijkstra():
    for i in N:
        graph = create_graph(i)
        start = timeit.default_timer()
        path, distances,repetitons = dijkstra_algorithm(graph, S, i)
        end = timeit.default_timer()
        actual_times.append((end - start) * 1000)
        theoretical_times.append(((i+ repetitons)*math.log(i)))

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
    graph = {}
    for i in range(1, n + 1):
        graph[i] = {}
        for j in range(1, n + 1):
            if i != j and abs(i-j) <= 3: # i and j cannot be eqaul and abs(i-j) must be equal or smaller than 3.
                graph[i][j] = i + j

    return graph            
graph_dijkstra()



