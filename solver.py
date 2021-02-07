import tours
import search
from itertools import permutations
from random import choice

reg_tours = tours.generate_instances(100)
reg_tours = [list(permutations(cities)) for cities in reg_tours]

optimal = search.brute_force(reg_tours)

# random tour
selected_tours = [list(choice(permus)) for permus in reg_tours]
search.random_tour(selected_tours)

# hill climbing with randomly selected starting points
min_costs = search.hill_climbing(selected_tours)

# count optimal tours and print out
num_optimal = sum(x == y for x,y in zip(min_costs, optimal))

print("OPTIMAL PATHS FOUND: " + str(num_optimal))
print()

'''
  for tours with lots of cities
 100 cities proved to take incredibly long, 
 50 gets the job done in a reasonable amount of time
'''
big_tours = tours.generate_instances(100, 50)
search.hill_climbing(big_tours)