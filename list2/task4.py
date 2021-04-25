import list2_lib as lib
import task1 as task1
import task2 as task2
import task3 as task3

def SI_comparison_of_euler_and_dopri(dt, logScale, savePath):
    T_plt, dataSI = task1.SI_model(dt)
    _, dataSIDopri = task2.SI_model_dopri(dt)
    dataSI.update(dataSIDopri)
    lib.plot_model(T_plt,
        dataSI,
        f"Porównanie modelu SI dla N={lib.N}, $I_0$=1, $\\beta$={lib.beta}, dt={dt}",
        logScale,
        savePath)

def SIS_comparison_of_euler_and_dopri(dt, logScale, savePath):
    T_plt, dataSIS = task1.SIS_model(dt)
    _, dataSISDopri = task2.SIS_model_dopri(dt)
    dataSIS.update(dataSISDopri)
    lib.plot_model(T_plt,
        dataSIS,
        f"Porównanie modelu SIS dla N={lib.N}, $I_0$=1, $\\beta$={lib.beta}, $\\gamma$={lib.gamma}, dt={dt}",
        logScale,
        savePath)

def SIRS_comparison_of_euler_and_dopri(dt, logScale, savePath):
    T_plt, dataSIRS = task1.SIRS_model(dt)
    _, dataSIRSDopri = task2.SIRS_model_dopri(dt)
    dataSIRS.update(dataSIRSDopri)
    lib.plot_model(T_plt,
        dataSIRS,
        f"Porównanie modelu SIRS dla N={lib.N}, $I_0$=1, $\\beta$={lib.beta}, $\\gamma$={lib.gamma}, $\\eta$={lib.eta}, dt={dt}",
        logScale,
        savePath)

def SEIR_comparison_of_euler_and_dopri(dt, logScale, savePath):
    T_plt, dataSEIR = task3.SEIR_model(dt)
    _, dataSEIRDopri = task3.SEIR_dopri_model(dt)
    dataSEIR.update(dataSEIRDopri)
    lib.plot_model(T_plt,
        dataSEIR,
        f"Porównanie modelu SEIR dla N={lib.N}, $I_0$=1, $\\beta$={lib.beta}, $\\gamma$={lib.gamma}, $\\eta$={lib.eta}, dt={dt}",
        logScale,
        savePath)

def SEIRS_comparison_of_euler_and_dopri(dt, logScale, savePath):
    T_plt, dataSEIRS = task3.SEIRS_model(dt)
    _, dataSEIRSDopri = task3.SEIRS_dopri_model(dt)
    dataSEIRS.update(dataSEIRSDopri)
    lib.plot_model(T_plt,
        dataSEIRS,
        f"Porównanie modelu SEIRS dla N={lib.N}, $I_0$=1, $\\beta$={lib.beta}, $\\gamma$={lib.gamma}, $\\eta$={lib.eta}, dt={dt}",
        logScale,
        savePath)

if __name__ == "__main__":
    dts = [1, 0.1, 0.01, 0.001]
    for dt in dts:
        SI_comparison_of_euler_and_dopri(dt, False, f"task4Results/SI_model{int(dt*1000)}.png");
        SIS_comparison_of_euler_and_dopri(dt, False, f"task4Results/SIS_model{int(dt*1000)}.png");
        SIRS_comparison_of_euler_and_dopri(dt, False, f"task4Results/SIRS_model{int(dt*1000)}.png");
        SEIR_comparison_of_euler_and_dopri(dt, False, f"task4Results/SEIR_model{int(dt*1000)}.png");
        SEIRS_comparison_of_euler_and_dopri(dt, False, f"task4Results/SEIRS_model{int(dt*1000)}.png");

        SI_comparison_of_euler_and_dopri(dt, True, f"task4LogResults/SI_model{int(dt*1000)}.png");
        SIS_comparison_of_euler_and_dopri(dt, True, f"task4LogResults/SIS_model{int(dt*1000)}.png");
        SIRS_comparison_of_euler_and_dopri(dt, True, f"task4LogResults/SIRS_model{int(dt*1000)}.png");
        SEIR_comparison_of_euler_and_dopri(dt, True, f"task4LogResults/SEIR_model{int(dt*1000)}.png");
        SEIRS_comparison_of_euler_and_dopri(dt, True, f"task4LogResults/SEIRS_model{int(dt*1000)}.png");
