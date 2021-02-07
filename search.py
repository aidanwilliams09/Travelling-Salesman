import analytics
import tours
from random import choice

def brute_force(tours_list=[]):
    costs = []
    
    # traverse every permutation and find cost
    for tour in tours_list:
        costs.append([tours.calc_distance(permu) for permu in tour])

        
    min_of_tours = analytics.analyze_min([analytics.analyze_min(cost) for cost in costs])
    max_of_tours = analytics.analyze_max([analytics.analyze_max(cost) for cost in costs])
    mean_of_tours = analytics.analyze_mean([analytics.analyze_mean(cost) for cost in costs])
    std_of_tours = analytics.analyze_std([analytics.analyze_std(cost) for cost in costs])

    print("BRUTE FORCE")
    print("---------------------------")
    print("MIN: " + str(min_of_tours))
    print("MAX: " + str(max_of_tours))
    print("MEAN: " + str(mean_of_tours))
    print("STD DEV: " + str(std_of_tours))
    print()

    return [analytics.analyze_min(cost) for cost in costs]

def random_tour(selected_tours=[]):

    costs = [tours.calc_distance(a_tour) for a_tour in selected_tours]
    min_of_choice = analytics.analyze_min(costs)
    max_of_choice = analytics.analyze_max(costs)
    mean_of_choice = analytics.analyze_mean(costs)
    std_of_choice = analytics.analyze_std(costs)

    print("BASELINE")
    print("---------------------------")
    print("MIN: " + str(min_of_choice))
    print("MAX: " + str(max_of_choice))
    print("MEAN: " + str(mean_of_choice))
    print("STD DEV: " + str(std_of_choice))
    print()

def hill_climbing(selected_tours=[]):
    min_costs = []

    # go through each randomly generated tour with a random starting location
    for tour in selected_tours:
        cur_cost = tours.calc_distance(tour)
        cur_tour = tour
        # loop until no neighbors are better than the current best
        while True:
            # cut list in 3 parts, flip the middle section, and restitch
            neighbors = [cur_tour[:i] + cur_tour[i:j][::-1] + cur_tour[j:] 
            for i in range(0,len(cur_tour) - 2) for j in range(i+2, len(cur_tour))]
            
            costs = [tours.calc_distance(neighbor) for neighbor in neighbors]
            new_cost = min(costs)
            new_tour = neighbors[costs.index(new_cost)]
            if new_cost >= cur_cost:
                min_costs.append(cur_cost)
                break
            else:
                cur_cost = new_cost
                cur_tour = new_tour


    min_of_choice = analytics.analyze_min(min_costs)
    max_of_choice = analytics.analyze_max(min_costs)
    mean_of_choice = analytics.analyze_mean(min_costs)
    std_of_choice = analytics.analyze_std(min_costs)

    print("HILL-CLIMBING")
    print("---------------------------")
    print("MIN: " + str(min_of_choice))
    print("MAX: " + str(max_of_choice))
    print("MEAN: " + str(mean_of_choice))
    print("STD DEV: " + str(std_of_choice))
    print()

    return min_costs
