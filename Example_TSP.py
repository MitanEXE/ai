import random
import math

def distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def total_distance(path, cities):
    dist = 0
    for i in range(len(path) - 1):
        dist += distance(cities[path[i]], cities[path[i+1]])
    dist += distance(cities[path[-1]], cities[path[0]])  # Return to the starting city
    return dist

def generate_random_solution(cities):
    return random.sample(range(len(cities)), len(cities))

def generate_neighbor_solution(solution):
    neighbor = solution[:]
    i, j = random.sample(range(len(solution)), 2)
    neighbor[i], neighbor[j] = neighbor[j], neighbor[i]
    return neighbor

def hill_climbing(cities, max_iter):
    current_solution = generate_random_solution(cities)
    current_cost = total_distance(current_solution, cities)
    
    for i in range(max_iter):
        neighbor_solution = generate_neighbor_solution(current_solution)
        neighbor_cost = total_distance(neighbor_solution, cities)
        
        if neighbor_cost < current_cost:
            current_solution = neighbor_solution
            current_cost = neighbor_cost
    
    return current_solution, current_cost

cities = [(0, 0), (1, 2), (3, 1), (5, 2), (4, 0)]

best_solution, best_cost = hill_climbing(cities, 1000)
print("Best solution:", best_solution)
print("Best cost:", best_cost)
