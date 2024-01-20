from graph_module import create_ukraine_graph
from collections import deque

from bfs import bfs_recursive
from dfs import dfs_recursive

G_ukraine = create_ukraine_graph()

print("DFS шлях:")
dfs_path = dfs_recursive(G_ukraine, "Київ")
print("\n")

print("BFS шлях:")
queue = deque(["Київ"])
bfs_path = bfs_recursive(G_ukraine, queue)