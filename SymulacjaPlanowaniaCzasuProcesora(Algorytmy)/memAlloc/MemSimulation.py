from LRU import LRU
from FIFO import FIFO
from ReadRef import ReadRefs
from refsGenerator import refsgen
import json
import copy
import numpy as np
import  matplotlib.pyplot as plt
refsD = []
#tpf_fifo = [[] for i in range(0, len(AmountOFframes))]
#print(tpf_fifo)

memoryConfig={}
with open("configMem.txt" , "r") as memconf:
    for i in memconf:
        slasher = i.index(":")
        if i[:slasher] != "AmountOFframes":
            memoryConfig[i[:slasher]] = int(i[slasher+1:-1])
        if i[:slasher] == "AmountOFframes":
            memoryConfig[i[:slasher]] = [int(x) for x in i[slasher+1:-1].split(",")]


def SeTplot(faults1, algorithm1, amountRefs1, frames1, faults2, algorithm2, amountRefs2, frames2):
    plt.title("Comparison of Algorithms")


    Frames1 = [i for i in frames1[0]]
    Faults1 = [j for j in faults1[0]]


    Frames2 = [i for i in frames2[0]]
    Faults2 = [j for j in faults2[0]]

    bar_width = 0.35


    bar_shift = [x + bar_width for x in Frames1]


    plt.bar(Frames1, Faults1, color='green', width=bar_width, label=algorithm1)
    plt.bar(bar_shift, Faults2, color='blue', width=bar_width, label=algorithm2)

    plt.xlabel("frames")
    plt.ylabel(f"faults for specific amount of refs")
    plt.xticks(Frames1)
    plt.legend()
    plt.show()
def symulation(config):
    path = "refs.txt"
    refsgen(config["AmountOFrefs"],config["AmountOFseries"],config["Amountofpages"],config["Randomizer"])
    RefsTable = ReadRefs(path)
    return RefsTable
if __name__ == "__main__":
    RefStorage = symulation(memoryConfig)
    FIFOStorage =[i for i  in RefStorage]
    LRUStorage = copy.deepcopy(RefStorage)
    #RefsTable = ReadRefs(path)
    # print(FIFO(RefsTable, 2))
    resultLRU = []
    resultFIFO = []
    for val in range(0, len(memoryConfig["AmountOFframes"])):
        for i in range(0 , memoryConfig["AmountOFrefs"]):
            #print(LRU(LRUStorage, val))
            listFIFO =FIFO(FIFOStorage , val)
            listLRU = LRU(LRUStorage, val)
            print(listFIFO)
            resultFIFO.append([memoryConfig["AmountOFframes"][val], listFIFO[0],listFIFO[1]])
            resultLRU.append([memoryConfig["AmountOFframes"][val],listLRU[0], listLRU[1] ])
    print(resultLRU)

    #LRU section
    LRUFaulst =[]
    LRUFrames =[]
    LRUPageHit = []
    with open("LRU.json" , "r") as LRUfile:
        LRUdata = json.load(LRUfile)
    for i in range(len(resultLRU )):
        LRUFaulst.append(resultLRU[i][1])
    LRUdata["faulst"].append(LRUFaulst)
    for j in range(len(resultLRU)):
        LRUFrames.append(resultLRU[j][0])
    for g in range(len(resultLRU)):
        LRUPageHit.append(resultLRU[g][2])
    LRUdata["frames"].append(LRUFrames)
    LRUdata["refsAmount"].append(memoryConfig["AmountOFrefs"])
    LRUdata["pagehit"].append(LRUPageHit)
    with open("LRU.json", "w") as LRUfile:
        json.dump(LRUdata ,  LRUfile , indent=2)
    #FIFO section
    FIFOFaulst = []
    FIFOFrames = []
    FIFOPageHit = []
    with open("FIFO.json", "r") as FIFOfile:
        FIFOdata = json.load(FIFOfile)
    for i in range(len(resultFIFO)):
        FIFOFaulst.append(resultFIFO[i][1])
    FIFOdata["faulst"].append(FIFOFaulst)
    for j in range(len(resultFIFO)):
        FIFOFrames.append(resultFIFO[j][0])
    for g in range(len(resultFIFO)):
        FIFOPageHit.append(resultFIFO[g][2])
    FIFOdata["frames"].append(FIFOFrames)
    FIFOdata["refsAmount"].append(memoryConfig["AmountOFrefs"])
    FIFOdata["pagehit"].append(FIFOPageHit)
    with open("FIFO.json", "w") as FIFOfile:
        json.dump(FIFOdata, FIFOfile, indent=2)
    #LRU GRAF
    with open("LRU.json" , "r") as LRUfile:
        LRUdata = json.load(LRUfile)
    with open("FIFO.json" , "r") as FIFOfile:
        FIFOdata = json.load(FIFOfile)
    SeTplot(LRUdata["faulst"], LRUdata["algorithm"], LRUdata["refsAmount"], LRUdata["frames"],
            FIFOdata["faulst"], FIFOdata["algorithm"], FIFOdata["refsAmount"], FIFOdata["frames"])

