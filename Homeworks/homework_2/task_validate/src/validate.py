def validate(pushed: list[int], popped: list[int]) -> bool:
    if len(pushed) != len(popped):
        return False

    stack = []
    j = 0 
    for x in pushed:
        stack.append(x)
        while stack and j < len(popped) and stack[-1] == popped[j]:
            stack.pop()
            j += 1

    return not stack