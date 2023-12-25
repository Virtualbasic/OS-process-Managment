import copy
import json
from matplotlib import pyplot
from dataPrep import data_preparation
from SJF import SJF
from ProcessGeneration import  ProcGeneration
from FCFS import FCFS
import matplotlib.pyplot as plt
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

    maxexctimeFCFS= [i for i in ResultFcFs]

    maxecextimeSJF = [i for i in ResultSJF]


    bar_width = 0.35

    bar_shift = [x + bar_width for x in maxexctimeFCFS]

    plt.bar(howmanyprocesses, maxexctimeFCFS, color='green', width=bar_width, label="FCFS")
    plt.bar(bar_shift, maxecextimeSJF, color='blue', width=bar_width, label="SJF")

    plt.xlabel("frames")
    plt.ylabel(f"faults for specific amount of refs")
    plt.xticks(maxecextimeSJF)
    plt.legend()
    plt.show()

def simulationPrep(config):
    ProcGeneration(config["AmountOfRepeat"], config["AmountOfprocess"],config["MaxExecTime"],config["MaxAwaitTime"] , config["RandomizationEXC"],config["RandomizationAWAIT"])
    ProcessList = data_preparation(path)

    return ProcessList


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
    with open("statsFCFS.json", "w") as fileFCFS:
        json.dump(dataFCFS ,fileFCFS, indent=2)


    #SJF section
    aTimetoExec_SJF = 0
    for time in ResultSJF:
        aTimetoExec_SJF += time
    with open("statsSJF.json", "r") as fileSJF:
        dataSJF = json.load(fileSJF)
    dataSJF ["Avarage_Exec_Time"].append(aTimetoExec_SJF/len(ResultSJF))
    dataSJF ["Avarage_Await_Time"].append(AwaitTime/len(ResultSJF))
    dataSJF ["Tables_with_Exectime"].append(ResultSJF)
    with open("statsSJF.json", "w") as fileSJF:
        json.dump(dataSJF, fileSJF, indent=2)
    print(SJFprocList)
    print(FCFSprocList )
    print(aTimetoExec_SJF / len(ResultSJF))
    #setplot
    with open("statsSJF.json", "r") as fileSJF:
        dataSJF = json.load(fileSJF)
    with open("statsFCFS.json", "r") as fileFCFS:
        dataFCFS = json.load(fileFCFS)
    SeTplot(dataFCFS["Avarage_Exec_Time"], dataSJF["Avarage_Exec_Time"], (configForProcessAlgorithm["AmountOfprocess"] *configForProcessAlgorithm["AmountOfRepeat"]), configForProcessAlgorithm["RandomizationAWAIT"],configForProcessAlgorithm["MaxAwaitTime"] )
