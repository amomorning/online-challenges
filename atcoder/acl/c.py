import networkx as nx


n, m = map(int, input().split())

G = nx.Graph()
G.add_nodes_from(range(n))

for i in range(m):
    u, v = map(int, input().split())
    G.add_edge(u-1, v-1)

print(nx.number_connected_components(G)-1)
