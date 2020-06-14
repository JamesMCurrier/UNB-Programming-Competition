def can_fold(x: float, y: float, z: float) -> bool:
    """Determines whether a sheet of paper can be folded"""
    
    return max(x, y) / 2 > 3 * z


# Get inputs
x, y = [float(i) for i in input().split()]
z = float(input())

num_folds = 0


# Fold the paper until it is no longer possible
while can_fold(x, y, z):
    num_folds += 1

    if x > y:
        x = x / 2

    else:
        y = y / 2

    z *= 2


print(num_folds)
