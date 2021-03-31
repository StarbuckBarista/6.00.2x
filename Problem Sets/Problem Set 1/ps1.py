###########################
# 6.00.2x Problem Set 1: Space Cows 

from ps1_partition import get_partitions
import time

#================================
# Part A: Transporting Space Cows
#================================

def load_cows(filename):
    cow_dict = dict()

    f = open(filename, 'r')
    
    for line in f:
        line_data = line.split(',')
        cow_dict[line_data[0]] = int(line_data[1])
    return cow_dict

# Problem 1
def greedy_cow_transport(cows, limit = 10):
    cowsCopy = cows.copy()
    sortedCows = sorted(cowsCopy.items(), key = lambda cow: cow[1], reverse = True)

    trips = []

    while sum(cowsCopy.values()) > 0:
        ship = []
        totalCost = 0

        for cow, value in sortedCows:
            if cowsCopy[cow] != 0 and totalCost + value <= limit:
                ship.append(cow)
                totalCost += value
                cowsCopy[cow] = 0

        trips.append(ship)

    return trips

# Problem 2
def brute_force_cow_transport(cows, limit = 10):
    trip = []
    shortest = None

    for partition in get_partitions(cows):
        valid = True

        for ship in partition:
            if sum([cows[cowName] for cowName in ship]) > limit:
                valid = False

        if valid:
            if shortest == None or len(partition) < shortest:
                trip = partition
                shortest = len(partition)

    return trip

# Problem 3
def compare_cow_transport_algorithms():
    cows = {'Maggie': 3, 'Herman': 7, 'Betsy': 9, 'Oreo': 6, 'Moo Moo': 3, 'Milkshake': 2, 'Millie': 5, 'Lola': 2, 'Florence': 2, 'Henrietta': 9}

    greedyStart = time.time()
    greedy_cow_transport(cows)
    greedyTime = time.time() - greedyStart

    bruteForceStart = time.time()
    brute_force_cow_transport(cows)
    bruteForceTime = time.time() - bruteForceStart

    print(f"The Greedy Algorithm took {greedyTime} seconds")
    print(f"The Brute Force Algorithm took {bruteForceTime} seconds")

cows = load_cows("ps1_cow_data.txt")
limit = 100
print(cows)

print(greedy_cow_transport(cows, limit))
print(brute_force_cow_transport(cows, limit))
compare_cow_transport_algorithms()
