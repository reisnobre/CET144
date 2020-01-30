"""."""
from classes.specimen import Specimen
import math
import random
from decimal import Decimal


class Population:
    """."""

    def __init__(self, target, mutation_rate):
        """."""
        self.target = target
        self.mutation_rate = mutation_rate
        self.specimens = []
        self.mating_pool = []
        self.population_fitness = []
        self.generations = 0
        self.best = None
        self.perfect_score = 1
        self.finished = False

    def get_population(self, population_size):
        """Cria uma nova população."""
        for i in range(population_size):
            specimen = Specimen()
            specimen.get_random_genes(len(self.target))
            specimen.get_fitness(self.target)  # calcule a fitness do individuo

            self.specimens.append(specimen)  # adicione o individuo a população

    # def get_population_fitness(self):
    #     """."""
    #     for specimen in self.specimens:
    #         specimen.get_fitness(self.target)

    def get_max_fitness(self):
        """Pega o maior fitness de toda a população."""
        fitness = 0
        for specimen in self.specimens:
            if specimen.fitness > fitness:
                fitness = specimen.fitness
        return fitness

    def get_mating_pool(self):
        """Cria uma pool de acasalamento."""
        mating_pool = []
        # max_fitness = self.get_max_fitness()

        for specimen in self.specimens:
            fitness = math.floor(specimen.fitness * 100)  # cada individuo tem um número de entradas na mating_pool proporcional a sua fitness * 100
            for i in range(fitness):
                mating_pool.append(specimen)
        self.mating_pool = mating_pool

    def get_new_generation(self):
        """Cria uma nova geração de indivíduos substituindo os anteriores."""
        for i in range(len(self.specimens)):
            parent_a = random.choice(self.mating_pool)  # Escolha o antecessor A aleatoriamente
            parent_b = random.choice(self.mating_pool)  # Escolha o antecessor B aleatoriamente

            child = parent_a.crossover(parent_b)  # realize o cruzamento do A com B
            child.mutate(self.mutation_rate)  # realize a mutação no filho
            child.get_fitness(self.target)  # pegue a fitness do filho
            self.specimens[i] = child  # substitua o individuo na posição i da população
        self.generations += 1

    def evaluate(self):
        """Avalia a população."""
        worldrecord = 0
        index = 0
        # Procure o individuo com melhor fitness
        for i, specimen in enumerate(self.specimens):
            if specimen.fitness > worldrecord:
                worldrecord = specimen.fitness
                index = i

        # Pegue a melhor frase para aquela geração
        self.best = self.specimens[index].get_phrase()
        # Se eu cheguei a minha condição de parada, conclua a minha população
        if worldrecord == self.perfect_score:
            self.finished = True

    def get_average_fitness(self):
        """."""
        average = Decimal(sum(specimen.fitness for specimen in self.specimens) / len(self.specimens))
        return round(average, 2)
