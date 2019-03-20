import numpy as np

POP_SIZE = 10
MAX_ITERATIONS = 1648
ELITE_RATE = .1
MUTATION_RATE = .25

ELITE_SIZE = int(POP_SIZE * ELITE_RATE)
MUTATION_CHANCE = 4

CHROM_MAX_LEN = 10

target = list(np.arange(10)) # create target
target += target # create target
# print(target)

# initial solution, fitness 
class Individual(object):
    def __init__(self):
        self.fitness = 0
        self.solution = np.random.randint(CHROM_MAX_LEN, size=(len(target), ))

def calculate_fitness(population):
    for i in range(POP_SIZE):
        fitness = 0
        for j in range(len(target)):
            if(population[i].solution[j] == target[j]):
                fitness += 1
        population[i].fitness = fitness

def sort_by_fitness(population):
    for i in range(len(population)):
        j = i -1
        temp = population[i]
        while(j > -1 and population[j].fitness > temp.fitness):
            population[j+1] = population[j]
            j -= 1
        population[j+1] = temp

def print_best_individual(population, generation=None):
    try:
        print('at gen[%d], best: %d' % (generation, population[len(population)-1]))
    except:
        print('best: %d' % (population[len(population)-1]))

def mate_population(population, verbose=0):
    def debugging_msg(verbose):
        if(verbose):
            print(i, '\t\t\t\t\t ', i+1)
            print(temp[i].solution, temp[i+1].solution)
    
    temp = population.copy()
    for i in range(ELITE_SIZE, POP_SIZE, 2):
        r = np.random.randint(0, len(target))
        solution_i = population[i].solution.copy()
        try:
            debugging_msg(verbose)
            temp[i].solution[r:] = population[i+1].solution[r:]
            temp[i+1].solution[r:] = solution_i[r:]
            debugging_msg(verbose)
        except:
            pass

# def set_fitness(individuals):
#     for i in range(len(individuals)):
#         individuals[i].fitness = 0

# def random_solutions(individuals):
#     for i in range(len(individuals)):
#         individuals[i].solutions = np.random.randint(len(CHROM_MAX_LEN))

# def init_population(individuals):
#     set_fitness(individuals)
#     random_solutions(individuals)

if __name__ == "__main__":
    pop_a = []
    for i in range(POP_SIZE):
        pop_a.append(Individual())

    # for i in range(len(pop_a)):
    #     print(pop_a[i].fitness)

    calculate_fitness(pop_a)
    
    # for i in range(len(pop_a)):
    #     print(pop_a[i].fitness)
    
    sort_by_fitness(pop_a)

    p = []
    for i in range(len(pop_a)):
        p.append(pop_a[i])
    print(p)

    mate_population(pop_a, verbose=0)
