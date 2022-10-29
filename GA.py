import itertools
import random

from test_functions import ObjectiveFunction


class Genetic_Algorithm:

    def __init__(
        self,
        objective: ObjectiveFunction,
        numDimensions: int,
        populationSize: int,
        offspringsNo: int,
        crossoverRatio: float,
        mutationStddev: float = 0.5,
        use_uniform_mutation: bool = False,
       
    ) -> None:
        self.objective = objective.function
        self.x_min = objective.lower_bound
        self.x_max = objective.upper_bound
        self.numDimensions = numDimensions
        self.populationSize = populationSize
        self.offspringsNo = offspringsNo
        self.crossoverRatio = crossoverRatio
        self.mutationStddev = mutationStddev
        self.use_uniform_mutation = use_uniform_mutation
        

        self.population: list[list[float]] = []
        self.mating_pool: list[list[float]] = []
        self.next_generation: list[list[float]] = []

    def initializePopulation(self) -> None:
        for _ in range(self.populationSize):
            self.population.append(
                [random.uniform(self.x_min, self.x_max) for _ in range(self.numDimensions)]
            )

    def __generateMatingPool(self) -> None:
        for i in range(self.populationSize):
            randomK=random.choices(self.population,k=5);
            self.mating_pool.append(min(randomK))


    # def __simpleArithmeticCrossover(self) -> None:
    #     for _ in range(self.offspringsNo // 2):
    #         parents = random.choices(self.mating_pool, k=2)
    #         crossover_index = random.randint(0, self.numDimensions - 1)
    #         t1 = [allele * self.crossoverRatio for allele in parents[0][crossover_index:]] \
    #                 + [allele * (1 - self.crossoverRatio) for allele in parents[1][crossover_index:]]

    #         t2 = [allele * (1 - self.crossoverRatio) for allele in parents[0][crossover_index:]] \
    #                  + [allele * self.crossoverRatio for allele in parents[1][crossover_index:]]

    #         child1 = parents[0][:crossover_index] + t1
    #         child2 = parents[1][:crossover_index] + t2

    #         self.next_generation.extend([child1, child2])

    def __singleArithmeticCrossover(self) -> None:

        for _ in range(self.offspringsNo // 2):
            parents = random.choices(self.mating_pool, k=2)

            crossover_index = random.randint(0, self.numDimensions - 1)
            child1 = parents[0].copy()
            child2 = parents[1].copy()

            child1[crossover_index] = (
                parents[1][crossover_index] * (1 - self.crossoverRatio) + parents[0][crossover_index] * self.crossoverRatio
            )
            child2[crossover_index] = (
                parents[0][crossover_index] * (1 - self.crossoverRatio) + parents[1][crossover_index] * self.crossoverRatio
            )

            self.next_generation.extend([child1, child2])

    def __uniformMutation(self) -> None:

        for index in range(len(self.next_generation)):
            mutation_index = random.randint(0, self.numDimensions - 1)
            self.next_generation[index][mutation_index] = random.uniform(self.x_min, self.x_max)

    def __replacement(self) -> None:
        all_individuals = self.population + self.next_generation
        all_individuals.sort(key=self.objective)
        self.population = all_individuals[: self.populationSize]
        self.next_generation = []

    def generationStep(self) -> None:
        self.__generateMatingPool()
        self.__singleArithmeticCrossover()
        self.__uniformMutation()
        self.__replacement()

    def findBestSol(self) -> list[float]:
        return min(self.population, key=self.objective)


