"""."""
import numpy as np
import string
import random


class Specimen:
    """."""

    def __init__(self, length):
        """."""
        self.genes = []
        self.fitness = 0

        self.get_random_genes(length)

    def get_random_gene(self):
        """."""
        return random.choice(string.ascii_letters + ' ')

    def get_random_genes(self, length):
        """."""
        for i in range(length):
            self.genes.append(self.get_random_gene())

    def get_phrase(self):
        """."""
        return ''.join(self.genes)

    def get_fitness(self, target):
        """Return the number of characters that are equal to the target."""
        score = 0
        for i, gene in enumerate(self.genes):
            if gene == target[i]:
                score += 1
        self.fitness = score / len(target)

    def crossover(self, partner):
        """."""
        child = self.__class__(len(self.genes))
        middle = np.random.randint(0, len(self.genes))

        for i in range(len(self.genes)):
            if i > middle:
                child.genes[i] = self.genes[i]
            else:
                child.genes[i] = partner.genes[i]

        return child

    def mutate(self, mutation_rate):
        """."""
        for i in range(len(self.genes)):
            if random.uniform(0, 1) < mutation_rate:
                self.genes[i] = self.get_random_gene()
