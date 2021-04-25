import list2_lib as lib
import numpy as np

def init_values(time):
    S = np.zeros(time)
    I = np.zeros(time)
    I[0] = 1
    S[0] = lib.N - I[0]
    return S, I

def SI_model(dt):
    time = int(lib.T/dt)
    T_plt = np.arange(0, lib.T, dt)
    S, I = init_values(time)
    for x in range(time-1):
        S[x+1] = S[x] - dt*(lib.beta*I[x]*S[x]/lib.N)
        I[x+1] = I[x] + dt*(lib.beta*I[x]*S[x]/lib.N)

    return (T_plt, {'S': S, 'I': I})

def SIS_model(dt):
    time = int(lib.T/dt)
    T_plt = np.arange(0, lib.T, dt)
    S, I = init_values(time)
    for x in range(time-1):
        S[x+1] = S[x] + dt*(-lib.beta*I[x]*S[x]/lib.N + lib.gamma*I[x])
        I[x+1] = I[x] + dt*(lib.beta*I[x]*S[x]/lib.N - lib.gamma*I[x])

    return (T_plt, {'S': S, 'I': I})

def SIRS_model(dt):
    time = int(lib.T/dt)
    T_plt = np.arange(0, lib.T, dt)
    S, I = init_values(time)
    R = np.zeros(time)
    for x in range(time-1):
        S[x+1] = S[x] + dt*(-lib.beta*I[x]*S[x]/lib.N + lib.eta*R[x])
        I[x+1] = I[x] + dt*(lib.beta*I[x]*S[x]/lib.N - lib.gamma*I[x])
        R[x+1] = R[x] + dt*(lib.gamma*I[x] - lib.eta*R[x])

    return (T_plt, {'S': S, 'I': I, 'R': R})

if __name__ == "__main__":
    lib.plot_model(*SI_model(1),
        f"Ewolucja SI dla N={lib.N}, $I_0$=1, $\\beta$={lib.beta}",
        False,
        "task1Results/SI_model.png")
    lib.plot_model(*SIS_model(1),
        f"Ewolucja SIS dla N={lib.N}, $I_0$=1, $\\beta$={lib.beta}, $\\gamma$={lib.gamma}",
        False,
        "task1Results/SIS_model.png")
    lib.plot_model(*SIRS_model(1),
        f"Ewolucja SIRS dla N={lib.N}, $I_0$=1, $\\beta$={lib.beta}, $\\gamma$={lib.gamma}, $\\eta$={lib.eta}",
        False,
        "task1Results/SIRS_model.png")

    lib.plot_model(*SI_model(1),
        f"Ewolucja SI dla N={lib.N}, $I_0$=1, $\\beta$={lib.beta}",
        True,
        "task1Results/SI_model_log.png")
    lib.plot_model(*SIS_model(1),
        f"Ewolucja SIS dla N={lib.N}, $I_0$=1, $\\beta$={lib.beta}, $\\gamma$={lib.gamma}",
        True,
        "task1Results/SIS_model_log.png")
    lib.plot_model(*SIRS_model(1),
        f"Ewolucja SIRS dla N={lib.N}, $I_0$=1, $\\beta$={lib.beta}, $\\gamma$={lib.gamma}, $\\eta$={lib.eta}",
        True,
        "task1Results/SIRS_model_log.png")
