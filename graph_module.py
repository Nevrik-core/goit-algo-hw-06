import networkx as nx

def create_ukraine_graph():
    G_ukraine = nx.Graph()

    cities = ["Київ", "Харків", "Одеса", "Дніпро", "Львів", "Запоріжжя", "Миколаїв", "Івано-Франківськ", "Вінниця", "Полтава", "Ялта"]
    G_ukraine.add_nodes_from(cities)

    connections = [
        ('Київ', 'Харків', 489),
        ('Київ', 'Дніпро', 479),
        ('Київ', 'Львів', 541),
        ('Харків', 'Дніпро', 221),
        ('Одеса', 'Миколаїв', 135),
        ('Львів', 'Івано-Франківськ', 135),
        ('Запоріжжя', 'Дніпро', 85),
        ('Одеса', 'Київ', 474),
        ('Вінниця', 'Київ', 281),
        ('Полтава', 'Харків', 143),
        ('Ялта', 'Миколаїв', 441),
        ('Вінниця', 'Львів', 363),
        ('Вінниця', 'Івано-Франківськ', 365),
        ('Вінниця', 'Одеса', 425),
        ('Одеса', 'Миколаїв', 135),
        ('Полтава', 'Київ', 352),
        ('Дніпро', 'Миколаїв', 327),
        ('Миколаїв', 'Запоріжжя', 392)
    ]

    G_ukraine.add_weighted_edges_from(connections)

    return G_ukraine

