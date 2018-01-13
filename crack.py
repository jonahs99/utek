import Encryption
import cipher
import genetic
import random
import re

#raw = '''Seeing, now, that there were no curtains to the window, 
#and that the street being very narrow, the house opposite 
#commanded a plain view into the room, and observing'''

raw = "once upon a midnight dreary"

IN = re.sub('[^A-Z]', '', raw.upper())
print(IN)
#CIPHER = Encryption.permutation(IN, 'ZYXWVUTSRQPONMLKJIHGFEDCBA')
CIPHER = Encryption.block_step(IN, [1, 10, 2])

class GenChromo(genetic.Chromosome):
    def fitness(self):
        return cipher.score(self.string)
    def mutate(self):
        lstr = list(self.string)
        lstr[random.randint(0, len(self.string) - 1)] = chr(random.randint(65, 90))
        return GenChromo(''.join(lstr))

class PermChromo(genetic.Chromosome):
    def __init__(self, string):
        super()
        self.string = string
    def fitness(self):
        decr = Encryption.permutation(CIPHER, self.string)
        return cipher.score(decr)
    def mutate(self):
        lstr = list(self.string)
        for _ in range(random.randint(1, 6)):
            a = random.randint(0, len(self.string) - 1)
            b = random.randint(0, len(self.string) - 1)

            tmp = lstr[a]
            lstr[a] = lstr[b]
            lstr[b] = tmp
        offspring = PermChromo(''.join(lstr))
        return offspring

class SimpleChromo(genetic.Chromosome):
    def __init__(self, step):
        super()
        self.step = step
    def fitness(self):
        decr = Encryption.simple_step(CIPHER, self.step)
        return cipher.score(decr)
    def mutate(self):
        offspring = SimpleChromo(random.randint(0, 25))
        return offspring
    def __repr__(self):
        return str(self.step)

class BlockChromo(genetic.Chromosome):
    def __init__(self, shifts):
        super()
        self.shifts = shifts
    def fitness(self):
        decr = Encryption.block_step(CIPHER, self.shifts)
        return cipher.score(decr)
    def mutate(self):
        shifts = self.shifts.copy()
        shifts[random.randint(0, len(shifts) - 1)] = random.randint(0, 25)
        offspring = BlockChromo(shifts)
        return offspring
    def __repr__(self):
        return str(self.step)

trainer = genetic.Trainer(1000, lambda: BlockChromo([ random.randint(0, 25) for _ in range(3) ]))
#trainer = genetic.Trainer(1000, lambda: PermChromo('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))

print(IN, cipher.score(IN))

for i in range(100):
    w = trainer.iterate()
    if i % 10 == 0:
        decr = Encryption.block_step(CIPHER, w.shifts)
        print(decr, w.shifts, cipher.score(decr))

'''for i in range(1000):
    w = trainer.iterate()
    if i % 5 == 0:
        decr = Encryption.permutation(CIPHER, w.string)
        print(decr, w.string, cipher.score(decr))'''