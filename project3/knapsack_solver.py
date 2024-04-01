from pulp import *

def knapsack_solver(capacity, costs, values):
    # ナップサック問題を解くアルゴリズムを実装
    items = [i for i in range(len(costs))]
    prob = pulp.LpProblem(sense = LpMaximize)
    x = LpVariable.dicts("x", (items), cat="Binary")
    prob += lpSum(values[i] * x[i] for i in items)
    prob += lpSum(costs[i] * x[i] for i in items) <= capacity
    result = prob.solve() 
    selected_items = [i for i in items if x[i].value() == 1]
    opt_value = prob.objective.value()
    opt_cost = 0
    for i in items:
        if x[i].value() == 1:
            opt_cost += costs[i]
    return selected_items, opt_value, opt_cost