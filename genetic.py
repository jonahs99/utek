import random

class Chromosome:
    def __init__(self, string):
        self.string = string
    def fitness(self):
        return 0
    def mutate(self):
        offspring = Chromosome(self.string)
        a = random.randint(0, len(self.string))
        b = random.randint(0, len(self.string))
        offspring.string[a] = self.string[b]
        offspring.string[b] = self.string[a]
        return offspring

class Trainer:
    def __init__(self, pool_size, construct):
        self.pool_size = pool_size
        self.pool = [ construct() for i in range(self.pool_size) ]

        self.cuttoff_ratio = 0.5
        self.mutation_rate = 0.02

    def iterate(self):
        scored = sorted([ (chromo, chromo.fitness()) for chromo in self.pool ], key = lambda p: p[1])
        winners = scored[int(self.cuttoff_ratio * self.pool_size):]

        offspring = []
        while len(winners) + len(offspring) < self.pool_size:
            parent = random.choice(winners)[0]
            offspring.append(parent.mutate())
        
        self.pool = winners + offspring

trainer = Trainer(10, lambda: Chromosome("12345678"))
trainer.iterate()
print(trainer.pool)