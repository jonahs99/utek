

import clean
from math import log
import re

import random

ngrams = clean.ngram_count()
# return a dictionary 
# the keys are the ngrams
# the values are counts

N = 7

def Pr(s):
    Lambda = [1e-6, 1e-5, 1e-4, 1e-3, 1e-2, 1e-1, 0.888889]
    prob = 0.0
    length = len(s)
    
    for j in range(1, min(length, N)):
        a = s[: j]
        b = s[: j+1]
        
        if a in ngrams:
            a_cnt = ngrams[a]
        else:
            a_cnt = 0
        
        if b in ngrams:
            b_cnt = ngrams[b]
        else:
            b_cnt = 0
            
        Lambda_idx = j + N - length
        #print('using Lambda', Lambda[Lambda_idx])
        
        if (a_cnt != 0):
            prob += Lambda[Lambda_idx] * b_cnt / a_cnt
            #print(b, a, b_cnt, a_cnt, 
             #     Lambda[Lambda_idx] * b_cnt / a_cnt, 
              #    prob)
        
    return prob
    
def score(sentence):
    sentence = re.sub('[^a-zA-Z]', '', sentence)
    
    length = len(sentence)
    _score  = 0.0
    
    neg_inf = - random.randint(100, 200)
    
    for i in range( max(length - N + 1, 0) ):
        #print(sentence[i : i + N])
        k = Pr( sentence[i : i + N] )
        if (k != 0.0):
            _score += log(k)
            #print(sentence[i : i + N], ':', log(k), '\n')
        else:
            _score += neg_inf
    
    return _score
    