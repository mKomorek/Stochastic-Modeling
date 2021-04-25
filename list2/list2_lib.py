import os
import matplotlib.pyplot as plt

N = 1000
beta = 0.5
gamma = 0.1
eta = 0.2
sigma = 0.3
T = 100

def plot_model(T, data, title, logScale, savePath=None):
    for key in data.keys():
        if key.find('DOPRI') > 0:
            plt.plot(T, data[key], '--', label=f"${key}_t$")
        else:
            plt.plot(T, data[key], label=f"${key}_t$")
    if logScale: apply_log_scale()
    apply_chart_properties(title)
    if savePath: save_file(savePath)
    plt.cla()

def apply_log_scale():
    plt.yscale("log")

def apply_chart_properties(title):
    plt.xlabel(f"Czas[np. dni]")
    plt.ylabel(f"Liczba przypadków (osób)")
    plt.title(title)
    plt.legend(loc='best', frameon=False)
    plt.grid()

def mkdir_p(myPath):
    from errno import EEXIST
    from os import makedirs,path

    try:
        makedirs(myPath)
    except OSError as exc:
        if exc.errno == EEXIST and path.isdir(myPath):
            pass
        else: raise

def save_file(savePath):
    myPath = os.path.abspath(__file__)
    dirPath = savePath[ : savePath.find('/')]
    mkdir_p(dirPath)
    plt.savefig(savePath, dpi=600)
