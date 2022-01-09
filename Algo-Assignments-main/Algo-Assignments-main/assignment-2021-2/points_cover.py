from itertools import chain, combinations
import sys
import argparse


class Line:
    points = []
    equation = ""
    def __init__(self, equation, points):
        self.points = points
        self.equation = equation

def data_grafos_1(filename):
    points = {} # Initialize
    i = 0 
    with open(filename) as input_file:
        for line in input_file:
            parts = line.split()
            parts_new = tuple(int(i) for i in parts)
            points[i] = parts_new
            i = i + 1
    return points

def getAllAvailableTuples(available_points):
    points = list(available_points.keys())
    points2 = list(available_points.keys())
    tuple_combinations = {}
    i = 0
    for point1 in points:
        for point2 in points2:
            if point1 == point2:
                continue
            tuple_combinations[i] = (point1, point2)
            i += 1
        
        points2.remove(point1)
    return tuple_combinations

def getLine(point1, point2):
    # Return (x, y)
    # return 11, None
    # return None, [a, b]

    if point1[0] == point2[0]:
        # x = x0
        # equation = "x = " + str(point1[0])
        return point1[0], None
    else:
        # y = ax + b
        a = (point2[1] - point1[1]) / (point2[0] - point1[0])

        b = point1[1] - (a * point1[0])
        # equation = str(a) + "*x + " + str(b)
        return None, [a, b]

def getEquations(points, available_tuples, g_flag):
    
    equation_dict = {}
    for point_tuple in available_tuples:
        
        equation = getLine(points[available_tuples[point_tuple][0]], points[available_tuples[point_tuple][1]])
        
        if g_flag:
            if equation[0] is not None or equation[1][0] == 0: 
                equation_dict[point_tuple] = Line(equation, [available_tuples[point_tuple][0], available_tuples[point_tuple][1]] )
        else:
            equation_dict[point_tuple] = Line(equation, [available_tuples[point_tuple][0], available_tuples[point_tuple][1]] )

    return equation_dict

def getDictionaryForSort(equation_dict):
    equations = {}

    for equationID in equation_dict:
        equations[equationID] = len(equation_dict[equationID].points)
    
    return equations

def powerset(iterable):
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))

def satisfies(equation_dict, combination, remaining_points):
    for lineID in combination:
        remaining_points = [point for point in remaining_points if point not in equation_dict[lineID].points]
    return len(remaining_points) == 0

def getOptimalLine(equation_dict, points, combinations, remaining_points_initial):

    optimal_combination = None
    
    for combination in combinations:
        remaining_points = [point for point in remaining_points_initial]
        if satisfies(equation_dict, combination, remaining_points):
            if optimal_combination is None or len(combination) < len(optimal_combination):
                optimal_combination = combination
    
    # We know the optimal combination here
    for lineID in optimal_combination:
        line = equation_dict[lineID]
        result = ""
        for pointID in line.points:
            result += " " + str(points[pointID])
        
        print(result)

parser = argparse.ArgumentParser(description='Points cover')

parser.add_argument('-f', action="store_true")
parser.add_argument('-g', action="store_true")
parser.add_argument('filename', type=str, help='filename')
args = parser.parse_args()



data = args.filename
points = data_grafos_1(data)
available_tuples = getAllAvailableTuples(points)
equation_dict = getEquations(points, available_tuples, args.g)

# Fill the points that an equation fills
for equationID in equation_dict:
    for point in points:
        x = points[point][0]
        y = points[point][1]
        # print("x: " + str(x) + " " + " y: " + str(y))
        if equation_dict[equationID].equation[0] is None:
            # y = ax + b
            # Check an epalitheuei
            a = equation_dict[equationID].equation[1][0]
            b = equation_dict[equationID].equation[1][1]
            result = a * x + b

            if result == y and not point in equation_dict[equationID].points:
                equation_dict[equationID].points.append(point)
                # print(equation_dict[equationID].points)
                
        else:
            x_value = equation_dict[equationID].equation[0]
            if x == x_value and not point in equation_dict[equationID].points:
                equation_dict[equationID].points.append(point)
                # print(equation_dict[equationID].points)

equation_dict_for_sort = getDictionaryForSort(equation_dict)
sorted_equation_dict = sorted(equation_dict_for_sort.items(), key=lambda x: x[1], reverse=True)


available_line_ids = []
for line in sorted_equation_dict:
    available_line_ids.append(line[0])

# for point in available_line_ids:
#     recursion(equation_dict, available_line_ids, list(points.keys()), point)



if args.f:
    # Full scan
    getOptimalLine(equation_dict, points, list(powerset(available_line_ids)), list(points.keys()))
else:
    remaining_points = list(points.keys())
    i = 0
    
    while len(remaining_points) > 0:
        if len(remaining_points) == 0:
            break
        # print(sorted_equation_dict[equationID])
        # for 
        equationID = sorted_equation_dict[0][0]
        i += 1


        check = any(item in equation_dict[equationID].points for item in remaining_points)
        
        if check:
            points_from_this_line = ""

            points_for_removal = []

            for point in equation_dict[equationID].points:
                
                
                if point in remaining_points:
                    remaining_points.remove(point) # Remove from remaining points

                    # Remove the points from the other lines
                    points_from_this_line += " " + str(points[point])
                    for eqID in equation_dict:
                        if point in equation_dict[eqID].points:
                            if eqID != equationID:
                                equation_dict[eqID].points.remove(point)
                            else:
                                points_for_removal.append(point)
            print(points_from_this_line)
            for point in points_for_removal:
                equation_dict[equationID].points.remove(point)
            equation_dict_for_sort = getDictionaryForSort(equation_dict)
            sorted_equation_dict = sorted(equation_dict_for_sort.items(), key=lambda x: x[1], reverse=True)
        else:
            continue
        