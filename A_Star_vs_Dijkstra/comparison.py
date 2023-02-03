import timeit
import math
from a_star import a_star_algorithm
from dijkstra import dijkstra_algorithm
import matplotlib.pyplot as plt

S = 1
N = [10,50,100,200,500,1000,1500,2000]

dijkstra_actual_times = []
dijkstra_theoretical_times = []
astar_actual_times = []
astar_theoretical_times = []


def run_dijkstra():

    for i in N:
        graph = graph_of_dijkstra(i)
        start = timeit.default_timer()
        path, distances,repetitons = dijkstra_algorithm(graph, S, i)
        end = timeit.default_timer()
        dijkstra_actual_times.append((end - start) * 1000)
    return dijkstra_actual_times

def graph_of_dijkstra(n):
    graph = {}
    for i in range(1, n+1):
        graph[i] = {}
        for j in range(1, n+1):
            if i != j and abs(i-j) <= 3:
                graph[i][j] = i + j
    return graph

def run_a_star():
    for i in N:
        graph = graph_a_star(i)
        start = timeit.default_timer()
        path, distances, repetitions = a_star_algorithm(i, S, i, graph)
        end = timeit.default_timer()
        astar_actual_times.append((end - start) * 1000)
        
    return astar_actual_times

def graph_a_star(n):

    #  Graph is created with weights according to the given rules in the report.
    adjacency_matrix = [[float("inf")] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if i != j and abs(i-j) <= 3:
                adjacency_matrix[i][j] = i + j

    return adjacency_matrix 


 


dijkstra_actual = run_dijkstra()
astar_actual = run_a_star()

f1 = plt.figure()
ax1 = f1.add_subplot(111)
ax1.plot(N, dijkstra_actual,  color = "b")
ax2 = ax1.twinx()
ax2.plot(N, astar_actual, color = "r")
ax1.set_xlabel("N")
ax1.set_ylabel("Running Time (microsecends)")
ax1.legend(['Dijkstra Running Time'])
ax2.legend(['A Star Running Time'], loc = "upper right")
plt.show()

