# Итеративный вариант
def sequence_iter(k):
    a, b = 1, 1
    for _ in range(2, k + 1):
        a, b = 2 * b - 1 + a, 2 * a + b
    return a, b

# Рекурсивный вариант
def sequence_rec(k, a=1, b=1):
    if k == 1:
        return a, b
    a_new = 2 * b - 1 + a
    b_new = 2 * a + b
    return sequence_rec(k - 1, a_new, b_new)

# Тест
print(sequence_iter(5))
print(sequence_rec(5))
