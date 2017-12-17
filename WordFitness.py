from funcoes.crack_ga import *

goal = "banana"
firstGeneration = generateFirstPopulation(500, goal)
print(Evolution(firstGeneration, goal, 1));



    #for x in range(0,500):
    #    print("We're on time %d" % (x))