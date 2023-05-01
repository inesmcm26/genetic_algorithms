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


if __name__ == '__main__':
    p1 = [0, 0, 0, 0]
    p2 = [1, 1, 1, 1]
    print(single_point_crossover(p1, p2))