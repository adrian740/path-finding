import numpy as np
import matplotlib.pyplot as plt

# Format matplotlib
plt.rcParams.update({'font.size': 10})
plt.rcParams.update({'figure.dpi': 300})
plt.rcParams.update({'figure.autolayout': True})

data1 = np.genfromtxt("ERDA 3c - Sheet1.csv", delimiter=",")
data2 = np.genfromtxt("cities south holland.csv", delimiter=",")

plt.minorticks_on()
plt.grid(b=True, which='major', color='gray', linestyle='-')
plt.grid(b=True, which='minor', color='lightgray', linestyle='--')

city_nodes = np.array([data2[:,1], data2[:,2]]).T
unvisited_parks = data1[:,1:].tolist()
starting_node = [52.0186, 4.3782]

alpha, segments = 100, 10

def cost(start_node, end_node):
    start_node, end_node = np.array(start_node), np.array(end_node)
    sum_1 = 0
    sum_2 = 0
    for i in range(segments):
        scaled_ = start_node + (end_node - start_node)*i/segments
        for city in city_nodes:
            sum_1 += np.linalg.norm(city - scaled_)
            sum_2 += np.linalg.norm(city - scaled_)
    return sum_2 / (np.linalg.norm(end_node - start_node))**alpha, sum_1

def rc_plane_path(starting_node):
    x_coord, y_coord, total_cost = [starting_node[0]], [starting_node[1]], 0
    sum_dist = 0
    while len(unvisited_parks) != 0:
        costs = []
        for park in unvisited_parks:
            s = cost(starting_node, park)
            sum_dist += s[1]
            costs.append(s[0])
        idx = np.argmax(costs)
        total_cost += costs[idx]
        target_park = unvisited_parks[idx]
        unvisited_parks.remove(target_park)
        x_coord.append(target_park[0])
        y_coord.append(target_park[1])
    return x_coord, y_coord, total_cost, sum_dist

x_coord, y_coord, total_cost, sum_dist = rc_plane_path(starting_node)
plt.plot(x_coord, y_coord, label=r"Path $\alpha=$" + str(alpha), color="darkorchid")
plt.xlabel(r"Latitude [$^{\circ}$]")
plt.ylabel(r"Longitude [$^{\circ}$]")
print("Total cost:", total_cost, "Dist:", sum_dist)

plt.scatter(data1[:,1], data1[:,2], label="Parks")
plt.scatter(data2[:,1], data2[:,2], label="Cities")

plt.scatter([52.0186], [4.3782], label="Delft")
plt.scatter([52.1763], [4.5282], label="Leiden")

plt.xlim(51.9, 52.2)
plt.legend()
plt.show()