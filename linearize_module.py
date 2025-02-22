from collections import deque

def linearize_iter(lst):
    result = []
    stack = deque([lst])
    while stack:
        curr = stack.pop()
        if isinstance(curr, list):
            stack.extend(reversed(curr))
        else:
            result.append(curr)
    return result

def linearize_rec(lst):
    result = []
    def helper(sublist):
        for item in sublist:
            if isinstance(item, list):
                helper(item)
            else:
                result.append(item)
    helper(lst)
    return result

print(linearize_iter([1, 2, [3, 4, [5, [6, []]]]]))
print(linearize_rec([1, 2, [3, 4, [5, [6, []]]]]))