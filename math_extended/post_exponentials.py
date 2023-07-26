def tetration(a, b):
    """Computes a^^b."""
    return eval(f'{a}' + f' ** {a}' * (b - 1))


if __name__ == '__main__':
    print(tetration(3, 3))
