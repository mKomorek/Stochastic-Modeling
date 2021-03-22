import numpy as np
import matplotlib.pyplot as plt
from scipy import linalg

roValues = [0, 0.25, 0.5, 0.75, 0.9]

if __name__ == "__main__":
    for ro in roValues:
        covMatrix = np.array([[1, ro], [ro, 1]])
        Z = np.random.normal(0, 1, (2, 100000))
        C = linalg.cholesky(covMatrix)
        M = np.dot(C.transpose(), Z)

        x = np.array(M[0, :])
        y = np.array(M[1, :])

        plt.title("Two-dimensional normal distribution")
        plt.plot(x, y, '.')
        plt.grid()
        plt.show()
