import matplotlib.pyplot as plt
import numpy as np
import task1 as task1
import task5 as task5
import list2_lib as lib

def fan_chart_SI():
    figS = plt.figure()
    axS = figS.add_subplot(1,1,1)
    figI = plt.figure()
    axI = figI.add_subplot(1,1,1)
    T_plt, SIDataDeterministic = task1.SI_model(1)
    for i in range(lib.T):
        lib.loading(i)
        T_plt, SIData = task5.SI_model()
        alpha = 0.1*(i+1)/lib.T
        axS.fill_between(T_plt, SIDataDeterministic['S'], SIData['S'], color='red', alpha=alpha)
        axI.fill_between(T_plt, SIDataDeterministic['I'], SIData['I'], color='red', alpha=alpha)

    axS.plot(T_plt, SIDataDeterministic['S'], '--', color='black')
    lib.apply_chart_properties_ax(axS, f"Fan chart $S_t$ dla N={lib.N}, $I_0$=1, $\\beta$={lib.beta}")
    lib.save_file_fig("task7Results/SI_model_St.png", figS)

    axI.plot(T_plt, SIDataDeterministic['I'], '--', color='black')
    lib.apply_chart_properties_ax(axI, f"Fan chart $I_t$ dla N={lib.N}, $I_0$=1, $\\beta$={lib.beta}")
    lib.save_file_fig("task7Results/SI_model_It.png", figI)

def fan_chart_SIS():
    figS = plt.figure()
    axS = figS.add_subplot(1,1,1)
    figI = plt.figure()
    axI = figI.add_subplot(1,1,1)
    T_plt, SISDataDeterministic = task1.SIS_model(1)
    for i in range(lib.T):
        lib.loading(i)
        T_plt, SISData = task5.SIS_model()
        alpha = 0.1*(i+1)/lib.T
        axS.fill_between(T_plt, SISDataDeterministic['S'], SISData['S'], color='red', alpha=alpha)
        axI.fill_between(T_plt, SISDataDeterministic['I'], SISData['I'], color='red', alpha=alpha)

    axS.plot(T_plt, SISDataDeterministic['S'], '--', color='black')
    lib.apply_chart_properties_ax(axS, f"Fan chart $S_t$ dla N={lib.N}, $\\beta$={lib.beta}, $\\gamma$={lib.gamma}")
    lib.save_file_fig("task7Results/SIS_model_St.png", figS)

    axI.plot(T_plt, SISDataDeterministic['I'], '--', color='black')
    lib.apply_chart_properties_ax(axI, f"Fan chart $I_t$ dla N={lib.N}, $\\beta$={lib.beta}, $\\gamma$={lib.gamma}")
    lib.save_file_fig("task7Results/SIS_model_It.png", figI)

def fan_chart_SIRS():
    figS = plt.figure()
    axS = figS.add_subplot(1,1,1)
    figI = plt.figure()
    axI = figI.add_subplot(1,1,1)
    figR = plt.figure()
    axR = figR.add_subplot(1,1,1)
    T_plt, SIRSDataDeterministic = task1.SIRS_model(1)
    for i in range(lib.T):
        lib.loading(i)
        T_plt, SIRSData = task5.SIRS_model()
        alpha = 0.1*(i+1)/lib.T
        axS.fill_between(T_plt, SIRSDataDeterministic['S'], SIRSData['S'], color='red', alpha=alpha)
        axI.fill_between(T_plt, SIRSDataDeterministic['I'], SIRSData['I'], color='red', alpha=alpha)
        axR.fill_between(T_plt, SIRSDataDeterministic['R'], SIRSData['R'], color='red', alpha=alpha)

    axS.plot(T_plt, SIRSDataDeterministic['S'], '--', color='black')
    lib.apply_chart_properties_ax(axS, f"Fan chart $S_t$ dla N={lib.N}, $I_0$=1, $\\beta$={lib.beta}, $\\gamma$={lib.gamma}, $\\eta$={lib.eta}")
    lib.save_file_fig("task7Results/SIRS_model_St.png", figS)

    axI.plot(T_plt, SIRSDataDeterministic['I'], '--', color='black')
    lib.apply_chart_properties_ax(axI, f"Fan chart $I_t$ dla N={lib.N}, $I_0$=1, $\\beta$={lib.beta}, $\\gamma$={lib.gamma}, $\\eta$={lib.eta}")
    lib.save_file_fig("task7Results/SIRS_model_It.png", figI)

    axR.plot(T_plt, SIRSDataDeterministic['R'], '--', color='black')
    lib.apply_chart_properties_ax(axR, f"Fan chart $R_t$ dla N={lib.N}, $I_0$=1, $\\beta$={lib.beta}, $\\gamma$={lib.gamma}, $\\eta$={lib.eta}")
    lib.save_file_fig("task7Results/SIRS_model_Rt.png", figR)

if __name__ == "__main__":
    fan_chart_SI()
    fan_chart_SIS()
    fan_chart_SIRS()
