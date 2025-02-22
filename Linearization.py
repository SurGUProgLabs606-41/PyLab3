# Итеративный вариант
def linearize_iter(lst):
    result = []
    stack = [lst]
    while stack:
        curr = stack.pop()
        if isinstance(curr, list):
            stack.extend(reversed(curr))
        else:
            result.append(curr)
    return result

# Рекурсивный вариант
def linearize_rec(lst):
    if not lst:
        return []
    if isinstance(lst[0], list):
        return linearize_rec(lst[0]) + linearize_rec(lst[1:])
    return [lst[0]] + linearize_rec(lst[1:])

# Тест
print(linearize_iter([1, 2, [3, 4, [5, [6, []]]]]))
print(linearize_rec([1, 2, [3, 4, [5, [6, []]]]]))
