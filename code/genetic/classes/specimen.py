"""."""
import numpy as np
import string
import random


class Specimen:
    """."""

    def __init__(self):
        """."""
        self.genes = []
        self.fitness = 0

    def get_random_gene(self):
        """Pega um gene aleatoriamente."""
        return random.choice(string.ascii_letters + ' ')

    def get_random_genes(self, length):
        """Inicializa os genes de um individuo aleatoriamente."""
        for i in range(length):
            self.genes.append(self.get_random_gene())

    def get_phrase(self):
        """Pega a frase para mostrar."""
        return ''.join(self.genes)

    def get_fitness(self, target):
        """Calcula o fitness do individuo."""
        score = 0
        for i, gene in enumerate(self.genes):
            if gene == target[i]:
                score += 1
        self.fitness = score / len(target)

    def crossover(self, partner):
        """Realiza o cruzametno do individuo A com o partner e retorna o novo individuo."""
        child = self.__class__()  # cria um novo individuo
        middle = np.random.randint(0, len(self.genes))  # um valor de 0 a len de genes para ser o meio onde o cruzamento dos genes irá ocorrer

        for i in range(len(self.genes)):
            if i > middle:
                child.genes.append(self.genes[i])  # pega os genes do individuo A
            else:
                child.genes.append(partner.genes[i])  # pega os genes dos individuo B

        return child  # retorna o novo individuo

    def mutate(self, mutation_rate):
        """Realiza a mutação do individuo."""
        for i in range(len(self.genes)):
            if random.uniform(0, 1) < mutation_rate:  # probabilidade de mutação
                self.genes[i] = self.get_random_gene()
