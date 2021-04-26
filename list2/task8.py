import matplotlib.pyplot as plt
import numpy as np
import task3 as task3
import task6 as task6
import list2_lib as lib

def fan_chart_SEIR():
    figS = plt.figure()
    axS = figS.add_subplot(1,1,1)
    figE = plt.figure()
    axE = figE.add_subplot(1,1,1)
    figI = plt.figure()
    axI = figI.add_subplot(1,1,1)
    figR = plt.figure()
    axR = figR.add_subplot(1,1,1)
    T_plt, SEIRDataDeterministic = task3.SEIR_model(1)
    for i in range(lib.T):
        lib.loading(i)
        T_plt, SEIRData = task6.SEIR_model()
        alpha = 0.1*(i+1)/lib.T
        axS.fill_between(T_plt, SEIRDataDeterministic['S'], SEIRData['S'], color='red', alpha=alpha)
        axE.fill_between(T_plt, SEIRDataDeterministic['E'], SEIRData['E'], color='red', alpha=alpha)
        axI.fill_between(T_plt, SEIRDataDeterministic['I'], SEIRData['I'], color='red', alpha=alpha)
        axR.fill_between(T_plt, SEIRDataDeterministic['R'], SEIRData['R'], color='red', alpha=alpha)

    axS.plot(T_plt, SEIRDataDeterministic['S'], '--', color='black')
    lib.apply_chart_properties_ax(axS, f"Fan chart $S_t$ dla N={lib.N}, $I_0$=1, $\\beta$={lib.beta}, $\\gamma$={lib.gamma}, $\\eta$={lib.eta}")
    lib.save_file_fig("task8Results/SEIR_model_St.png", figS)

    axE.plot(T_plt, SEIRDataDeterministic['E'], '--', color='black')
    lib.apply_chart_properties_ax(axS, f"Fan chart $E_t$ dla N={lib.N}, $I_0$=1, $\\beta$={lib.beta}, $\\gamma$={lib.gamma}, $\\eta$={lib.eta}")
    lib.save_file_fig("task8Results/SEIR_model_Et.png", figE)

    axI.plot(T_plt, SEIRDataDeterministic['I'], '--', color='black')
    lib.apply_chart_properties_ax(axI, f"Fan chart $I_t$ dla N={lib.N}, $I_0$=1, $\\beta$={lib.beta}, $\\gamma$={lib.gamma}, $\\eta$={lib.eta}")
    lib.save_file_fig("task8Results/SEIR_model_It.png", figI)

    axR.plot(T_plt, SEIRDataDeterministic['R'], '--', color='black')
    lib.apply_chart_properties_ax(axR, f"Fan chart $I_t$ dla N={lib.N}, $I_0$=1, $\\beta$={lib.beta}, $\\gamma$={lib.gamma}, $\\eta$={lib.eta}")
    lib.save_file_fig("task8Results/SEIR_model_Rt.png", figR)

def fan_chart_SEIRS():
    figS = plt.figure()
    axS = figS.add_subplot(1,1,1)
    figE = plt.figure()
    axE = figE.add_subplot(1,1,1)
    figI = plt.figure()
    axI = figI.add_subplot(1,1,1)
    figR = plt.figure()
    axR = figR.add_subplot(1,1,1)
    T_plt, SEIRSDataDeterministic = task3.SEIRS_model(1)
    for i in range(lib.T):
        lib.loading(i)
        T_plt, SEIRSData = task6.SEIRS_model()
        alpha = 0.1*(i+1)/lib.T
        axS.fill_between(T_plt, SEIRSDataDeterministic['S'], SEIRSData['S'], color='red', alpha=alpha)
        axE.fill_between(T_plt, SEIRSDataDeterministic['E'], SEIRSData['E'], color='red', alpha=alpha)
        axI.fill_between(T_plt, SEIRSDataDeterministic['I'], SEIRSData['I'], color='red', alpha=alpha)
        axR.fill_between(T_plt, SEIRSDataDeterministic['R'], SEIRSData['R'], color='red', alpha=alpha)

    axS.plot(T_plt, SEIRSDataDeterministic['S'], '--', color='black')
    lib.apply_chart_properties_ax(axS, f"Fan chart $S_t$ dla N={lib.N}, $I_0$=1, $\\beta$={lib.beta}, $\\gamma$={lib.gamma}, $\\eta$={lib.eta}")
    lib.save_file_fig("task8Results/SEIRS_model_St.png", figS)

    axE.plot(T_plt, SEIRSDataDeterministic['E'], '--', color='black')
    lib.apply_chart_properties_ax(axS, f"Fan chart $E_t$ dla N={lib.N}, $I_0$=1, $\\beta$={lib.beta}, $\\gamma$={lib.gamma}, $\\eta$={lib.eta}")
    lib.save_file_fig("task8Results/SEIRS_model_Et.png", figE)

    axI.plot(T_plt, SEIRSDataDeterministic['I'], '--', color='black')
    lib.apply_chart_properties_ax(axI, f"Fan chart $I_t$ dla N={lib.N}, $I_0$=1, $\\beta$={lib.beta}, $\\gamma$={lib.gamma}, $\\eta$={lib.eta}")
    lib.save_file_fig("task8Results/SEIRS_model_It.png", figI)

    axR.plot(T_plt, SEIRSDataDeterministic['R'], '--', color='black')
    lib.apply_chart_properties_ax(axR, f"Fan chart $I_t$ dla N={lib.N}, $I_0$=1, $\\beta$={lib.beta}, $\\gamma$={lib.gamma}, $\\eta$={lib.eta}")
    lib.save_file_fig("task8Results/SEIRS_model_Rt.png", figR)

if __name__ == "__main__":
    fan_chart_SEIR()
    fan_chart_SEIRS()
