import numpy as np

POP_SIZE = 10 # กำหนดว่าประชากรมีกี่ Individual
MAX_ITERATIONS = 4096 # กำหนดว่าจะให้ทำ GA กี่ Generation
ELITE_RATE = .1 # กำหนดว่าให้มี Elite กี่เปอร์เซ็นต์ของจำนวนประชากร
MUTATION_RATE = .25 # กำหนด Mutation rate

ELITE_SIZE = int(POP_SIZE * ELITE_RATE)
MUTATION_CHANCE = 4 # ใช้แทน Mutation rate ในบรรทัดที่ 74
# Random เลข 0-3 มา ถ้าได้เลข 0 (มีโอกาส 25% เท่ากับ ELITE_RATE) ให้ทำการ Mutate

CHROM_MAX_LEN = 10 # กำหนดว่าแต่ละ Individual จะมี chromosome ยาวเท่าไหร่

# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
target = list(np.arange(10)) # บรรทัดนี้สร้างโจทย์บ่อดาย 
target += target # บรรทัดนี้สร้างโจทย์บ่อดาย 

"""
โปรแกรมจะประกอบด้วย:

Individual() ใช้สร้าง 1 Individual ที่มี Chromosome = [] และ และ fitness = 0

calculate_fitness(population) รับ Parameter เป็น Array ของ Individual ตย. [individual1, individual2, ...]
    ทำการหาว่าแต่ละ Individaul มีค่า fitness เท่าไหร่และกำหนดค่า fitness ให้ Individual แต่ละตัว

sort_by_fitness(population) รับ Parameter เป็น Array ของ Individual ทำการเรียงลำดับ Individual ที่มีค่า fitness
    จากน้อยไปมาก

print_best_individual(population, generation=None) รับ Parameter เป็น Array ของ Individual ทำการ print Individual ตัวสุดท้าย
    (ตัวที่ fitness สูงสุด) สามารถใส่ generation เพื่อให้ฟังก์ชั่น print ว่าปัจจุบันเป็น gen ที่เท่าไหร่ได้

mate(population, verbose = 0) รับ Parameter เป็น Array ของ Individual ทำการ crossover โดยสุ่มตำแหน่ง crossing site ตั้งแต่ 0 ถึง
    ความยาวของ Chromosome Parameter verbose=1 เป็นการกำหนดให้ฟังก์ชัน print ผลในแต่ละขั้นตอนของ 
    mate ออกมา

mutate(population, verbose=0) รับ Parameter เป็น Array ของ Individual ทำการ mutate เฉพาะ Individual ที่เป็น elite 
    ด้วย mutation_rate = 1/MUTATION_CHANCE Parameter verbose=1 เป็นการกำหนดให้ฟังก์ชัน print 
    ผลในแต่ละขั้นตอนของ mutate ออกมา
"""

# initial solution (random), fitness
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
        print('at gen[%d], best: %a, fitness: %d' % (generation, population[len(population)-1].solution, population[len(population)-1].fitness))
    except:
        print('best: %d' % (population[len(population)-1]))

def mate(population, verbose=0):
    def debugging_msg(verbose):
        if(verbose):
            print(i, '\t\t\t\t\t ', i+1)
            print(temp[i].solution, temp[i+1].solution)

    if(verbose):
        print('mating')

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

    if(verbose):
        print()

def mutate(population, verbose=0):
    if(verbose):
        print('mutating')

    for i in range(ELITE_SIZE): # each elite
        if(not(np.random.randint(MUTATION_CHANCE + 1))):
            if(verbose):
                print('individual', i,  'being mutated')
                print('before', population[i].solution)
            
            mutate_idx = np.random.randint(len(population[0].solution))
            mutate_val = np.random.randint(10) # สุ่มให้ยีนที่ถูก mutate มีค่า [0-9]
            # เพราะในโจทย์กำหนดให้ยีนเป็น [0-9]
            population[i].solution[mutate_idx] = mutate_val

            if(verbose):
                print('mutate at index', mutate_idx, 'with value', mutate_val)
                print('after', population[i].solution)
        else:
            if(verbose):
                print('no mutation')
    
    if(verbose):
        print()

if __name__ == "__main__": # tests are done in main
    pop_a = []
    for i in range(POP_SIZE):
        pop_a.append(Individual())

    for i in range(MAX_ITERATIONS):
        calculate_fitness(pop_a)
        sort_by_fitness(pop_a)
        print_best_individual(pop_a, generation=i)

        if(pop_a[POP_SIZE - 1].fitness == len(target)):
            break

        mate(pop_a, verbose=0)
        mutate(pop_a, verbose=0)
    
    print_best_individual(pop_a, generation=i)
