inputs = """
COM)B
B)C
C)D
D)E
E)F
B)G
G)H
D)I
E)J
J)K
K)L
"""

file1 = open("day6_input.txt","r") 
inputs = file1.readlines() 
file1.close() 

s2 = [x.replace('\n','').split(')') for x in inputs if x]

# Make dict for graph
orbit_graph = {}
for x in s2:
    try:
        orbit_graph[x[1]] = x[0]
    except:
        print(x)


# Traverse all 
orbits = 0
for k,v in orbit_graph.items():
    current_key = k
    while current_key != 'COM':
        try:
            next_key = orbit_graph[current_key]
            orbits +=1
            current_key = next_key
        except:
            print('EROR', current_key)
            break

print(orbits)

# Part two
import networkx as nx

# Make dict for graph
G=nx.Graph()

# Add nodes
for k,v in orbit_graph.items():
    G.add_node(k)

# Add edges
for x in s2:
    G.add_edge(x[1],x[0])

#  shortest path
nx.shortest_path_length(G, source=orbit_graph.get('YOU'), target= orbit_graph.get('SAN'), weight=None)
