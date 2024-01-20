from graph_module import create_ukraine_graph
from dijkstra import dijkstra, reconstruct_path

G_ukraine = create_ukraine_graph()

start_point = "Івано-Франківськ"
distances, previous_nodes = dijkstra(G_ukraine, start_point)

print(f"Найкоротші шляхи від {start_point}:")
for destination in distances:
    path = reconstruct_path(start_point, destination, previous_nodes)
    print(f"До {destination}: {distances[destination]}, Шлях: {' -> '.join(path)}")
