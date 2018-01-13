import math
import re

path_in = './competition-package/ptb.train.txt'
path_cache = './ngram_counts.txt'

# https://stackoverflow.com/questions/16402525/python-read-whitespace-separated-strings-from-file-similar-to-readline
def _read_by_tokens(fileobj):
    for line in fileobj:
        for token in line.split():
            yield token

def _string_ngrams(string):
    for start in range(len(string)):
        for end in range(start + 1, min(start + 7, len(string))):
            yield string[start:end]

def _starting_ngrams(string):
    for end in range(7):
        yield string[0:end]

def _parse_ngrams():
    ngrams = {}
    count = 0
    with open(path_in) as file:
        buffer = ''
        for token in _read_by_tokens(file):
            if token == '<unk>' or token == 'N':
                continue
            token = token.upper()
            token = re.sub('[^a-zA-Z]', '', token);
            buffer += token

            while(len(buffer)) >= 7:
                for ngram in _string_ngrams(token):
                    if ngram in ngrams:
                        ngrams[ngram] += 1
                    else:
                        ngrams[ngram] = 1
                buffer = buffer[1:]

        return ngrams
    return None

def _cache_ngrams(ngrams):
    with open(path_cache, 'w') as file:
        for ngram, count in ngrams.items():
            file.write(ngram + ' ' + str(count) + '\n')

def _cache_read_ngrams():
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
    ngrams = _cache_read_ngrams()
    if ngrams is not None:
        return ngrams
    else:
        ngrams = _parse_ngrams()
        _cache_ngrams(ngrams)
        return ngrams

ngram_count()