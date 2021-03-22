import numpy as np
import statistics
import math

def generateSamples(numberOfSamples):
    uniformSamples = np.random.uniform(0, 1, numberOfSamples)
    for i in range(len(uniformSamples)):
        uniformSamples[i] *= 2
        uniformSamples[i] += 1
    return uniformSamples

def calculateRectangles(vec):
    Y = []
    for sam in vec:
        Y.append((pow(sam, 2) + sam) * 2)
    return np.array(Y)

def MC(vec):
    mean = np.mean(vec)
    std = np.std(vec)
    lower_band_b = mean - (1.96 * (std/math.sqrt(len(vec))))
    upper_band_b = mean + (1.96 * (std/math.sqrt(len(vec))))
    return mean, lower_band_b, upper_band_b


if __name__ == "__main__":
    numberOfSamples = 1000
    generatedSamples = generateSamples(numberOfSamples)
    y = calculateRectangles(generatedSamples)
    integral, lower_band, upper_band = MC(y)
    print(f"Integral value: {integral}")
    print(f"[{lower_band}, {upper_band}]")
