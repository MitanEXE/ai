import random

citys = [
    (0, 3), (0, 0),
    (0, 2), (0, 1),
    (1, 0), (1, 3),
    (2, 0), (2, 3),
    (3, 0), (3, 3),
    (3, 1), (3, 2)
]

l = len(citys)
path = list(range(l))
print("Initial path:", path)

def distance(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

def path_length(p):
    total_dist = 0
    for i in range(len(p)):
        total_dist += distance(citys[p[i]], citys[p[(i + 1) % len(p)]])
    return total_dist

def hill_climb(p):
    current_length = path_length(p)
    improved = True
    
    while improved:
        improved = False
        for i in range(len(p)):
            for j in range(i + 1, len(p)):
                new_path = p[:]
                new_path[i], new_path[j] = new_path[j], new_path[i]
                new_length = path_length(new_path)
                
                if new_length < current_length:
                    p = new_path
                    current_length = new_length
                    improved = True
                    break
            if improved:
                break
    
    return p, current_length

print('Initial path length:', path_length(path))

best_path, best_length = hill_climb(path)

print('Best path:', best_path)
print('Best path length:', best_length)
