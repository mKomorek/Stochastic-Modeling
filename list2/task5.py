import list2_lib as lib
import numpy as np

def init_values(time):
    T_plt = np.arange(0, lib.T, 1)
    S = np.zeros(time)
    I = np.zeros(time)
    S[0] = lib.N - 1
    I[0] = 1
    return T_plt, S, I

def SI_model():
    T_plt, S, I = init_values(lib.T)
    for x in range(lib.T-1):
        S[x+1] = S[x]
        I[x+1] = I[x]
        for i in range(lib.N):
            pS = (lib.beta*I[x]*S[x])/(lib.N*lib.N)
            U = np.random.uniform(0, 1)
            if U < pS:
                S[x+1] -= 1
                I[x+1] += 1
    return (T_plt, {'S': S, 'I': I})

def SIS_model():
    T_plt, S, I = init_values(lib.T)
    for x in range(lib.T-1):
        S[x+1] = S[x]
        I[x+1] = I[x]
        for i in range(lib.N):
            pS = (lib.beta*I[x]*S[x])/(lib.N*lib.N)
            pI = lib.gamma*I[x]/lib.N
            US = np.random.uniform(0, 1)
            UI = np.random.uniform(0, 1)
            if US < pS:
                S[x+1] -= 1
                I[x+1] += 1
            if UI < pI:
                S[x+1] += 1
                I[x+1] -= 1
    return (T_plt, {'S': S, 'I': I})

def SIRS_model():
    T_plt, S, I = init_values(lib.T)
    R = np.zeros(lib.T)
    for x in range(lib.T-1):
        S[x+1] = S[x]
        I[x+1] = I[x]
        R[x+1] = R[x]
        for i in range(lib.N):
            pS = (lib.beta*I[x]*S[x])/(lib.N*lib.N)
            pI = lib.gamma*I[x]/lib.N
            pR = lib.eta*R[x]/lib.N
            US = np.random.uniform(0, 1)
            UI = np.random.uniform(0, 1)
            UR = np.random.uniform(0, 1)
            if US < pS:
                S[x+1] -= 1
                I[x+1] += 1
            if UI < pI:
                R[x+1] += 1
                I[x+1] -= 1
            if UI < pR:
                S[x+1] += 1
                R[x+1] -= 1
    return (T_plt, {'S': S, 'I': I, 'R': R})

if __name__ == "__main__":
    lib.plot_model(*SI_model(),
        f"Ewolucja SI dla N={lib.N}, $\\beta$={lib.beta}",
        False,
        "task5Results/SI_model.png")
    lib.plot_model(*SIS_model(),
        f"Ewolucja SIS dla N={lib.N}, $\\beta$={lib.beta}, $\\gamma$={lib.gamma}",
        False,
        "task5Results/SIS_model.png")
    lib.plot_model(*SIRS_model(),
        f"Ewolucja SIRS dla N={lib.N}, $\\beta$={lib.beta}, $\\gamma$={lib.gamma}, $\\eta$={lib.eta}",
        False,
        "task5Results/SIRS_model.png")

    lib.plot_model(*SI_model(),
        f"Ewolucja SI dla N={lib.N}, $\\beta$={lib.beta}",
        True,
        "task5Results/SI_model_log.png")
    lib.plot_model(*SIS_model(),
        f"Ewolucja SIS dla N={lib.N}, $\\beta$={lib.beta}, $\\gamma$={lib.gamma}",
        True,
        "task5Results/SIS_model_log.png")
    lib.plot_model(*SIRS_model(),
        f"Ewolucja SIRS dla N={lib.N}, $\\beta$={lib.beta}, $\\gamma$={lib.gamma}, $\\eta$={lib.eta}",
        True,
        "task5Results/SIRS_model_log.png")
