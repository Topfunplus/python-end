# -*- coding: utf-8 -*-

import csv
import networkx as nx
import matplotlib.pyplot as plt

# 打开node.csv 以读的方式， 编码方式为utf-8 读取文件内容到f
with open("node.csv", "r", encoding="utf-8") as f:
    reader = csv.reader(f)  # reader 是一个迭代器
    header = next(reader)  # 读取表头
    col1, col3 = [], []

    # 拿到迭代器中的每一行 row是一个列表
    for row in reader:
        col1.append(row[0])
        col3.append(row[2])

nodes = col1

nodes_size = list(map(float, col3))


# 打开edge.csv 以读的方式， 编码方式为utf-8 读取文件内容到f
with open("edge.csv", "r", encoding="utf-8") as f:
    reader = csv.reader(f)
    header = next(reader)  # 读取表头

column_data = [(row[0], row[1]) for row in reader]

edges = column_data


G = nx.Graph()

for charactor in nodes:
    G.add_node(charactor)

for edge in edges:
    G.add_edge(edge[0], edge[1])

fig, ax = plt.subplots(figsize=(10, 8))

pos = nx.random_layout(G)
nx.draw_networkx_nodes(G, pos, node_size=nodes_size, node_color="lightblue", ax=ax)
nx.draw_networkx_edges(G, pos)
nx.draw_networkx_labels(
    G, pos, font_size=10, font_family="sans-serif", font_color="black", ax=ax
)
plt.axis("off")
plt.savefig("networkx.png")

plt.show()
