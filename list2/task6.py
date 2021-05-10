import numpy as np
import list2_lib as lib

def init_values(time):
    T_plt = np.arange(0, lib.T, 1)
    S = np.zeros(time)
    E = np.zeros(time)
    I = np.zeros(time)
    R = np.zeros(time)
    E[0] = 1
    S[0] = lib.N - E[0]
    return T_plt, S, E, I, R

def SEIR_model():
    T_plt, S, E, I, R = init_values(lib.T)
    for x in range(lib.T-1):
        S[x+1] = S[x]
        E[x+1] = E[x]
        I[x+1] = I[x]
        R[x+1] = R[x]
        for i in range(lib.N):
            pS = (lib.beta*I[x]*S[x])/(lib.N*lib.N)
            pE = lib.sigma*E[x]/lib.N
            pI = lib.gamma*I[x]/lib.N
            US = np.random.uniform(0, 1)
            UE = np.random.uniform(0, 1)
            UI = np.random.uniform(0, 1)
            if US < pS:
                S[x+1] -= 1
                E[x+1] += 1
            if UE < pE:
                I[x+1] += 1
                E[x+1] -= 1
            if UI < pI:
                R[x+1] += 1
                I[x+1] -= 1
    return (T_plt, {'S': S, 'E': E, 'I': I, 'R': R})

def SEIRS_model():
    T_plt, S, E, I, R = init_values(lib.T)
    for x in range(lib.T-1):
        S[x+1] = S[x]
        E[x+1] = E[x]
        I[x+1] = I[x]
        R[x+1] = R[x]
        for i in range(lib.N):
            pS = (lib.beta*I[x]*S[x])/(lib.N*lib.N)
            pE = lib.sigma*E[x]/lib.N
            pI = lib.gamma*I[x]/lib.N
            pR = lib.eta*R[x]/lib.N
            US = np.random.uniform(0, 1)
            UE = np.random.uniform(0, 1)
            UI = np.random.uniform(0, 1)
            UR = np.random.uniform(0, 1)
            if US < pS:
                S[x+1] -= 1
                E[x+1] += 1
            if UE < pE:
                I[x+1] += 1
                E[x+1] -= 1
            if UI < pI:
                R[x+1] += 1
                I[x+1] -= 1
            if UR < pR:
                R[x+1] -= 1
                S[x+1] += 1
    return (T_plt, {'S': S, 'E': E, 'I': I, 'R': R})

if __name__ == "__main__":
    lib.plot_model(*SEIR_model(),
        f"Ewolucja SEIR dla N={lib.N}, $E_0$=1, $\\beta$={lib.beta}, $\\sigma$={lib.sigma}, $\\eta$={lib.eta}",
        False,
        "task6Results/SEIR_model.png")

    lib.plot_model(*SEIRS_model(),
        f"Ewolucja SEIRS dla N={lib.N}, $E_0$=1, $\\beta$={lib.beta}, $\\sigma$={lib.sigma}, $\\eta$={lib.eta}",
        False,
        "task6Results/SEIRS_model.png")

    lib.plot_model(*SEIR_model(),
        f"Ewolucja SEIR dla N={lib.N}, $E_0$=1, $\\beta$={lib.beta}, $\\sigma$={lib.sigma}, $\\eta$={lib.eta}",
        True,
        "task6Results/SEIR_model_log.png")

    lib.plot_model(*SEIRS_model(),
        f"Ewolucja SEIRS dla N={lib.N}, $E_0$=1, $$\\beta$={lib.beta}, $\\sigma$={lib.sigma}, $\\eta$={lib.eta}",
        True,
        "task6Results/SEIRS_model_log.png")
