from statistics import mean, stdev

# some simple helper methods to get required analytics
# can be expanded to include data visualizations using matplotlib
def analyze_mean(costs=[]):
    return mean(costs)

def analyze_min(costs=[]):
    return min(costs)

def analyze_max(costs=[]):
    return max(costs)

def analyze_std(costs=[]):
    return stdev(costs)