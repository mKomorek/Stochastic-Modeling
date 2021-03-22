import numpy as np
import matplotlib.pyplot as plt

X_zero = 10
dt = 1
sigma = 0.4
my = 0.04

def trajectoriesABM(numberOfSamples):
    trajectorieSamples = [X_zero]
    for i in range(1, numberOfSamples, 1):
        trajectorieSamples.append(trajectorieSamples[i-1]
            + my * dt
            + sigma * np.random.normal(0,1))
    return np.array(trajectorieSamples)

def deterministicTrend(numberOfSamples):
    trendSamples = [X_zero]
    for i in range(1, numberOfSamples, 1):
        trendSamples.append(trendSamples[i-1] + my*dt)
    return np.array(trendSamples)

if __name__ == "__main__":
    plt.plot(deterministicTrend(1000), 'r--', label=f"Deterministic trend")
    for x in range(3):
        plt.plot(trajectoriesABM(1000), label=f"Trajectory {x+1}")

    plt.ylabel('Value')
    plt.xlabel('Sample');
    plt.title("Trajectories of arithmetic Brown motion")
    plt.legend(loc='best', frameon=False)
    plt.grid()
    plt.show()
