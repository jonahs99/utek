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

trainer = genetic.Trainer(100, lambda: GenChromo("AAAAAAAAAAAAAAAAAAAA"))

for i in range(100000):
    w = trainer.iterate()
    if i % 10000:
        print(w)