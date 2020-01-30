"""."""
from classes.population import Population

POPULATION_SIZE = 200
MUTATION_RATE = 0.01

population = Population('alvaro degas', MUTATION_RATE)  # string alvo
population.get_population(POPULATION_SIZE)  # Crie uma população de tamanho POPULATION_SIZE

while not population.finished:
    population.get_mating_pool()  # Crie uma pool de acasalamento
    population.get_new_generation()  # A partir dessa pool de acasalamento, crie uma nova geração, substituindo a anterior
    population.evaluate()  # Avalie a nova população em busca da solução

print(f"Palavra encontrada na geração: {population.generations}\nFiness média: {population.get_average_fitness()}")
