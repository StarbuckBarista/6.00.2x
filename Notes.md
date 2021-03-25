# MIT 6.00.2x Notes

## Lecture 1 - Optimization and the Knapsack Problem
* Optimization Models are good for answering questions such as the biggest, smallest, most, fewest, fastest, slowest, etc...
* Optimization Models have two parts; an objective function that should be minimized or maximized, and a set of constraints (possibly empty) that must be honored.
* It's much easier to reduce a new problem to an already answered problem that can be solved rather than creating your solution.
* Optimization Problems are really slow to compute, Greedy Algorithms are often used instead to find an approximate solution that is "good enough".
* The Knapsack Problem is a problem in which you have some items with different weighted values and you must decide which to take without exceeding a set constraint.
* A 0/1 Knapsack Problem means that the items are whole, you either take the whole item or you don't take it at all.
* Brute Force Algorithms generate every possible combination of items (called a power set), remove all combinations that do not follow the given constraints and pick out the combination(s) with the best value from those remaining.
* Brute Force Algorithms can often be unpractical because of how large power sets can get, and since Brute Force Algorithms are exponential, they perform terribly with large power sets.
* The Knapsack Problem is inherently exponential, no solution will not be exponential.
* There still are good methods for finding approximate solutions to Knapsack Problems that work almost all of the time.
* Greedy Algorithms are a common replacement for Optimization Models as they are much quicker and provide an approximate solution.
* Greedy Algorithms work by choosing the best available item in which the constraints are met.
* What defines the "best" item to choose in a Greedy Algorithm?
* Modularity in programming can be very useful and is a very important aspect of good programming.
```Python
def greedy(items, maxCost, keyFunction):
    itemsCopy = sorted(items, key = keyFunction, reverse = True) # Sorts the items from best to worst based on our definition of the "best" item defined in keyFunction

    result = []
    totalValue, totalCost = 0.0, 0.0

    for i in range(len(itemsCopy)): # Iterates in the order of best items to the worst items
        if (totalCost + itemsCopy[i].getCost()) <= maxCost: # Ensures that we do not exceed our limit
            result.append(itemsCopy[i])
            totalCost += itemsCopy[i].getCost()
            totalValue += itemsCopy[i].getValue()

    return (result, totalValue)
```
* The Greedy Algorithm shown above has a Time Complexity of n log n because our sort function is has a Time Complexity of n log n and our iteration over itemsCopy has a Time Complexity of n.
* Lambda functions can be extremely useful for basic functions, but you should always define proper functions when dealing with more advanced computation.
* Greedy Algorithms usually find a Local Optimum which is not necessarily the Global Optimum.
* Anyone Key Function will not always give you the best approximate answer, there is no way to tell which Key Function will provide the best answer.
* Greedy Algorithms are easy to implement and computationally efficient, but they do not always provide the best solution.

## Lecture 2 - Decision Trees and Dynamic Programming
* The process of Brute Force algorithms can be implemented into code using a Search Tree.
* Search Trees inbuilt top down starting with the root, and the first element is selected from the group of items.
* If that item meets the constraints, a node is constructed that reflects a consequence of choosing to take that item (left child), and the consequences of that action (right child).
* The process is then applied recursively to non-leaf children.
* Left-first, depth-first enumeration is when you always choose the left decision first to the bottom of the tree, then to begin backing up to the next decision.
* Brute Force Algorithms are guaranteed to find the most optimal solution because it shows all possible combinations.
* Time is based on the number of nodes in the Search Tree.
* To find the number of nodes there will be, look at the number of levels in the tree and the number of nodes per level.
* The number of levels is the number of items to choose from, and the number of nodes at level *i* is *2<sup>i</sup>*
* If there are *n* items, the number of nodes can be shown as:
![number_of_nodes](http://latex.codecogs.com/svg.latex?%5Csum_%7Bi%3D0%7D%5E%7Bi=n%7D2^i)
* The Search Tree can be simplified by stopping the continuation of the tree once the constraints are broken.
```Python
def maxVal(toConsider, avail):
    """Assumes toConsider a list of items, avail a weight
    Returns a tuples of the total value of a solution to the 0/1 knapsack
    problem and the items of that solution"""
    if toConsider == [] or avail == 0: # Stops the exploration of that path as there are no longer available items or the constraint has been broken
        result = (0, ())
    elif toConsider[0].getCost() > avail: # Explorting the right branch only because the left branch would break the constraint
        result = maxVal(toConsider[1:], avail)
    else:
        nextItem = toConsider[0]

        # Left branch
        withVal, withToTake = maxVal(toConsider[1:], avail - nextItem.getCost())
        withVal += nextItem.getValue()

        # Right branch
        withoutVal, withoutToTake = maxVal(toConsider[1:], avail)

        # Explore the better branch
        if withVal > withoutVal:
            result = (withVal, withToTake + (nextItem,))
        else:
            result = (withoutVal, withoutToTake)
    return result
```
* Brute Force Algorithms can get slow, really quickly, it's exponential of course.
* Exponential Programs are in theory hopeless, but not in practice with Dynamic Programming.
* Dynamic Programming uses Memoization to use space rather than time.
* Dynamic Programming works well for problems with Optimal Substructure and Overlapping Subproblems.
* Optimal Substructure is when a globally optimal solution can be found by combining optimal solutions to local subproblems.
* Overlapping Subproblems is when finding an optimal solution involves solving the same problem multiple times.
* Dynamic Programming can be useful in Knapsack Problems in some cases, these cases being where the remaining room in the knapsack is the same.
* Computational Complexity can be very subtle.
