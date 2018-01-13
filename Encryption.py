

def letter(i):
    return chr(i + ord('A'))

def letter_index(l):
    return ord(l) - ord('A')

def letter_shift(i, shift):
    return letter( (letter_index(i) + shift) % 26 )

def non_alphabetic(i):
    if (ord('A') <= ord(i) <= ord('Z')):
        return False
    return True

def simple_step(string, shift):
    return ''.join([(l if non_alphabetic(l) else letter_shift(l, shift))
                    for l in string])

def block_step(string, shifts):
    keys_idx = -1
    keys_cnt = len(shifts)
    ans = ''
    
    for i in string:
        if non_alphabetic(i):
            ans += i
        else:
            (keys_idx) = (keys_idx + 1) % keys_cnt
            ans += letter_shift(i, shifts[keys_idx])
        
    return ans

