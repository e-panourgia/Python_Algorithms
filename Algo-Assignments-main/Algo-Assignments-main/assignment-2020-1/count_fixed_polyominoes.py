# TODO order graph , implement pseudocode
# import libaries 
import pprint as pp

from numpy import size

def is_empty(untried):
    """Implementation function for terminal condition of recursion"""
    return len(untried) == 0

def RemoveFromSet(untried):
    pass

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
    list = [] # Initialize a list 
    while not is_empty(untried):
        u = RemoveFromSet(untried)
        list.append(p, u)
        
        pass


    return c

def produce_nodes(n):
    """Fix graph based on the size polynominos given from terminan(cmd)"""
    begin = (0,0)
    horizontally_right = [] 
    intermediate = (0,1)
    horizontally_left = [] 

    for i in range(n):
        horizontally_right.append((i,0))
    
    for i in range(n-1):
        result_x = intermediate[0] - i
        horizontally_left.append((result_x,1))
    list_border = horizontally_right + horizontally_left
    list_border_backup = []
    # produce possible solution space 
    k, m = n, n
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
    # sort keys to find them with the proper order
    list_nodes.sort(key=lambda y: y[0])
    hold_neigbours = []
    # create connectors 
    for i in range(len(list_nodes)):
        list_tuple = []
        x = list_nodes[i][0]
        y = list_nodes[i][1]
        x_plus = x + 1
        x_minus = x - 1
        y_plus = y + 1
        y_minus = y - 1
        # possible tuple to check 
        tuple_1 = (x_minus, y)
        tuple_2 = (x_plus, y) 
        tuple_3 = (x, y_minus)
        tuple_4 = (x, y_plus)
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
    G = {} # Initialize python-dict
    for i in range(len(keys)):
        G[keys[i]] = neighbours[i]
    return G
## Initialize parameters to call the main function 
n = 5 
list_nodes = produce_nodes(n)
neighbours, keys = create_graph(list_nodes)
G = create_final_graph(neighbours, keys)
untried={(0,0)}
p = []
# call main function that solve the problem 
c = CountFixedPolynoes(G, untried, n, p, c=0)
# print final output
pp.pp(G)
print(c)