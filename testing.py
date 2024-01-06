import json

def nearest_neighbor(graph):
    n = len(graph)
    unvisited = set(range(1, n))  # Neighbouring locations excluding r0
    current_vertex = 0  # Starting at r0
    path = [current_vertex]


    while unvisited:
        # Check if current_vertex is valid
        if current_vertex >= n:
            break

        # Find the index of the nearest neighbor based on the distances in the graph
        nearest_neighbor_index = min(unvisited, key=lambda neighbor: graph[current_vertex][neighbor-1])
        path.append(nearest_neighbor_index)
        unvisited.remove(nearest_neighbor_index)
        current_vertex = nearest_neighbor_index

    path.append(0)  # Return to r0 to complete the cycle
    return path


# Loading input data
with open(r"C:\KLA alum data\Input data\level0.json") as inpf:
    idata = json.load(inpf)

print("idata:\n", idata)

num_neighbours = idata["n_neighbourhoods"]

restaurant_dist = []
neighbour_dist = []

for i, v in idata.items():
    if i == "restaurants":
        for x, z in v.items():
            for x2, z2 in z.items():
                if x2 == "neighbourhood_distance":
                    restaurant_dist = z2

    if i == "neighbourhoods":
        for i1, v2 in v.items():
            for i3, v3 in v2.items():
                if i3 == "distances":
                    neighbour_dist.append(v3)

print("r0 -->", restaurant_dist)

visited = []
path = []
path.append(-1)
visit = restaurant_dist.index(min(restaurant_dist))
print(visit)

# Given graph (distances between locations)
graph = [restaurant_dist] + neighbour_dist
for i, n in enumerate(graph):
    print(i, "--->", n)

min_path_cycle = nearest_neighbor(graph)

print("Minimum path cycle:", min_path_cycle)
result =[]
for i in min_path_cycle:
    if i==0:
        result.append(f"r{i}")
    else:
        result.append(f"n{i-1}")
print(result)

outdict={"v0": {"path": result}}
with open('level0_output.json', 'w') as f:
    json.dump(outdict, f)