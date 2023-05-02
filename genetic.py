import random
import data
import openpyxl


#global variables
MUTAUTION_RATE=0.1
CROSSOVER_RATE=0.9
GENERATIONS=100
POP_SIZE=50
SETS=data.sets
UNIVERSE=data.universe

#repair an infeasible solution
def repairing(solution):
    global SETS,UNIVERSE
    universe=set(UNIVERSE)
    coverd=set()
    _=[coverd.add(elt) for item in SETS for elt in item if solution[SETS.index(item)]]
    uncoverd = universe - coverd
    if coverd==universe:
        return solution
    for index in range(len(SETS)):
        for item in SETS[index]:
            if item in uncoverd:
                uncoverd.remove(item)
                solution[index]=1
                break
    return solution

#population initialization
def initialize_pop():
    global SETS
    return [repairing([random.randint(0,1) for _ in range(len(SETS))]) for _ in range(POP_SIZE)]

#implementing the uniform crossover
def uniform_crossover(parent1,parent2):

    global SETS,UNIVERSE
    offspring=[]
    for gene in range(len(parent1)):
        prob=random.random()
        if prob>0.5:
            offspring.append(parent1[gene])
        else :
            offspring.append(parent2[gene])
    return repairing(offspring)

#implementig mutation
def mutation(solution):
    global MUTAUTION_RATE
    for index in range(len(solution)):
        prob = random.random()
        if prob < MUTAUTION_RATE:
            solution[index] = not solution[index]
    return repairing(solution)

#fitness function
def evaluate_fitness(solution):
    return sum(solution)


def mate(population):
    global GENERATIONS
    for _ in  range(GENERATIONS):
        offspring=[]
        population = sorted(population, key=lambda individual: evaluate_fitness(individual))
        offspring.extend(population[:int(0.2*POP_SIZE)])# elitsm
        for _ in range(POP_SIZE-int(0.2*POP_SIZE)):
            parent1=random.choice(population)
            parent2=random.choice(population)
            offspring.append(mutation(uniform_crossover(parent1,parent2)))
    return population[0]





#this part of code create a file to store the solution in order to be visualized later.
population=initialize_pop()
solution=mate(population)

#indeices of chosen subsets
indices=[index for index in range(len(SETS)) if solution[index]]

# create a new workbook
workbook = openpyxl.Workbook()

# select the active worksheet
worksheet = workbook.active
# create headers for the table
worksheet['A1'] = 'city'
worksheet['B1'] = 'lat'
worksheet['C1'] = 'lng'

# populate the table with data
for index in indices:
    worksheet.append([data.potential_sites[index][0],data.potential_sites[index][1],data.potential_sites[index][2]])
# save the workbook
workbook.save('solution.xlsx')
