import re
import cipher
import Encryption
import crack

# 1a
with open('./output/1a.out', 'w') as w:
    with open('./input/1a.in') as file:
        for line in file:
            tokens = line.split('|')
            tokens[0] = re.sub(r'\s', '', tokens[0])
            tokens[2] = re.sub(r'\s', '', tokens[2])
            if tokens[0] == "ENCRYPT":
                w.write(Encryption.simple_step(tokens[2], int(tokens[1])) + '\n')
            elif tokens[0] == "DECRYPT":
                w.write(Encryption.simple_step(tokens[2], 26 - int(tokens[1])) + '\n')

# 1b
with open('./output/1b.out', 'w') as w:
    with open('./input/1b.in') as file:
        for line in file:
            tokens = line.split('|')
            tokens[0] = re.sub(r'\s', '', tokens[0])
            tokens[2] = re.sub(r'\s', '', tokens[2])
            shifts = [ int(s) for s in tokens[1].split() ]
            if tokens[0] == "ENCRYPT":
                w.write(Encryption.block_step(tokens[2], shifts) + '\n')
            elif tokens[0] == "DECRYPT":
                w.write(Encryption.block_step(tokens[2], [ 26 - shift for shift in shifts ]) + '\n')

#1c
with open('./output/1c.out', 'w') as w:
    with open('./input/1c.in') as file:
        for line in file:
            tokens = line.split('|')
            tokens[0] = re.sub(r'\s', '', tokens[0])
            tokens[1] = re.sub(r'\s', '', tokens[1])
            tokens[2] = re.sub(r'\s', '', tokens[2])
            if tokens[0] == "ENCRYPT":
                w.write(Encryption.permutation(tokens[2], tokens[1]) + '\n')
            elif tokens[0] == "DECRYPT":
                w.write(Encryption.permutation(tokens[2], tokens[1]) + '\n')

#2b
with open('./output/2b.out', 'w') as w:
    with open('./input/2b.in') as file:
        for line in file:
            tokens = line.split('|')
            tokens[0] = re.sub(r'\s', '', tokens[0])
            tokens[1] = re.sub(r'\s', '', tokens[1])
            score1 = cipher.score(tokens[0])
            score2 = cipher.score(tokens[1])
            w.write( ('1' if score1 > score2 else '2') + '\n' )

#3a
with open('./output/3a.out', 'w') as w:
    with open('./input/3a.in') as file:
        for line in file:
            cipher = re.sub(r'\s', '', line)
            w.write(crack.crack_simple(cipher) + '\n')

#3b
with open('./output/3b.out', 'w') as w:
    with open('./input/3b.in') as file:
        for line in file:
            tokens = line.split('|')
            n_shift = int(tokens[0])
            cipher = re.sub(r'\s', '', tokens[1])
            w.write(crack.crack_block(cipher, n_shift) + '\n')

#3c
with open('./output/3c.out', 'w') as w:
    with open('./input/3c.in') as file:
        for line in file:
            cipher = re.sub(r'\s', '', line)
            w.write(crack.crack_block(cipher) + '\n')

#3d
with open('./output/3d.out', 'w') as w:
    with open('./input/3d.in') as file:
        for line in file:
            cipher = re.sub(r'\s', '', line)
            w.write(crack.crack_permutation(cipher) + '\n')