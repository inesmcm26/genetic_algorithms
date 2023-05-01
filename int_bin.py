# Binary integers problem definition

from charles.charles import Individual, Population
from charles.search import hill_climb, sim_annealing
from copy import deepcopy


class IntBinIndividual(Individual):
    def __init__(self, representation, size = None, valid_set = None):
        super().__init__(representation, size, valid_set)

    def get_neighbours(self):
        """
        Get neighbours: the number below and the number above in binary
        """

        n = [deepcopy(self.representation) for _ in range(len(self.representation))] # initialize binary representation of the neighbors
        
        # bit flipping -> neighbours of binary number representation
        for count, i in enumerate(n):
            # i is a list of neighbors with a bit flipped
            if i[count] == 1:
                i[count] = 0
            elif i[count] == 0:
                i[count] = 1

        n = [IntBinIndividual(i) for i in n] # all the neighbors
        return n

    
    def get_fitness(self):
        """
        Get number of ones in the binary representation
        """
        # return "{0:04b}".format(self.representation[0]).count("1")
        return self.representation.count(1)


pop = Population(size = 1,
                 optim = 'max',
                 type_of_individ = IntBinIndividual,
                 sol_size = 4, # 4 bits
                 valid_set = [0, 1]
                 )

# hill_climb(pop)
sim_annealing(pop)