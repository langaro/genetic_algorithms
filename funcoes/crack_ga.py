#https://blog.sicara.com/getting-started-genetic-algorithms-python-tutorial-81ffa1dd72f9

import random
import operator
import sys

def VerifyBetter(population, populationType, goal, nGen):
    if goal in population:
        print('Fittest found in mutated generation No ', nGen)
        sys.exit()
    else:
        nGen += 1
        Evolution(population, goal, nGen)

def Evolution(generation, goal, nGen):
    print('Generation No', nGen)

    fitnessSorted = computePerfPopulation(generation, goal);
    print('     Fitness Sorted', fitnessSorted)

    selected = selectFromPopulation(fitnessSorted, 30, 20)
    print('     Fitness Selected', selected)

    children = createChildren(selected, 2);
    print('     Children ', children)

    mutated = mutatePopulation(children, 0);
    print('     Mutated ', mutated)
    print('')

    VerifyBetter(mutated, 'mutated', goal, nGen)

def fitness(password, test_word):
    if (len(test_word) != len(password)):
        print("taille incompatible")
        return
    else:
        score = 0
        i = 0
        while (i < len(password)):
            if (password[i] == test_word[i]):
                score += 1
            i += 1
        return score * 100 / len(password)

def generateAWord(length):
    i = 0
    result = ""
    while i < length:
        letter = chr(97 + int(26 * random.random()))
        result += letter
        i +=1
    return result

def generateFirstPopulation(sizePopulation, password):
    population = []
    i = 0
    while i < sizePopulation:
        population.append(generateAWord(len(password)))
        i+=1
    return population

def computePerfPopulation(population, password):
    populationPerf = {}
    for individual in population:
        populationPerf[individual] = fitness(password, individual)
    return sorted(populationPerf.items(), key = operator.itemgetter(1), reverse=True)

def selectFromPopulation(populationSorted, best_sample, lucky_few):
    nextGeneration = []
    for i in range(best_sample):
        nextGeneration.append(populationSorted[i][0])
    for i in range(lucky_few):
        nextGeneration.append(random.choice(populationSorted)[0])
    random.shuffle(nextGeneration)
    return nextGeneration

def createChild(individual1, individual2):
    child = ""
    for i in range(len(individual1)):
        #percorre cada letra e randonicamente (linha de baixo) pega uma letra de cada palavra
        if (int(100 * random.random()) < 50):
            child += individual1[i]
        else:
            child += individual2[i]

    #print(' pai: ', individual1, ' mae: ', individual2, ' filho', child);
    return child

def createChildren(breeders, number_of_child):
    nextPopulation = []
    #primeiro e ultimo, segundo e penultimo, terceiro e antepenultimo...
    for i in range(int(len(breeders)/2)):
        for j in range(number_of_child):
            nextPopulation.append(createChild(breeders[i], breeders[len(breeders) -1 -i]))
    return nextPopulation

def mutateWord(word):
    index_modification = int(random.random() * len(word))
    if (index_modification == 0):
        word = chr(97 + int(26 * random.random())) + word[1:]
    else:
        word = word[:index_modification] + chr(97 + int(26 * random.random())) + word[index_modification + 1:]
    return word

def mutatePopulation(population, chance_of_mutation):
    for i in range(len(population)):
        if random.random() * 100 < chance_of_mutation:
            population[i] = mutateWord(population[i])
    return population