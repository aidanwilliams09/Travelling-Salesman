# Travelling-Salesman
A basic implementation of the traveling salesman problem that solves it using brute force and hill climbing with 2-opt search. Each run will create 100 instances with x amount of random cities and produce a readout of the minimum, maximum, and mean path as well as the standard deviation between them. Additionally, if brute force and hill climbing are run, hill climbing reports the total number of optimal paths.

# Requirements
* python 3: instructions to download can be found at https://realpython.com/installing-python/

# Installation and Usage
1. Clone the repository locally
2. cd into folder with solver.py
3. Run command "python3 solver.py"
4. Amount of instances and cities per instance can be modified in solver.py by changing ***number*** to the new number of instances you want and ***num_cities*** to however many cities per instance you want in **tours.generate_instances()**
 
# Contributors

* Aidan Williams
