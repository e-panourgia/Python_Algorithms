from sklearn.datasets import make_blobs
import numpy as np, matplotlib.pyplot as plt, random, pprint as pp
np.random.seed(42) # seed, it helps me for debugging !

def calculate_mean_of_cluster1(xx1 , yy1 , e = 0.000000000000001):
    """find global mean for the whole cluster 1"""
    # calculate x
    devision_x = len(xx1)
    sum_x = sum(xx1)
    mean_x = sum_x / (devision_x + e)
    # calculate y
    devision_y = len(xx1)
    sum_y = sum(yy1)
    mean_y = sum_y / (devision_y + e)
    return mean_x, mean_y

def calculate_mean_of_cluster2(xx2 , yy2):
    """find global mean for the whole cluster 2"""
    pass

def calculate_mean_of_cluster3(xx3, yy3):
    """find global mean for the whole cluster 3"""
    pass

def assing_node(node):
    """assign all nodes to clusters"""
    values_of_dict = min(node.dict_distances_from_center.values())
    center_to_assign = list(node.dict_distances_from_center.keys())[list(node.dict_distances_from_center.values()).index(values_of_dict)]
    return [center_to_assign, node]

class Node:
    """it stores an objects of form: {[xx, yy], {center1 : dist1, cenetr2 : dist2, cenetr3 : dist3}}"""
    def __init__(self, coordinates, dict_distances_from_center):
        self.coordinates = coordinates
        self.dict_distances_from_center = dict_distances_from_center

def calculate_euclidian_dist(xx, cc):
    """it calculates euclidean distance of a point xx with the center cc""" 
    return np.sqrt(np.sum((xx-cc) ** 2))

def select_points(list):
    """This function selects three data points, randomly"""
    point1 , point2, point3 = np.random.choice(len(list), size=3, replace=False)
    point1, point2, point3 = list[point1], list[point2], list[point3] # [-3.14887714 -9.05950487] ... [-0.30070027 -3.66805138]
    return point1, point2, point3

def calculateDistance_cluster_1(centroids1):
    """calculate all distances for all nodes from center 1"""
    list_centroids1 = [] # Initialize a list
    for i in range(len(x)):
        list_centroids1.append(calculate_euclidian_dist(centroids1, x[i])) # returns 500 values
    return list_centroids1

def calculateDistance_cluster_2(centroids2):
    """calculate all distances for all nodes from center 2"""
    list_centroids2 = []  # Initialize a list
    for i in range(len(x)):
        list_centroids2.append(calculate_euclidian_dist(centroids2, x[i]))  # returns 500 values
    return list_centroids2

def calculateDistance_cluster_3(centroids3):
    """calculate all distances for all nodes from center 3"""
    list_centroids3 = []  # Initialize a list
    for i in range(len(x)):
        list_centroids3.append(calculate_euclidian_dist(centroids3, x[i]))  # returns 500 values
    return list_centroids3

def find_indexes_of_mins(list1, list2, list3): return min(list1) , min(list2), min(list3)

if __name__ == "__main__":
    """Generate dataset to implement K-means algorithm"""
    global x
    global ITERATIONS # stopping condition 
    hold_centroids1, hold_centroids2, hold_centroids3 = [], [], [] # will store nodes (x)
    x, y = make_blobs(centers=3, n_samples=500, n_features=2, shuffle=True, random_state=40) # shape (500, 2)
    # a = plt.scatter(x[:, 0], x[:, 1], c=y)
    # plt.title("Generated data")
    # plt.show()
    centroids1, centroids2, centroids3 = select_points(x)
    list_center_1 = calculateDistance_cluster_1(centroids1) # list contains distances centroids1 and all x
    list_center_2 = calculateDistance_cluster_2(centroids2)  # list contains distances centroids2 and all x
    list_center_3 = calculateDistance_cluster_3(centroids3)  # list contains distances centroids3 and all x
    res1, res2, res3 = [x for x in range(len(list_center_1)) if list_center_1[x] == 0], [x for x in range(len(list_center_2)) if list_center_2[x] == 0], [x for x in range(len(list_center_3)) if list_center_3[x] == 0]
    list_center_1[res1[0]], list_center_2[res2[0]], list_center_3[res3[0]] = 1000, 1000, 1000
    min1, min2, min3 = find_indexes_of_mins(list_center_1, list_center_2, list_center_3) # not myself
    for i in range(len(x)):
        # apend centroids
        if i == 0: hold_centroids1.append(centroids1), hold_centroids2.append(centroids2), hold_centroids3.append(centroids3)
        node = Node(x[0], {'centroids1': list_center_1[i], "cenetr2" :  list_center_2[i], "centroids3" : list_center_3[i]})
        list_assign = assing_node(node)
        if list_assign[0] == "centroids1": hold_centroids1.append(list_assign[1])
        elif list_assign[0] == "centroids2": hold_centroids2.append(list_assign[1])
        elif list_assign[0] == "centroids3": hold_centroids3.append(list_assign[1])
    # calculate mean of each cluster 
    print(hold_centroids1)
    print(hold_centroids1[0]) # [xx, yy] append myself then nodes 
    print(hold_centroids1[0][0]) # xx
    print(hold_centroids1[0][1]) # yy 
    dict = vars(hold_centroids1[1]) # {cluster1 : dist1, cluster2 : dist2, clusteer3 : dist3} 
    print(type(dict))
    print(dict['coordinates'][0]) # xx
    xx_cluster1, xx_cluster2, xx_cluster3 = [], [], [] # Initialize xxs 
    yy_cluster1, yy_cluster2, yy_cluster3 = [], [], [] # Initialize xxs 
    for i in range(len(hold_centroids1)):    
        if i == 0:
            ## myself # TODO  
            continue
        dict = vars(hold_centroids1[i])
        xx = dict['coordinates'][0]
        yy = dict['coordinates'][1]
        xx_cluster1.append(xx)
        yy_cluster1.append(yy)
    mean_x, mean_y = calculate_mean_of_cluster1(xx_cluster1, yy_cluster1)
    print(centroids1,mean_x, mean_y)
# chech converenge 
## TODO calculate mean for 3 clusters for axis x , axis y 
## TODO fix all iterations 
## TODO converenge copy old with new 
## TODO generalize your code 
## Implement with HADOOP - power of parallel 
## TODO unittest 