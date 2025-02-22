from functools import lru_cache

def sequence_iter(k):
    if k == 1:
        return 1, 1
    a, b = 1, 1
    for _ in range(2, k + 1):
        a, b = 2 * b - 1 + a, 2 * a + b
    return a, b

@lru_cache(None)
def sequence_rec(k, a=1, b=1):
    if k == 1:
        return a, b
    return sequence_rec(k - 1, 2 * b - 1 + a, 2 * a + b)

print(sequence_iter(5))
print(sequence_rec(5))