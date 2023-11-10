import networkx as nx

G = nx.Graph()

maravillas = [
    {"nombre": "Machu Picchu", "pais": "Perú", "tipo": "arquitectonica"},
    {"nombre": "Chichén Itzá", "pais": "México", "tipo": "arquitectonica"},
    {"nombre": "Coliseo Romano", "pais": "Italia", "tipo": "arquitectonica"},
    {"nombre": "Gran Muralla China", "pais": "China", "tipo": "arquitectonica"},
    {"nombre": "Petra", "pais": "Jordania", "tipo": "arquitectonica"},
    {"nombre": "Cristo Redentor", "pais": "Brasil", "tipo": "arquitectonica"},
    {"nombre": "Amazonia", "pais": "Brasil", "tipo": "natural"},
    {"nombre": "Bahía de Ha Long", "pais": "Vietnam", "tipo": "natural"},
    {"nombre": "Cataratas del Iguazú", "pais": "Argentina", "tipo": "natural"},
    {"nombre": "Monte Everest", "pais": "Nepal", "tipo": "natural"},
    {"nombre": "Parque Nacional de Yellowstone", "pais": "Estados Unidos", "tipo": "natural"},
    {"nombre": "Pirámides de Giza", "pais": "Egipto", "tipo": "arquitectonica"},
]

for maravilla in maravillas:
    G.add_node(maravilla["nombre"], pais=maravilla["pais"], tipo=maravilla["tipo"])

aristas = [
    ("Machu Picchu", "Chichén Itzá", 300),
    ("Machu Picchu", "Coliseo Romano", 800),
    ("Machu Picchu", "Gran Muralla China", 2500),
    ("Machu Picchu", "Petra", 1500),
    ("Machu Picchu", "Cristo Redentor", 4000),
    ("Machu Picchu", "Pirámides de Giza", 10000),
    ("Chichén Itzá", "Coliseo Romano", 1200),
    ("Chichén Itzá", "Gran Muralla China", 2800),
]

G.add_weighted_edges_from(aristas)

for nodo in G.nodes(data=True):
    print(f"Nombre: {nodo[0]}, País: {nodo[1]['pais']}, Tipo: {nodo[1]['tipo']}")

arquitectonicas = [nodo for nodo, datos in G.nodes(data=True) if datos["tipo"] == "arquitectonica"]
naturales = [nodo for nodo, datos in G.nodes(data=True) if datos["tipo"] == "natural"]

arbol_expansion_minima_arq = nx.minimum_spanning_tree(G.subgraph(arquitectonicas))
arbol_expansion_minima_nat = nx.minimum_spanning_tree(G.subgraph(naturales))

print(f"\nÁrbol de expansión mínima maravillas arquitectónicas: {arbol_expansion_minima_arq.edges()}")
print(f"\nÁrbol de expansión mínima maravillas naturales: {arbol_expansion_minima_nat.edges()}")
print(f"Longitud total del árbol de expansión mínima maravillas naturales: {sum(arbol_expansion_minima_nat[e[0]][e[1]]['weight'] for e in arbol_expansion_minima_nat.edges())}")

paises_arq = set([datos["pais"] for nodo, datos in G.nodes(data=True) if datos["tipo"] == "arquitectonica"])
paises_nat = set([datos["pais"] for nodo, datos in G.nodes(data=True) if datos["tipo"] == "natural"])

paises_con_ambos = paises_arq.intersection(paises_nat)

print(f"\nPaises con maravillas arquitectónicas y naturales: {paises_con_ambos}")

paises_con_mas_de_una_arq = [pais for pais in paises_arq if sum(1 for nodo, datos in G.nodes(data=True) if datos["tipo"] == "arquitectonica" and datos["pais"] == pais) > 1]
paises_con_mas_de_una_nat = [pais for pais in paises_nat if sum(1 for nodo, datos in G.nodes(data=True) if datos["tipo"] == "natural" and datos["pais"] == pais) > 1]

print(f"\nPaises con más de una maravilla arquitectónica: {paises_con_mas_de_una_arq}")
print(f"Paises con más de una maravilla natural: {paises_con_mas_de_una_nat}")
