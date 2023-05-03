from random import randint

def single_point_crossover(parent1, parent2):
    """
    Implementation of single point crossover.

    Args:
        p1 (Individual): First parent for crossover.
        p2 (Individual): Second parent for crossover.

    Returns:
        Individuals: Two offspring, resulting from the crossover.
        
    """
    xo_point = randint(1, len(parent1) - 1)

    offspring1 = parent1[:xo_point] + parent2[xo_point:]
    offspring2 = parent2[:xo_point] + parent1[xo_point:]

    return offspring1, offspring2

def cycle_crossover(parent1, parent2):

    offspring1 = [None] * len(parent1)
    offspring2 = [None] * len(parent1)

    while None in offspring1:
        idx = offspring1.index(None)

        val1 = parent1[idx]
        val2 = parent2[idx]

        while val1 != val2:
            # set values on the offspring
            offspring1[idx] = parent1[idx]
            offspring2[idx] = parent2[idx]

            # update val2 to the value on the new index
            val2 = p2[idx]
            
            # get new position on parent 1 that correspond to the value on parent 2
            idx = parent1.index(val2)


        for element in offspring1:
            if element is None:
                idx = offspring1.index(element)
                if offspring1[idx] is None:
                    offspring1[idx] = parent2[idx]
                    offspring2[idx] = parent1[idx]

    return offspring1, offspring2



if __name__ == '__main__':
    p1 = [0, 0, 0, 0]
    p2 = [1, 1, 1, 1]
    print(single_point_crossover(p1, p2))