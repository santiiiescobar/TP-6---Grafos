import networkx as nx

G = nx.Graph()

ambientes = ["cocina", "comedor", "cochera", "quincho", "baño1", "baño2", "habitacion1", "habitacion2", "sala_de_estar", "terraza", "patio"]
G.add_nodes_from(ambientes)

aristas = [
    ("cocina", "comedor", 5),
    ("cocina", "cochera", 8),
    ("comedor", "quincho", 6),
    ("quincho", "sala_de_estar", 7),
    ("habitacion1", "habitacion2", 4),
    ("habitacion1", "sala_de_estar", 9),
    ("sala_de_estar", "terraza", 3),
    ("terraza", "patio", 5),
]

G.add_weighted_edges_from(aristas)

arbol_expansion_minima = nx.minimum_spanning_tree(G)
longitud_total_cables = sum(arbol_expansion_minima[e[0]][e[1]]['weight'] for e in arbol_expansion_minima.edges())

print(f"Árbol de expansión mínima: {arbol_expansion_minima.edges()}")
print(f"Longitud total de cables necesarios: {longitud_total_cables} metros")

camino_mas_corto = nx.shortest_path(G, source="habitacion1", target="sala_de_estar")
longitud_camino_mas_corto = nx.shortest_path_length(G, source="habitacion1", target="sala_de_estar")

print(f"Camino más corto desde habitacion1 hasta sala_de_estar: {camino_mas_corto}")
print(f"Longitud del camino más corto: {longitud_camino_mas_corto} metros")
