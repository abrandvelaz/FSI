# Search methods

import search

#ab = search.GPSProblem('A', 'B'
#                       , search.romania)
#
#print("Anchura: ", search.breadth_first_graph_search(ab).path()) # Búsqueda por amplitud/anchura
#print("Profundidad: ", search.depth_first_graph_search(ab).path())   # Búsqueda por profundidad

print("--------------------------Comparacion RyA y RyA subestimacion---------------------")

ab = search.GPSProblem('A', 'B'
                       , search.romania)
print("Ramificación y acotación: ", search.rya_graph_search(ab).path()) # Búsqueda por ramificación y acotación
print("Ramificación y acotación con estimación: ", search.rya_subest_graph_search(ab).path()) # Búsqueda por ramificación y acotación con estimación


print("--------------------------Comparacion RyA y RyA subestimacion---------------------")

ab = search.GPSProblem('A', 'D'
                       , search.romania)
print("Ramificación y acotación: ", search.rya_graph_search(ab).path()) # Búsqueda por ramificación y acotación
print("Ramificación y acotación con estimación: ", search.rya_subest_graph_search(ab).path()) # Búsqueda por ramificación y acotación con estimación

print("--------------------------Comparacion RyA y RyA subestimacion---------------------")

ab = search.GPSProblem('A', 'Z'
                       , search.romania)
print("Ramificación y acotación: ", search.rya_graph_search(ab).path()) # Búsqueda por ramificación y acotación
print("Ramificación y acotación con estimación: ", search.rya_subest_graph_search(ab).path()) # Búsqueda por ramificación y acotación con estimación

# Result:
# [<Node B>, <Node P>, <Node R>, <Node S>, <Node A>] : 101 + 97 + 80 + 140 = 418
# [<Node B>, <Node F>, <Node S>, <Node A>] : 211 + 99 + 140 = 450
# [<Node B>, <Node P>, <Node R>, <Node S>, <Node A>] : 140 + 80 + 97 + 101 = 418