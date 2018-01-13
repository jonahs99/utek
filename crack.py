import Encryption
import cipher
import genetic
import random

class GenChromo(genetic.Chromosome):
    def fitness(self):
        return cipher.score(self.string)
    def mutate(self):
        lstr = list(self.string)
        lstr[random.randint(0, len(self.string) - 1)] = chr(random.randint(65, 90))
        return GenChromo(''.join(lstr))

class PermChromo(genetic.Chromosome):
    def fitness(self):
        decr = Encryption.permutation("ITSSGVGKSR", self.string)
        return cipher.score(self.string)
    def mutate(self):
        a = random.randint(0, len(self.string) - 1)
        b = random.randint(0, len(self.string) - 1)

        lstr = list(self.string)
        lstr[a] = self.string[b]
        lstr[b] = self.string[a]

        offspring = PermChromo(''.join(lstr))
        return offspring

trainer = genetic.Trainer(100, lambda: PermChromo("ABCDEFGHIJKLMNOPQRSTUVWXYZ"))

for i in range(10000):
    w = trainer.iterate()
    if i % 100 == 0:
        print(w)
        #decr = Encryption.permutation("ITSSGVGKSR", w.string)
        #print(decr)