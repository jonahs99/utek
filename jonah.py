import clean

def letter(i):
    return chr(i + 65)

def letter_index(l):
    return ord(l) - 65

def shift_cypher(string, shift):
    return ''.join([ letter( (letter_index(l) + shift) % 26 ) for l in string ])
