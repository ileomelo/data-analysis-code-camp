import numpy as np

INPUT_LIST = [0,1,2,3,4,5,6,7,8]

def calculate(INPUT_LIST):
    if len(INPUT_LIST) != 9:
        raise ValueError("List must contain nine numbers")
    
    # Transformar a lista em uma matriz 3x3
    matrix = np.array(INPUT_LIST).reshape(3,3)

    calculations = {
        'mean': [
            matrix.mean(axis=0).tolist(),
            matrix.mean(axis=1).tolist(),
            matrix.mean()
        ],
        'variance': [
            matrix.mean(axis=0).tolist(),
            matrix.mean(axis=1).tolist(),
            matrix.var()
        ],
        'standard deviation': [
            matrix.mean(axis=0).tolist(),
            matrix.mean(axis=1).tolist(),
            matrix.std()
        ],
        'max': [
            matrix.mean(axis=0).tolist(),
            matrix.mean(axis=1).tolist(),
            matrix.max()
        ],
        'min': [
            matrix.mean(axis=0).tolist(),
            matrix.mean(axis=1).tolist(),
            matrix.min()
        ],
        'sum': [
            matrix.mean(axis=0).tolist(),
            matrix.mean(axis=1).tolist(),
            matrix.sum()
        ]
    }
    return calculations

results = calculate(INPUT_LIST)

print(results)