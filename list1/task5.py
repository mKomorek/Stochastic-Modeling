import numpy as np
import matplotlib.pyplot as plt

X_zero = 10
dt = 1
sigma = 0.04
my = 0.01

def trajectoriesGBM(numberOfSamples):
    trajectorieSamples = [X_zero]
    for i in range(1, numberOfSamples, 1):
        trajectorieSamples.append(
            trajectorieSamples[i-1] * np.power(
                np.e, (my-np.power(sigma, 2)/2) + sigma*np.random.normal(0,1)))
    return np.array(trajectorieSamples)

def deterministicTrend(numberOfSamples):
    trendSamples = [X_zero]
    for i in range(1, numberOfSamples, 1):
        trendSamples.append(trendSamples[i-1] * np.power(np.e, my))
    return np.array(trendSamples)

if __name__ == "__main__":
    plt.plot(deterministicTrend(200), 'r--')
    for x in range(3):
        plt.plot(trajectoriesGBM(200))

    plt.grid()
    plt.show()
