# Knapsack problem

from charles.charles import Individual, Population
from charles.search import hill_climb, sim_annealing
from charles.selection import fitness_proportionate_selection, tournament_selection
from charles.mutation import binary_mutation
from charles.crossover import single_point_crossover
from copy import deepcopy
from data.ks_data import values, weights, capacity

from random import random


class KSIndividual(Individual):
    """
    
    """
    def __init__(self, representation = None, size = None, valid_set = None, replacement = True):
        super().__init__(representation, size, valid_set, replacement)

    def get_neighbours(self):
        """
        Bit flipping
        """

        n = [deepcopy(self.representation) for _ in range(len(self.representation))] # initialize binary representation of the neighbours
        
        for index, neighbour in enumerate(n):
            if neighbour[index] == 1:
                neighbour[index] = 0
            elif neighbour[index] == 0:
                neighbour[index] = 1

        n = [KSIndividual(i) for i in n]
        return n

    
    def get_fitness(self):
        """
        Return total value when weight doesn't exceed maxiumum
        Else, return a bad fitness value: the negative of how far it is from being admissable
        """
        fit = 0
        tot_weight = 0

        # for each item, add weight and fitness
        for bit in range(len(self.representation)):
            if self.representation[bit]:
                tot_weight += weights[bit]
                fit += values[bit]

        # when solution is not admissable
        if tot_weight > capacity:
            return  capacity - tot_weight
        
        return fit

pop = Population(size = 100,
                 optim = 'max',
                 type_of_individ = KSIndividual,
                 sol_size = len(values), # 50 bits
                 valid_set = [0, 1],
                 replacement = True
                 )

# hill_climb(pop)
# sim_annealing(pop)

pop.evolve(n_generations = 100,
           xo_prob = 0.9,
           mut_prob = 0.2,
           select = tournament_selection,
           crossover = single_point_crossover,
           mutate = binary_mutation,
           elitism = True)

