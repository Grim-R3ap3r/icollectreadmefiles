import test_functions
from GA import Genetic_Algorithm

generations = 2500
objective = test_functions.ackleyFunction

solution = Genetic_Algorithm(
    objective=objective,
    numDimensions=2,
    populationSize=500,
    offspringsNo=1500,
    crossoverRatio=0.16,
)

solution.initializePopulation()

for _ in range(generations):
    solution.generationStep()

print(
    f"Best solution Fitness: {objective.function(solution.findBestSol())}"
)
