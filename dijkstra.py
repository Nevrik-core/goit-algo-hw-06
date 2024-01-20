def print_table(distances, visited):
    # Верхній рядок таблиці
    print("{:<10} {:<10} {:<10}".format("Вершина", "Відстань", "Перевірено"))
    print("-" * 30)

    # Вивід даних для кожної вершини
    for vertex in distances:
        distance = distances[vertex]
        if distance == float('infinity'):
            distance = "∞"
        else:
            distance = str(distance)

        status = "Так" if vertex in visited else "Ні"
        print("{:<10} {:<10} {:<10}".format(vertex, distance, status))
    print("\n")


def dijkstra(graph, start):
    distances = {vertex: float('infinity') for vertex in graph.nodes}
    previous_nodes = {vertex: None for vertex in graph.nodes}
    distances[start] = 0
    unvisited = set(graph.nodes)
    visited = set()

    while unvisited:
        current_vertex = min(unvisited, key=lambda vertex: distances[vertex])

        if distances[current_vertex] == float('infinity'):
            break

        for neighbor in graph.neighbors(current_vertex):
            weight = graph[current_vertex][neighbor]['weight']
            distance = distances[current_vertex] + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous_nodes[neighbor] = current_vertex

        visited.add(current_vertex)
        unvisited.remove(current_vertex)

        # Вивід таблиці після кожного кроку
        # print_table(distances, visited)

    return distances, previous_nodes

def reconstruct_path(start, end, previous_nodes):
    path = []
    current = end
    while current != start:
        path.insert(0, current)
        current = previous_nodes[current]
    path.insert(0, start)
    return path