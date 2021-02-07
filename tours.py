from random import seed, random
from math import sqrt

# create num_cities random coordinates
def generate_cities(num_cities):
    seed()
    return [(random(), random()) for _ in range(num_cities)]

# create number instances and call generate_cities
def generate_instances(number=100, num_cities=7):
    return [generate_cities(num_cities) for _ in range(number)]

# calculates the total distance for one tour
def calc_distance(city_perm):
    city_one = city_perm[0]
    cost = 0
    for city in city_perm:
        city_two = city
        dist = (city_one[0] - city_two[0]) ** 2 + (city_one[1] - city_two[1]) ** 2
        cost += sqrt(dist) if dist != 0 else 0
        city_one = city
    cost += sqrt((city_perm[-1][0] - city_perm[0][0]) ** 2 + (city_perm[-1][1] - city_perm[0][1]) ** 2)

    return cost



