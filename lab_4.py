# initialize graph
graph = {'A': {'B', 'C'},
         'B': {'A', 'D', 'E'},
         'C': {'A', 'F'},
         'D': {'B'},
         'E': {'B', 'F'},
         'F': {'C', 'E'}}


# define function for dfs
def dfs_paths(graph, start, goal):
    # create stack
    stack = [(start, [start])]
    while stack:
        (vertex, path) = stack.pop()
        for i in graph[vertex] - set(path):
            # if found i and it equals goal
            if i == goal:
                yield path + [i]
            else:
                # add element to stack
                stack.append((i, path + [i]))


print list(dfs_paths(graph, 'A', 'F')) # [['A', 'C', 'F'], ['A', 'B', 'E', 'F']]