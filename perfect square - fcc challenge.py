def is_perfect_square(n):
    if n < 0:
        return False
    root = n ** (1/2)
    return int(root) == root


print(is_perfect_square(49))
print(is_perfect_square(2))

