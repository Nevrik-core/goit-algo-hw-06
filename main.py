from graph_module import create_ukraine_graph

import matplotlib.pyplot as plt
import networkx as nx

G_ukraine = create_ukraine_graph()

# Координати міст для візуалізації
city_positions = {
    "Київ": (50.45, 30.52), "Харків": (49.98, 36.23), "Одеса": (46.47, 30.73),
    "Дніпро": (48.45, 35.05), "Львів": (49.83, 24.01), "Запоріжжя": (47.82, 35.17),
    "Миколаїв": (46.96, 32.0), "Івано-Франківськ": (48.92, 24.71), "Вінниця": (49.23, 28.48),
    "Полтава": (49.59, 34.54), "Ялта": (44.49, 34.16)
}
graph_positions = {city: (coord[1], coord[0]) for city, coord in city_positions.items()}

plt.figure(figsize=(10, 8))
nx.draw(G_ukraine, pos=graph_positions, with_labels=True, node_color='orange', node_size=2000, font_size=12, font_weight='bold')
plt.title("Граф Основних Міст України (Схематична Карта)")
plt.show()

# Аналіз основних характеристик графа
print("Кількість міст (вершин):", G_ukraine.number_of_nodes())
print("Кількість зв'язків (ребер):", G_ukraine.number_of_edges())
print("Ступінь кожного міста (вершини):")
for city, degree in G_ukraine.degree():
    print(f"{city}: {degree}")