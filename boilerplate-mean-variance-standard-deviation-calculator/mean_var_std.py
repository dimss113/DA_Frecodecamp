import numpy as np

def calculate(list):
    if len(list) != 9:
        raise ValueError("List must contain nine numbers")
    
    matrix3d = np.fromiter(list, dtype=float)
    matrix3d.resize(3,3)
    # print(matrix3d)

    mean = [
        [matrix3d.mean(axis=0).tolist()],
        [matrix3d.mean(axis=1).tolist()],
        [matrix3d.flatten().mean().tolist()]
    ]
    variance = [
        [matrix3d.var(axis=0).tolist()],
        [matrix3d.var(axis=1).tolist()],
        [matrix3d.flatten().var().tolist()]
    ]

    standard_deviation = [
        [matrix3d.std(axis=0).tolist()],
        [matrix3d.std(axis=1).tolist()],
        [matrix3d.flatten().std().tolist()]
    ]

    max = [
        [matrix3d.max(axis=0).tolist()],
        [matrix3d.max(axis=1).tolist()],
        [matrix3d.flatten().max().tolist()]
    ]
    min = [
        [matrix3d.min(axis=0).tolist()],
        [matrix3d.min(axis=1).tolist()],
        [matrix3d.flatten().min().tolist()]
    ]
    sum = [
        [matrix3d.sum(axis=0).tolist()],
        [matrix3d.sum(axis=1).tolist()],
        [matrix3d.flatten().sum().tolist()]
    ]

    return {
        'mean': mean,
        'variance': variance,
        'standard deviation': standard_deviation,
        'max': max,
        'min': min,
        'sum': sum
    }

# hasil = calculate([0,1,2,3,4,5,6,7,8])

# for tup in hasil:
#     print(tup, hasil[tup])
