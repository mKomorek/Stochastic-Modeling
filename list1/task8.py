import numpy as np
import matplotlib.pyplot as plt

X_zero = 20
dt = 1
alpha = 0.1
beta = 8
sigma = 0.4

def trajectoriesDiffusion(numberOfSamples):
    trajectorieSamples = [X_zero]
    for i in range(1, numberOfSamples, 1):
        trajectorieSamples.append(trajectorieSamples[i-1]
            + alpha * (beta - trajectorieSamples[i-1]) * dt
            + sigma * np.random.normal(0,1))
    return np.array(trajectorieSamples)

def deterministicTrend(numberOfSamples):
    trendSamples = [X_zero]
    for i in range(1, numberOfSamples, 1):
        trendSamples.append(trendSamples[i-1] + alpha*(beta-trendSamples[i-1])*dt)
    return np.array(trendSamples)

if __name__ == "__main__":
    plt.plot(deterministicTrend(400), 'r--')
    for x in range(3):
        plt.plot(trajectoriesDiffusion(400))

    plt.grid()
    plt.show()
