# Travel Sales Person problem

from charles.charles import Individual, Population
from charles.search import hill_climb, sim_annealing
from charles.selection import fitness_proportionate_selection, tournament_selection
from charles.mutation import swap_mutation
from charles.crossover import cycle_crossover
from data.tsp_data import distance_matrix

from copy import deepcopy

class TSPIndividual(Individual):

    def __init__(self, representation = None, size = None, valid_set = None, replacement = True):
        super().__init__(representation, size, valid_set, replacement)

    def get_neighbours(self):
        """
            Return the neighbours: switch consecutive indexes
            
            Ex.:
            original -> A B C D
            neighbour -> A D C B
        """
        neighs = [deepcopy(self.representation) for _ in range(len(self.representation) - 1)] 

        for i, neigh in enumerate(neighs):
            neigh[i], neigh[i + 1] = neigh[i + 1], neigh[i]

        neighs = [TSPIndividual(i) for i in neighs] # create one individual for each neighbour

        return neighs
    
    def get_fitness(self):
        """ 
            Returns the total distance of the path
        """
        dist = 0
        rep = self.representation

        for i in range(-1, len(rep) - 1):
            dist += distance_matrix[rep[i]][rep[i + 1]] # add distance between two cities

        return int(dist)

pop = Population(
    size = 100,
    sol_size = len(distance_matrix[0]),
    valid_set = [i for i in range(len(distance_matrix[0]))], # representation of each city is an integer
    type_of_individ = TSPIndividual,
    replacement = False,
    optim = 'min'
)

# hill_climb(pop)
# sim_annealing(pop)

pop.evolve(n_generations = 100,
           xo_prob = 0.9,
           mut_prob = 0.15,
           mutate = swap_mutation,
           crossover = cycle_crossover,
           select = tournament_selection,
           elitism = True)