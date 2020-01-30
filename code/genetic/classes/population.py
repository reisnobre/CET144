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
        """."""
        for i in range(population_size):
            specimen = Specimen(len(self.target))
            specimen.get_fitness(self.target)

            self.specimens.append(specimen)

    def get_population_fitness(self):
        """."""
        for specimen in self.specimens:
            specimen.get_fitness(self.target)

    def get_max_fitness(self):
        """."""
        fitness = 0
        for specimen in self.specimens:
            if specimen.fitness > fitness:
                fitness = specimen.fitness
        return fitness

    def get_mating_pool(self):
        """."""
        mating_pool = []
        # max_fitness = self.get_max_fitness()

        for specimen in self.specimens:
            fitness = math.floor(specimen.fitness * 100)
            for i in range(fitness):
                mating_pool.append(specimen)
        self.mating_pool = mating_pool

    def get_new_generation(self):
        """."""
        for i in range(len(self.specimens)):
            parent_a = random.choice(self.mating_pool)
            parent_b = random.choice(self.mating_pool)

            child = parent_a.crossover(parent_b)
            child.mutate(self.mutation_rate)
            child.get_fitness(self.target)
            self.specimens[i] = child
        self.generations += 1

    def evaluate(self):
        """."""
        worldrecord = 0
        index = 0
        for i, specimen in enumerate(self.specimens):
            if specimen.fitness > worldrecord:
                worldrecord = specimen.fitness
                index = i

        self.best = self.specimens[index].get_phrase()
        if worldrecord == self.perfect_score:
            self.finished = True

    def get_average_fitness(self):
        """."""
        average = Decimal(sum(specimen.fitness for specimen in self.specimens) / len(self.specimens))
        return round(average, 2)
