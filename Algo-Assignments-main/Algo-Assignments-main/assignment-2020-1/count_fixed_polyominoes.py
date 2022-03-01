""""
Strategy 
1. filter - Create Graph 
2. Implement pseudocode 
"""

# import libaries 


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


    pass

def fix_graph(n):
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
    k = n
    m = n
    for i in range(len(list_border)): ## all meria
        creator = list_border[i]
        if creator[1] == 0: 
            for i in range(k): # all n first colona
                list_border_backup.append((creator[0], creator[1]+i))
            k -= 1    
    
        elif creator[1] == 1:
            for i in range(m-1):
                if creator == (0,1):
                    continue
                list_border_backup.append((creator[0], creator[1]+i))
            m -= 1
    print(list_border_backup)

    # filter
    #create final graph 
    #list_all_nodes = list_border.copy()

    exit()
    #return G
    

## Initialize parameters to call the main function 
n = 5 
G = fix_graph(n)
print(G)
# untried={(0,0)}
# p = []
# # call main function that solve the problem 
# CountFixedPolynoes(G, untried, n, p, c=0)