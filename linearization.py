# Итеративный вариант
def linearize_iter(lst):
    result = [] # Пустой список для результата
    stack = [lst] # Инициализация стека с начальным списком
    while stack: # Пока стек не пуст
        curr = stack.pop() # Извлечение последнего элемента из стека
        if isinstance(curr, list): # Если это список
            stack.extend(reversed(curr)) # Добавление его элемента в стек в обратном порядке
        else: # Если это не список (элемент)
            result.append(curr) # Добавление элемента в результат
    return result # Возвращение результата

# Рекурсивный вариант
def linearize_rec(lst):
    if not lst: # Если список пуст
        return []
    if isinstance(lst[0], list): # Если первый элемент — список
        return linearize_rec(lst[0]) + linearize_rec(lst[1:]) # Рекурсивно линеаризуем (преобразование сложной структуры) его и оставшуюся часть
    return [lst[0]] + linearize_rec(lst[1:]) # Добавление первого элемента и рекурсивная обрабатотка оставшейся части

# Тест
print(linearize_iter([1, 2, [3, 4, [5, [6, []]]]])) # Итеративный вариант
print(linearize_rec([1, 2, [3, 4, [5, [6, []]]]])) # Рекурсивный вариант
