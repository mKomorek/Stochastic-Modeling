import numpy as np
from scipy.integrate import RK45
import list2_lib as lib

def init_values(time):
    S = np.zeros(time)
    E = np.zeros(time)
    I = np.zeros(time)
    R = np.zeros(time)
    E[0] = 1
    S[0] = lib.N - E[0]
    return S, E, I, R

def SEIR_model(dt):
    time = int(lib.T/dt)
    T_plt = np.arange(0, lib.T, dt)
    S, E, I, R = init_values(time)
    for x in range(time-1):
        S[x+1] = S[x] + dt*(-lib.beta*I[x]*S[x]/lib.N)
        E[x+1] = E[x] + dt*(lib.beta*I[x]*S[x]/lib.N - lib.sigma*E[x])
        I[x+1] = I[x] + dt*(lib.sigma*E[x] - lib.gamma*I[x])
        R[x+1] = R[x] + dt*(lib.gamma*I[x])

    return (T_plt, {'S': S, 'E':E, 'I': I, 'R': R})

def SEIRS_model(dt):
    time = int(lib.T/dt)
    T_plt = np.arange(0, lib.T, dt)
    S, E, I, R = init_values(time)
    for x in range(time-1):
        S[x+1] = S[x] + dt*(-lib.beta*I[x]*S[x]/lib.N + lib.eta*R[x])
        E[x+1] = E[x] + dt*(lib.beta*I[x]*S[x]/lib.N - lib.sigma*E[x])
        I[x+1] = I[x] + dt*(lib.sigma*E[x] - lib.gamma*I[x])
        R[x+1] = R[x]+ dt*(lib.gamma*I[x] - lib.eta*R[x])

    return (T_plt, {'S': S, 'E':E, 'I': I, 'R': R})

def SEIR_dopri_model(dt):
    def SEIR_ode(t, y):
        S0, E0, I0, R0 = y
        S1 = -lib.beta*I0*S0/lib.N
        E1 = lib.beta*I0*S0/lib.N - lib.sigma*E0
        I1 = lib.sigma*E0 - lib.gamma*I0
        R1 = lib.gamma*I0
        return [S1, E1, I1, R1]

    time = int(lib.T/dt)
    T_ode = np.zeros(time)
    Y = np.zeros((time, 4))
    Y[0, :] = [lib.N - 1, 1, 0, 0]
    for T in range(time-1):
        ode_system = RK45(lambda t, y: SEIR_ode(t, y), T_ode[T], Y[T, :], T_ode[T]+dt)
        while ode_system.status == 'running':
            ode_system.step()
        Y[T + 1, :] = ode_system.y
        T_ode[T + 1] = ode_system.t

    return (T_ode, {'S^{DOPRI}': Y[:, 0], 'E^{DOPRI}': Y[:, 1], 'I^{DOPRI}': Y[:, 2], 'R^{DOPRI}': Y[:, 3]})

def SEIRS_dopri_model(dt):
    def SEIRS_ode(t, y):
        S0, E0, I0, R0 = y
        S1 = -lib.beta*I0*S0/lib.N + lib.eta*R0
        E1 = lib.beta*I0*S0/lib.N - lib.sigma*E0
        I1 = lib.sigma*E0 - lib.gamma*I0
        R1 = lib.gamma*I0 - lib.eta*R0
        return [S1, E1, I1, R1]

    time = int(lib.T/dt)
    T_ode = np.zeros(time)
    Y = np.zeros((time, 4))
    Y[0, :] = [lib.N - 1, 1, 0, 0]
    for T in range(time-1):
        ode_system = RK45(lambda t, y: SEIRS_ode(t, y), T_ode[T], Y[T, :], T_ode[T]+dt)
        while ode_system.status == 'running':
            ode_system.step()
        Y[T + 1, :] = ode_system.y
        T_ode[T + 1] = ode_system.t

    return (T_ode, {'S^{DOPRI}': Y[:, 0], 'E^{DOPRI}': Y[:, 1], 'I^{DOPRI}': Y[:, 2], 'R^{DOPRI}': Y[:, 3]})

if __name__ == "__main__":
    lib.plot_model(*SEIR_model(1),
        f"Ewolucja SEIR dla N={lib.N}, $E_0$=1, $\\beta$={lib.beta}, $\\sigma$={lib.sigma}, $\\eta$={lib.eta}",
        False,
        "task3Results/SEIR_model.png")
    lib.plot_model(*SEIRS_model(1),
        f"Ewolucja SEIRS dla N={lib.N}, $E_0$=1, $\\beta$={lib.beta}, $\\sigma$={lib.sigma}, $\\eta$={lib.eta}",
        False,
        "task3Results/SEIRS_model.png")
    lib.plot_model(*SEIR_dopri_model(1),
        f"Ewolucja SEIR dla N={lib.N}, $E_0$=1, $\\beta$={lib.beta}, $\\sigma$={lib.sigma}, $\\eta$={lib.eta}",
        False,
        "task3Results/SEIR_dopri_model.png")
    lib.plot_model(*SEIRS_dopri_model(1),
        f"Ewolucja SEIRS dla N={lib.N}, $E_0$=1, $\\beta$={lib.beta}, $\\sigma$={lib.sigma}, $\\eta$={lib.eta}",
        False,
        "task3Results/SEIRS_dopri_model.png")

    lib.plot_model(*SEIR_model(1),
        f"Ewolucja SEIR dla N={lib.N}, $E_0$=1, $\\beta$={lib.beta}, $\\sigma$={lib.sigma}, $\\eta$={lib.eta}",
        True,
        "task3Results/SEIR_model_log.png")
    lib.plot_model(*SEIRS_model(1),
        f"Ewolucja SEIRS dla N={lib.N}, $E_0$=1, $\\beta$={lib.beta}, $\\sigma$={lib.sigma}, $\\eta$={lib.eta}",
        True,
        "task3Results/SEIRS_model_log.png")
    lib.plot_model(*SEIR_dopri_model(1),
        f"Ewolucja SEIR dla N={lib.N}, $E_0$=1, $\\beta$={lib.beta}, $\\sigma$={lib.sigma}, $\\eta$={lib.eta}",
        True,
        "task3Results/SEIR_dopri_model_log.png")
    lib.plot_model(*SEIRS_dopri_model(1),
        f"Ewolucja SEIRS dla N={lib.N}, $E_0$=1, $\\beta$={lib.beta}, $\\sigma$={lib.sigma}, $\\eta$={lib.eta}",
        True,
        "task3Results/SEIRS_dopri_model_log.png")
