import numpy as np
from scipy.integrate import RK45
import list2_lib as lib

def SI_model_dopri(dt):
    def SI_ode(t, y):
        S0, I0 = y
        S1 = -lib.beta*I0*S0/lib.N
        I1 = lib.beta*I0*S0/lib.N
        return [S1, I1]

    time = int(lib.T/dt)
    T_ode = np.zeros(time)
    Y = np.zeros((time, 2))
    Y[0, :] = [lib.N - 1, 1]
    for T in range(time-1):
        ode_system = RK45(lambda t, y: SI_ode(t, y), T_ode[T], Y[T, :], T_ode[T]+dt)
        while ode_system.status == 'running':
            ode_system.step()
        Y[T + 1, :] = ode_system.y
        T_ode[T + 1] = ode_system.t

    return (T_ode, {'S^{DOPRI}': Y[:, 0].astype(int), 'I^{DOPRI}': Y[:, 1].astype(int)})

def SIS_model_dopri(dt):
    def SIS_ode(t, y):
        S0, I0 = y
        S1 = -lib.beta*I0*S0/lib.N + lib.gamma*I0
        I1 = lib.beta*I0*S0/lib.N - lib.gamma*I0
        return [S1, I1]

    time = int(lib.T/dt)
    T_ode = np.zeros(time)
    Y = np.zeros((time, 2))
    Y[0, :] = [lib.N - 1, 1]
    for T in range(time-1):
        ode_system = RK45(lambda t, y: SIS_ode(t, y), T_ode[T], Y[T, :], T_ode[T]+dt)
        while ode_system.status == 'running':
            ode_system.step()
        Y[T + 1, :] = ode_system.y
        T_ode[T + 1] = ode_system.t

    return (T_ode, {'S^{DOPRI}': Y[:, 0].astype(int), 'I^{DOPRI}': Y[:, 1].astype(int)})

def SIRS_model_dopri(dt):
    def SIRS_ode(t, y):
        S0, I0, R0 = y
        S1 = -lib.beta*I0*S0/lib.N + lib.eta*R0
        I1 = lib.beta*I0*S0/lib.N - lib.gamma*I0
        R1 = lib.gamma*I0 - lib.eta*R0
        return [S1, I1, R1]

    time = int(lib.T/dt)
    T_ode = np.zeros(time)
    Y = np.zeros((time, 3))
    Y[0, :] = [lib.N - 1, 1, 0]
    for T in range(time-1):
        ode_system = RK45(lambda t, y: SIRS_ode(t, y), T_ode[T], Y[T, :], T_ode[T]+dt)
        while ode_system.status == 'running':
            ode_system.step()
        Y[T + 1, :] = ode_system.y
        T_ode[T + 1] = ode_system.t

    return (T_ode, {'S^{DOPRI}': Y[:, 0].astype(int), 'I^{DOPRI}': Y[:, 1].astype(int), 'R^{DOPRI}': Y[:, 2].astype(int)})

if __name__ == "__main__":
    lib.plot_model(*SI_model_dopri(1),
        f"Ewolucja SI dla N={lib.N}, $I_0$=1, $\\beta$={lib.beta}",
        False,
        "task2Results/SI_dopri_model.png")
    lib.plot_model(*SIS_model_dopri(1),
        f"Ewolucja SIS dla N={lib.N}, $I_0$=1, $\\beta$={lib.beta}, $\\gamma$={lib.gamma}",
        False,
        "task2Results/SIS_dorpi_model.png")
    lib.plot_model(*SIRS_model_dopri(1),
        f"Ewolucja SIRS dla N={lib.N}, $I_0$=1, $\\beta$={lib.beta}, $\\gamma$={lib.gamma}, $\\eta$={lib.eta}",
        False,
        "task2Results/SIRS_dopri_model.png")

    lib.plot_model(*SI_model_dopri(1),
        f"Ewolucja SI dla N={lib.N}, $I_0$=1, $\\beta$={lib.beta}",
        True,
        "task2Results/SI_dopri_model_log.png")
    lib.plot_model(*SIS_model_dopri(1),
        f"Ewolucja SIS dla N={lib.N}, $I_0$=1, $\\beta$={lib.beta}, $\\gamma$={lib.gamma}",
        True,
        "task2Results/SIS_dorpi_model_log.png")
    lib.plot_model(*SIRS_model_dopri(1),
        f"Ewolucja SIRS dla N={lib.N}, $I_0$=1, $\\beta$={lib.beta}, $\\gamma$={lib.gamma}, $\\eta$={lib.eta}",
        True,
        "task2Results/SIRS_dopri_model_log.png")
