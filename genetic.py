import random

'''def mutate(self):
    a = random.randint(0, len(self.string) - 1)
    b = random.randint(0, len(self.string) - 1)

    lstr = list(self.string)
    lstr[a] = self.string[b]
    lstr[b] = self.string[a]

    offspring = Chromosome(''.join(lstr))
    return offspring
'''
class Chromosome:
    def __init__(self,):
        pass
    def fitness(self):
        pass
    def mutate(self):
        pass

class Trainer:
    def __init__(self, pool_size, construct):
        self.pool_size = pool_size
        self.pool = [ construct() for i in range(self.pool_size) ]

        self.cuttoff_ratio = 0.5

    def iterate(self):
        scored = sorted([ (chromo, chromo.fitness()) for chromo in self.pool ], key = lambda p: p[1])
        winners = [ p[0] for p in scored[int(self.cuttoff_ratio * self.pool_size):]]

        offspring = []
        while len(winners) + len(offspring) < self.pool_size:
            parent = random.choice(winners)
            offspring.append(parent.mutate())
        
        self.pool = winners + offspring

        return scored[-1][0]