from pulp import *

prob = LpProblem("Maximize_Function", LpMaximize)

x = LpVariable("x", lowBound=0)
y = LpVariable("y", lowBound=0)
z = LpVariable("z", lowBound=0)

prob += 3 * x + 2 * y + 5 * z

prob += x + y <= 10
prob += 2 * x + z <= 9
prob += y + 2 * z <= 11

prob.solve()

print("最大值:", value(prob.objective))
print("x:", value(x))
print("y:", value(y))
print("z:", value(z))
