import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

def ruleOfTheDozen(numberOfSamples):
    N = np.full(numberOfSamples, 6.0, dtype=float)
    sumU = np.zeros([numberOfSamples])
    for i in range(12):
        U = np.random.uniform(0.0, 1.0, numberOfSamples)
        sumU += U
    N = sumU - N
    return N

def inverseTransform(numberOfSamples):
    U = np.random.uniform(0.0, 1.0, numberOfSamples)
    U = norm.ppf(U)
    return U

def boxMuller(numberOfSamples):
    # Probably there is another, better way to do it.
    # Probably by use vector paradigma.
    N = []
    U = np.random.uniform(0.0, 1.0, numberOfSamples)
    for i in range(0, numberOfSamples, 2):
        z1 = np.sqrt(-2*np.log(U[i])) * np.cos(2*np.pi*U[i+1])
        z2 = np.sqrt(-2*np.log(U[i])) * np.sin(2*np.pi*U[i+1])
        N.extend([z1, z2])
    return np.array(N)

def calculateBins(normalDistributionSamples):
    q25, q75 = np.percentile(normalDistributionSamples, [.25,.75])
    binWidth = 2 * (q75-q25) * len(normalDistributionSamples) ** (-1/3)
    return round(
        (normalDistributionSamples.max()-normalDistributionSamples.min()) / binWidth
    )
def plotHistogramWithPDF(normalDistributionSamples):
    bins = calculateBins(normalDistributionSamples)
    fig, ax = plt.subplots()

    ax.hist(normalDistributionSamples, density=True, bins=bins, label='f_emp(x)')
    x = np.linspace(norm.ppf(0.001), norm.ppf(0.999), 1000)
    ax.plot(x, norm.pdf(x), 'r-', lw=2, label='N(0,1)')
    ax.legend(loc='best', frameon=False)

    ax.set_xticks(np.arange(-3.5, 3.51, 0.5))
    ax.set_yticks(np.arange(0, 0.6, 0.05))
    plt.grid()
    plt.ylabel('Probability')
    plt.xlabel('Data');
    plt.title("Histogram")
    plt.show()

if __name__ == "__main__":
    ruleOfTheDozenSamples = ruleOfTheDozen(1000)
    plotHistogramWithPDF(ruleOfTheDozenSamples)

    inverseTransformSamples = inverseTransform(1000)
    plotHistogramWithPDF(inverseTransformSamples)

    boxMullerSamples = boxMuller(1000)
    plotHistogramWithPDF(boxMullerSamples)
