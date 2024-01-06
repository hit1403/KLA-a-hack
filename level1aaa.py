import json
import math

with open(r"C:\KLA alum data\Input data\level1a.json") as inpf:
    idata = json.load(inpf)

print("idata:\n", idata,"\n\n\n\n\n")

num_neighbours = idata["n_neighbourhoods"]

restaurant_dist = []
neighbour_dist = []
neighbour_capacity = []
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
                if i3 == "order_quantity":
                    neighbour_capacity.append(v3)

    if i=="vehicles":
        for i1, v2 in v.items():
            for i3, v3 in v2.items():
                if i3 == "capacity":
                    capacity = v3 

                    
print("vehicle capacity -->",capacity)
print("r0 -->", restaurant_dist)
print("capacities : ",neighbour_capacity)

#graph = [restaurant_dist] + neighbour_dist
for i, n in enumerate(neighbour_dist):
    print(f"n{i} --->", n)



def nearest_neighbor(graph,glob_visited,capacity):
    n = len(graph)
    unvisited = set(range(1, n))  # Neighbouring locations excluding r0
    fin = [z for z in unvisited if z not in glob_visited]

    current_vertex = 0  # Starting at r0
    path = [current_vertex]

    local_cap = 0
    while fin:
        if local_cap>=capacity:
            path.append(0)  # Return to r0 to complete the cycle
            return path        # Check if current_vertex is valid
        if current_vertex >= n:
            break

        # Find the index of the nearest neighbor based on the distances in the graph
        nearest_neighbor_index = min(fin, key=lambda neighbor: graph[current_vertex][neighbor-1])
        path.append(nearest_neighbor_index)
        local_cap += neighbour_capacity[nearest_neighbor_index-1] 
        glob_visited.append(nearest_neighbor_index)
        fin.remove(nearest_neighbor_index)
        current_vertex = nearest_neighbor_index
    
    path.append(0)  # Return to r0 to complete the cycle
    return path

num_slots = math.ceil(sum(neighbour_capacity)/capacity)
visited = []
glob_visited = []
min_path_cycle=[]
for i in range(num_slots):

    min_path_cycle.append(nearest_neighbor([restaurant_dist]+neighbour_dist,glob_visited,capacity))
print(min_path_cycle)


result ={"v0":{}}
path=[]
for ind,i in enumerate(min_path_cycle):
    path.append([])
    for j in i:
        if j==0:
            path[ind].append("r0")
        else:
            path[ind].append("n"+str(j-1))
print(path)
adddict ={}

for i,j in enumerate(path):
    adddict["path"+str(i)] = path[i]
result["v0"]=adddict
print(result)
with open('level1a_output.json', 'w') as f:
    json.dump(result, f)




#result = {"v0": {"path1": ["r0", "n0", "n1", "n2", "n3", "n4", "r0"], "path2": ["r0", "n5", "n6", "n7", "n8", "n9",  "r0"], "path3": ["r0", "n10", "n11", "n12", "n13", "r0"]}}

