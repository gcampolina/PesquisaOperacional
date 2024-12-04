from ortools.linear_solver import pywraplp
from projetopo.utils.ler_csv import ler_csv
import os

def solver_nutrientes(nutrientes):

    pasta_atual = os.path.dirname(os.path.abspath(__file__))
    diretorio = os.path.join(pasta_atual, "taco.csv")
    data = ler_csv(diretorio)
    #print(data)

    solver = pywraplp.Solver.CreateSolver("GLOP")

    for nutriente in nutrientes:
        if nutriente[2] == -1:
            nutriente[2] = solver.infinity()
    print(nutrientes)



    # Declare an array to hold our variables.
    foods = [solver.NumVar(0.0, 2, item[0]) for item in data]

    print("Number of variables =", solver.NumVariables())

    # Create the constraints, one per nutrient.
    constraints = []
    for i, nutrient in enumerate(nutrientes):
        constraints.append(solver.Constraint(nutrient[1], nutrient[2]))
        for j, item in enumerate(data):
            #print(item)
            constraints[i].SetCoefficient(foods[j], item[i + 2])


    print("Number of constraints =", solver.NumConstraints())

    # Objective function: Minimize the sum of (price-normalized) foods.
    objective = solver.Objective()


    for i,food in enumerate(foods):
        objective.SetCoefficient(food, data[i][1])
    objective.SetMinimization()


    print(f"Solving with {solver.SolverVersion()}")
    status = solver.Solve()


    # Check that the problem has an optimal solution.
    if status != solver.OPTIMAL:
        print("The problem does not have an optimal solution!")
        if status == solver.FEASIBLE:
            print("A potentially suboptimal solution was found.")
        else:
            print("The solver could not solve the problem.")
            exit(1)

    # Display the amounts (in dollars) to purchase of each food.
    
    result = []
    for i, food in enumerate(foods):
        if food.solution_value() > 0.0:
            result.append({"item":food.name(), "value":food.solution_value() * 100})
    print(result)
    print("_________________")
    return result
