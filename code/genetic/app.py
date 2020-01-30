"""."""
from classes.population import Population

POPULATION_SIZE = 500
MUTATION_RATE = 0.01

population = Population('banana doce', MUTATION_RATE)

while not population.finished:
    population.get_population(POPULATION_SIZE)
    population.get_population_fitness()
    population.get_mating_pool()
    population.get_new_generation()
    population.evaluate()

print(f"Palavra encontrada na geração: {population.generations}\nFiness média: {population.get_average_fitness()}")
