import gurobipy as gp
from gurobipy import GRB
m = gp.Model()

MAX = int(1e9)

for _ in range(int(input())):
    a, b = map(int, input().split())

    k = m.addVar(0, MAX, vtype=GRB.INTEGER)
    x = m.addVar(0, MAX, vtype=GRB.INTEGER)
    y = m.addVar(0, MAX, vtype=GRB.INTEGER)

    m.addConstr((a+x)*k==b+y)
    m.setObjective(x+y, GRB.MINIMIZE)
    m.params.NonConvex = 2
    m.optimize()

    print(m.ObjVal, x.x, y.x)

