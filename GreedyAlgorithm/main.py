"""
Solving Set Covering Problem using Python.
"""
class Subset:
  """
    Representing Each Subset using class Subset
    with properties : id and coveredItems
  """
  # Constructor generate each subset.
  def __init__(self, id, lst):
        self.id = id
        # direct conversion of list to set
        self.coveredItems = set(lst)


def buildInput():
  """
    Fill each Subset with data 
    and hold all subset to a list named subsets.
    :return: a list with all subset. 
  """

  subsets = []
  s = Subset(1, [1, 2])
  subsets.append(s)
  s = Subset(2, [1, 2, 3])
  subsets.append(s)
  s = Subset(3, [3, 4, 5, 6])
  subsets.append(s)
  s = Subset(4, [2, 3, 4, 9])
  subsets.append(s)
  s = Subset(5, [4, 5, 6, 8])
  subsets.append(s)
  s = Subset(6, [6, 7])
  subsets.append(s)
  s = Subset(7, [7, 8])
  subsets.append(s)
  s = Subset(8, [5, 7, 8, 10])
  subsets.append(s)
  s = Subset(9, [4, 8, 9])
  subsets.append(s)
  s = Subset(10, [8, 10])
  subsets.append(s)
  return subsets

## find subset covers more uncovered ele from universe
def IdentifyMaximizingCoverage(remaining_subset_set, uncovered_universe_element_set):
    """
    find the subset that covers the most uncovered elements from universe.
    :param remaining_subset_set: shows the remaining subsets.
    :param uncovered_universe_element_set: shows the uncovered elements form universe.
    :return: the subset which covers the most uncovered elements from universe.
    """
    covered_elements = -1
    selected_subset = None
    for subset in remaining_subset_set:
        coverage = len(uncovered_universe_element_set.intersection(subset.coveredItems))
        if coverage > covered_elements:
            covered_elements = coverage
            selected_subset = subset
    return selected_subset


def RemoveCoveredUniverseElements(selected_subset: Subset, uncovered_universe_element_set):
    """
    Updates the data of problem.
    :param selected_subset: Represents the selected subset.
    :param uncovered_universe_element_set: shows the uncovered elements form universe.
    :return: None
    """
    for elem in selected_subset.coveredItems:
        uncovered_universe_element_set.discard(elem)

# produce universe with comprehensive list
universe = [i + 1 for i in range(0, 10)]
subsets = buildInput()

selected_subsets = []
uncoveredUniverseElementSet = set(universe)
remainingSubsetSet = set(subsets)

# Greedy Algorithm
while len(uncoveredUniverseElementSet) > 0:
    selected = IdentifyMaximizingCoverage(remainingSubsetSet, uncoveredUniverseElementSet)
    selected_subsets.append(selected)
    remainingSubsetSet.discard(selected)
    RemoveCoveredUniverseElements(selected, uncoveredUniverseElementSet)

# Print the final Solution of problem
print('Selected subsets:')
for sub in selected_subsets:
    print(sub.id)
print('The Objective function is :  ', len(selected_subsets))
