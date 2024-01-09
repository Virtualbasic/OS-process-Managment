import copy
import json
from matplotlib import pyplot
import math
from dataPrep import data_preparation
from SJF import SJF
from ProcessGeneration import  ProcGeneration
from FCFS import FCFS
import matplotlib.pyplot as plt
import numpy as np
from copy import deepcopy
#config place
ResultFcFs = []
ResultSJF = []
path = "process.txt"

configForProcessAlgorithm = {}
with open("config.txt", "r") as config:

    for i in config:
        slasher = i.index(":")
        rep = i[::-1]
        if i[0] != "\n":
            configForProcessAlgorithm[i[:slasher]] = int(i[slasher + 1])

        configForProcessAlgorithm[i[:slasher]] = int(i[slasher+1:-1])
config.close()


def SeTplot(maxexctimeFCFS, maxecextimeSJF,howmanyprocesses,ranodmizer, MaxAwaittime):
    plt.title(f"Await time from {ranodmizer} to {MaxAwaittime}")

    maxexctimeFCFSs= maxexctimeFCFS[-1]

    maxecextimeSJFf = maxecextimeSJF[-1]


    bar_width = 0.35

    bar_shift = [x + bar_width for x in maxexctimeFCFS]
    handler = 1
    print(maxexctimeFCFS)

    plt.bar(handler, maxexctimeFCFSs, color='green', width=bar_width, label="FCFS")
    plt.bar((handler+1), maxecextimeSJFf, color='blue', width=bar_width, label="SJF")

    plt.xlabel("frames")
    plt.ylabel(f"Avarge executive time")
    #plt.xticks(maxecextimeSJF)
    #plt.xticks()
    plt.legend()
    plt.show()
arrivalTimes = []
def simulationPrep(config):
    ProcGeneration(config["AmountOfRepeat"], config["AmountOfprocess"],config["MaxExecTime"],config["MaxAwaitTime"] , config["RandomizationEXC"],config["RandomizationAWAIT"])
    ProcessList = data_preparation(path)

    for i in ProcessList:
        arrivalTimes.append(i[1])
    return ProcessList
def standard_deviation(avg,table):

    wariation = 0
    for i in table:
        wariation+=(float(i-avg)**2)/avg
    return math.sqrt(wariation)
def standard_deviation_plot(ARtime , execTimev1 , execTimev2, numoftests):
    deviation1 = np.std(execTimev1, axis=0)
    deviation2 = np.std(execTimev2, axis=0)
    plt.errorbar(execTimev1,ARtime, yerr=deviation1, fmt="o-" , label="SJF")
    plt.errorbar(execTimev2,ARtime , yerr=deviation2, color="red", fmt="o", label="FCFS")
    plt.title("standard deviation")
    plt.legend()
    plt.show()
if __name__ == "__main__":
    ProcesListStorage =simulationPrep(configForProcessAlgorithm)
    FCFSprocList = copy.deepcopy(ProcesListStorage)#[sub for sub in ProcesListStorage]
    SJFprocList =  [sub for sub in ProcesListStorage]
    AwaitTime = 0
    for i in  FCFSprocList:
        AwaitTime+=i[1]

    print(FCFS(FCFSprocList, ResultFcFs))
    print(SJF(SJFprocList, ResultSJF))
    print(len(ResultSJF))
    print(len(ResultFcFs))
    #FCFS section
    aTimetoExec_FCFS = 0
    for time in ResultFcFs:
        aTimetoExec_FCFS+=time
    with open("statsFCFS.json", "r") as fileFCFS:
        dataFCFS = json.load(fileFCFS)
    dataFCFS ["Avarage_Exec_Time"].append(aTimetoExec_FCFS/len(ResultFcFs))
    dataFCFS ["Avarage_Await_Time"].append(AwaitTime/len(ResultFcFs))
    dataFCFS ["Tables_with_Exectime"].append(ResultFcFs)
    # deviation
    with open("devationFCFS_SJF.json", "r") as dev:
        devationPROC = json.load(dev)
    devationPROC["devationAlg1"].append(standard_deviation(dataFCFS ["Avarage_Exec_Time"][0], dataFCFS["Tables_with_Exectime"][0] ))
    devationPROC["numoftry"] +=1
    with open("statsFCFS.json", "w") as fileFCFS:
        json.dump(dataFCFS ,fileFCFS, indent=2)
    with open("devationFCFS_SJF.json", "w") as dev:
        json.dump(devationPROC,dev,indent=2)

    #SJF section
    aTimetoExec_SJF = 0
    for time in ResultSJF:
        aTimetoExec_SJF += time
    with open("statsSJF.json", "r") as fileSJF:
        dataSJF = json.load(fileSJF)
    dataSJF ["Avarage_Exec_Time"].append(aTimetoExec_SJF/len(ResultSJF))
    dataSJF ["Avarage_Await_Time"].append(AwaitTime/len(ResultSJF))
    dataSJF ["Tables_with_Exectime"].append(ResultSJF)
    # deviation
    with open("devationFCFS_SJF.json", "r") as dev:
        devationPROC = json.load(dev)
    devationPROC["devationAlg2"].append(standard_deviation(dataSJF ["Avarage_Exec_Time"][0], dataSJF["Tables_with_Exectime"][0] ))
    with open("statsSJF.json", "w") as fileSJF:
        json.dump(dataSJF, fileSJF, indent=2)
    with open("devationFCFS_SJF.json", "w") as dev:
        json.dump(devationPROC, dev, indent=2)
    print(SJFprocList)
    print(FCFSprocList )
    print(aTimetoExec_SJF / len(ResultSJF))
    #setplot
    with open("statsSJF.json", "r") as fileSJF:
        dataSJF = json.load(fileSJF)
    with open("statsFCFS.json", "r") as fileFCFS:
        dataFCFS = json.load(fileFCFS)
    print(arrivalTimes)
    SeTplot(dataFCFS["Avarage_Exec_Time"], dataSJF["Avarage_Exec_Time"], (configForProcessAlgorithm["AmountOfprocess"] *configForProcessAlgorithm["AmountOfRepeat"]), configForProcessAlgorithm["RandomizationAWAIT"],configForProcessAlgorithm["MaxAwaitTime"] )
    #devation plot
    with open("statsSJF.json", "r") as fileSJFdev:
        dataSJFdev = json.load(fileSJFdev)
    with open("statsFCFS.json", "r") as fileFCFSdev:
        dataFCFSdev = json.load(fileFCFSdev)
    #with open("devationFCFS_SJF.json", "r") as devplot:
    #    devationPLOT = json.load(devplot)
    print(len(arrivalTimes))
    standard_deviation_plot(arrivalTimes, dataSJFdev["Tables_with_Exectime"][-1], dataFCFSdev["Tables_with_Exectime"][-1], 0)
