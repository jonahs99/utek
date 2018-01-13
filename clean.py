path = '../competition-package/ptb.train.txt'

# https://stackoverflow.com/questions/16402525/python-read-whitespace-separated-strings-from-file-similar-to-readline
def read_by_tokens(fileobj):
    for line in fileobj:
        for token in line.split():
            yield token

def ngram_count():
    ngrams = {}
    with open(path) as file:
        for token in read_by_tokens(file):
            if token == "<unk>" or token == "N":
                continue
            ngrams.append(token.upper())
            if len(ngrams) > 100:
                break
        return ngrams
    return None

print(clean())