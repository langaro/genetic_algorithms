from funcoes.crack_ga import *

goal = "banana"
firstGeneration = generateFirstPopulation(500, goal)
print(Evolution(firstGeneration, goal, 1));