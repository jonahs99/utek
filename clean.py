import math

path_in = './competition-package/ptb.train.txt'
path_cache = './ngram_counts.txt'

# https://stackoverflow.com/questions/16402525/python-read-whitespace-separated-strings-from-file-similar-to-readline
def read_by_tokens(fileobj):
    for line in fileobj:
        for token in line.split():
            yield token

def string_ngrams(string):
    for start in range(len(string)):
        for end in range(start + 1, min(start + 7, len(string))):
            yield string[start:end]

def parse_ngrams():
    ngrams = {}
    count = 0
    with open(path_in) as file:
        for token in read_by_tokens(file):
            if token == "<unk>" or token == "N":
                continue
            upper = token.upper()
            for ngram in string_ngrams(upper):
                if ngram in ngrams:
                    ngrams[ngram] += 1
                else:
                    ngrams[ngram] = 1
                    count += 1
                    if count % 1000000 == 0:
                        print('unique ngrams:', count)
        return ngrams
    return None

def cache_ngrams(ngrams):
    with open(path_cache, 'w') as file:
        for ngram, count in ngrams.items():
            file.write(ngram + ' ' + str(count) + '\n')

def cache_read_ngrams():
    ngrams = {}
    try:
        with open(path_cache, 'r') as file:
            for line in file:
                spl = line.split(' ')
                ngrams[spl[0]] = int(spl[1])
        return ngrams
    except FileNotFoundError:
        return None

def ngram_count():
    ngrams = cache_read_ngrams()
    if ngrams is not None:
        return ngrams
    ngrams = parse_ngrams()
    cache_ngrams(ngrams)
    return ngrams

ngram_count()