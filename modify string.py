
def modify_string(S):
    alphabets = [chr(i) for i in range(ord('a'), ord('z')+1)]
    frequency = {}
    for c in S:
        if c not in frequency:
            frequency[c] = 0
        frequency[c] += 1
    result = ""
    for c in S:
        index = alphabets.index(c) + frequency[c]
        result += alphabets[index % 26]
    return result
print(modify_string("ghee"))
