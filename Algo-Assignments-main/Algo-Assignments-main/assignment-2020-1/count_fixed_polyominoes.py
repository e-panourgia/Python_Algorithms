import argparse, pprint as pp # import libraries 
class Counter:
    def __init__(self):
        self.counter = 0

def CountFixedPolynoes(G, untried, n, p, c):
    """
        Input :
        - G, G = (V, E), a graph
        - untried, a set of nodes
        - n, the size polyominos    
        - p, the current polynomino 
        - c, a counter
        Output : 
        - r, the number of polynominoes of size n
    """
    while not (len(untried) == 0): # Stopping Condition
        u = untried.pop()
        p.append(u)
        if len(p) == n: c.counter = c.counter + 1
        else:
            new_neighbors, ps_except_u_neighbors = set(), [j for i in p if i != u for j in G[i]]
            for v in G[u]: 
                if (v not in untried) and (v not in p) and (v not in ps_except_u_neighbors): new_neighbors.add(v)
            new_untried = untried.union(new_neighbors)
            CountFixedPolynoes(G, new_untried, n, p, c) # recursion
        p.remove(u)
    return c.counter

def produce_nodes(n):
    """Fix graph based on the size polynominos given from terminan(cmd)"""
    begin, horizontally_right, intermediate, horizontally_left = (0,0), [], (0, 1), [] # Initialize
    for i in range(n): horizontally_right.append((i,0))
    for i in range(n-1):
        result_x = intermediate[0] - i
        horizontally_left.append((result_x,1))
    list_border = horizontally_right + horizontally_left
    list_border_backup = []
    # produce possible solution space 
    k, m = n, n # helpful counters 
    for i in range(len(list_border)): 
        creator = list_border[i]
        if creator[1] == 0: 
            for i in range(k): 
                list_border_backup.append((creator[0], creator[1]+i))
            k -= 1    
        elif creator[1] == 1:
            for i in range(m-1):
                if creator == (0,1):
                    continue
                list_border_backup.append((creator[0], creator[1]+i))
            m -= 1
    return list_border_backup

def create_graph(list_nodes):
    list_nodes.sort(key=lambda y: y[0]) # sort keys to find them with the proper order
    hold_neigbours = []
    # create connectors 
    for i in range(len(list_nodes)):
        list_tuple = []
        x, y = list_nodes[i][0], list_nodes[i][1]
        x_plus = x + 1
        x_minus = x - 1
        y_plus = y + 1
        y_minus = y - 1
        # possible tuple to check 
        tuple_1, tuple_2, tuple_3, tuple_4 = (x_minus, y), (x_plus, y), (x, y_minus), (x, y_plus)
        list_tuple.append(tuple_1)
        list_tuple.append(tuple_2)
        list_tuple.append(tuple_3)
        list_tuple.append(tuple_4)
        sub_list = []
        for f in range(len(list_tuple)):
           if list_tuple[f] in list_nodes:
                sub_list.append(list_tuple[f]) 
        hold_neigbours.append(sub_list)
    return hold_neigbours,list_nodes

def create_final_graph(neighbours, keys):
    """Return final Grapgh(G)"""
    G = {} # Initialize python-dict
    for i in range(len(keys)):
        G[keys[i]] = neighbours[i]
    return G
parser = argparse.ArgumentParser() # Fix Parameters 
parser.add_argument("n", type=int, help="the size polyominoes")
parser.add_argument("-p", help="print graph(G)", action="store_true")
args = parser.parse_args()
n = args.n
list_nodes = produce_nodes(n)
neighbours, keys = create_graph(list_nodes)
G = create_final_graph(neighbours, keys)
if args.p: # print Graph
    pp.pprint(G)
print(CountFixedPolynoes(G, {(0, 0)}, n, [], Counter())) # call main function solves the problem ! 