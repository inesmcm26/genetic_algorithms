from random import randint, sample

def binary_mutation(individual):
    """
    Binary mutation for a GA individual

    Args:
        individual (Individual): A GA individual from charles.py

    Raises:
        Exception: When individual is not binary encoded.py

    Returns:
        Individual: Mutated Individual
    """
    mut_index = randint(0, len(individual) - 1)

    if individual[mut_index] == 0:
        individual[mut_index] = 1
    elif individual[mut_index] == 1:
        individual[mut_index] = 0
    else:
        raise Exception(
            f"Trying to do binary mutation on {individual}. But it's not binary.")
        
    return individual

def swap_mutation(individual):
    """
    Swap mutation for a GA individual

    Args: individual (Individual): A GA individual from charles.py

    Returns: Individual: Mutated Individual
    """
    mutation_idxs = sample(range(len(individual)), 2)

    individual[mutation_idxs[0]], individual[mutation_idxs[1]] = individual[mutation_idxs[1]], individual[mutation_idxs[0]]

    return individual


if __name__ == '__main__':
    # test = [0, 0, 0, 0]
    # test = binary_mutation(test)

    ind = [1, 2, 3, 4]
    ind = swap_mutation(ind)
    print(ind)
