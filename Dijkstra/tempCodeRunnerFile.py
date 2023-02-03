    # # Graph is created with weights according to the given rules in the report.
    graph = {}
    for i in range(1, N + 1):
        graph[i] = {}
        for j in range(1, N + 1):
            if i != j and abs(i-j) <= 3: # i and j cannot be eqaul and abs(i-j) must be equal or smaller than 3.
                graph[i][j] = i + j