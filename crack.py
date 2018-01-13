import Encryption
import cipher
import genetic
import random
import re

class GenChromo(genetic.Chromosome):
    def fitness(self):
        return cipher.score(self.string)
    def mutate(self):
        lstr = list(self.string)
        lstr[random.randint(0, len(self.string) - 1)] = chr(random.randint(65, 90))
        return GenChromo(''.join(lstr))

class SimpleChromo(genetic.Chromosome):
    def __init__(self, step, cipher):
        super()
        self.step = step
        self.cipher = cipher
    def fitness(self):
        decr = Encryption.simple_step(self.cipher, self.step)
        return cipher.score(decr)
    def mutate(self):
        offspring = SimpleChromo(random.randint(0, 25), self.cipher)
        return offspring
    def __repr__(self):
        return str(self.step)

class BlockChromo(genetic.Chromosome):
    def __init__(self, shifts, cipher):
        super()
        self.shifts = shifts
        self.cipher = cipher
    def fitness(self):
        decr = Encryption.block_step(self.cipher, self.shifts)
        return cipher.score(decr)
    def mutate(self):
        shifts = self.shifts.copy()
        shifts[random.randint(0, len(shifts) - 1)] = random.randint(0, 25)
        offspring = BlockChromo(shifts, self.cipher)
        return offspring
    def __repr__(self):
        return str(self.step)

class PermChromo(genetic.Chromosome):
    def __init__(self, string, cipher):
        super()
        self.string = string
        self.cipher = cipher
    def fitness(self):
        decr = Encryption.permutation(self.cipher, self.string)
        return cipher.score(decr)
    def mutate(self):
        lstr = list(self.string)
        for _ in range(random.randint(1, 6)):
            a = random.randint(0, len(self.string) - 1)
            b = random.randint(0, len(self.string) - 1)

            tmp = lstr[a]
            lstr[a] = lstr[b]
            lstr[b] = tmp
        offspring = PermChromo(''.join(lstr), self.cipher)
        return offspring

def crack_simple(cipher):
    trainer = genetic.Trainer(100, lambda: SimpleChromo(random.randint(0, 25), cipher))
    for i in range(20):
        w = trainer.iterate()
    return str(26 - w.step) + ' ' + Encryption.simple_step(cipher, w.step)

def crack_block(cipher, n_shifts = None):
    if n_shifts is not None:
        gen = lambda: BlockChromo([random.randint(0, 25) for _ in range(n_shifts)], cipher)
    else:
        gen = lambda: BlockChromo([random.randint(0, 25) for _ in range(random.randint(1, 5))], cipher)
    
    trainer = genetic.Trainer(100, gen)
    for i in range(200):
        w = trainer.iterate()
    return ''.join([ str(26 - s) + ' ' for s in w.shifts ]) + '| ' + Encryption.block_step(cipher, w.shifts)

def crack_permutation(cipher):
    trainer = genetic.Trainer(100, lambda: PermChromo('ABCDEFGHIJKLMNOPQRSTUVWXYZ', cipher))
    for i in range(100):
        w = trainer.iterate()
    return w.string + ' | ' + Encryption.permutation(cipher, w.string)