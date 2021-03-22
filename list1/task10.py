import numpy as np
import matplotlib.pyplot as plt
from scipy import linalg

roValues = [0, 0.25, 0.5, 0.75, 0.9]
numberOfSamples = 1000
dt = 1
X_0 = 10
mu = 0.04
sigma = 0.4

def ABMTrajectory(numberOfSamples, M):
    firstTrajectory = [X_0]
    secTrajectory = [X_0]
    for i in range(1, numberOfSamples, 1):
        firstTrajectory.append(firstTrajectory[i-1] + mu * dt + sigma * M[0][i-1])
        secTrajectory.append(secTrajectory[i-1] + mu * dt + sigma * M[1][i-1])
    return np.array(firstTrajectory), np.array(secTrajectory)

def detTrend(numberOfSamples):
    trendSamples = [X_0]
    for i in range(1, numberOfSamples, 1):
        trendSamples.append(trendSamples[i-1] + mu*dt)
    return np.array(trendSamples)

def correlationSamplesGenerator(covMatrix):
    Z = np.random.normal(0, 1, (2, numberOfSamples))
    C = linalg.cholesky(covMatrix)
    M = np.dot(C.transpose(), Z)
    return M


if __name__ == "__main__":
    for ro in roValues:
        covMatrix = np.array([[1, ro], [ro, 1]])
        samples = correlationSamplesGenerator(covMatrix)
        plt.plot(detTrend(numberOfSamples), 'r--', label="Deterministic trend")
        t1, t2 = ABMTrajectory(numberOfSamples, samples)

        plt.plot(t1, label="Trajectory 1")
        plt.plot(t2, label="Trajectory 2")
        plt.ylabel('Value')
        plt.xlabel('Sample');
        plt.title("Dependent trajectories of arithmetic Brown motion")
        plt.legend(loc='best', frameon=False)
        plt.grid()
        plt.show()
