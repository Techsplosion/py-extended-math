def tetration(a, b):
    """Computes a^^b recursively."""
    if (b == 1) return a
    return a ** tetration(a, b - 1)


if __name__ == '__main__':
    print(tetration(3, 3))
