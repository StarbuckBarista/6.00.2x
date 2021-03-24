# MIT 6.00.2x Notes

## Lecture 1
* Optimization Models are good for answering questions such as the biggest, smallest, most, fewest, fastest, slowest, etc...
* Optimization Models have two parts; an objective function that should be minimized or maximized, and a set of constraints (possibly empty) that must be honored.
* It's much easier to reduce a new problem to an already answered problem that can be solved rather than creating your own solution.
* Optimization Problems are really slow to compute, Greedy Algorithms are often used instead to find an approximate solution that is "good enough".
* The Knapsack Problem is a problem in which you have some items with different weighted values and you must decide which to take without exceeding a set constraint.
* A 0/1 Knapsack Problem means that the items are whole, you either take the whole item or you don't take it at all.
* Brute Force Algorithms generate every possible combination of items (called a power set), remove all combinations that do not follow the given constraints, and pick out the combination(s) with the best value from those remaining.
* Brute Force Algorithms can often be unpractical because of how large power sets can get, and since Brute Force Algorithms are exponential, they perform terribly with large power sets.
* The Knapsack Problem is inherently exponential, there is no solution that will not be exponential.
* There still are good methods for finding approximate solutions to Knapsack Problems that work almost all of the time.

## Lecture 2
* Greedy Algorithms are a common replacement for Optimization Models as they are much quicker and provide an approximate solution.
* Greedy Algorithms work by choosing the best available item in which the constraints are met.
* What defines the "best" item to choose in a Greedy Algorithm?
* Modularity in programming can be very useful and is a very important aspect of good programming.
```Python
def greedy(items: list, maxCost: int, keyFunction):
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
* Lambda functions can be extremely useful for basic funtions, but you should always define proper functions when dealing with more advanced computation.
* Greedy Algorithms usual finds a Local Optimum which is not necessarily the Global Optimum.
* Any one Key Function will not always give you the best approximate answer, there is no way to tell which Key Function will provide the best answer.
* Greedy Algoritms are easy to implement and computationally effecient, but they do not always provide the best solution.
