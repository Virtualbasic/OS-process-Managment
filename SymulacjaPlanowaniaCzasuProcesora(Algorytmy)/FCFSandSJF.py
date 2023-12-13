import  numpy
from ProcessGeneration import AmountOfprocess , AmountOfRepeat
import matplotlib.pyplot as plot
import time
from dataPrep import data_preparation
from FCFS import FCFS
from SJF import SJF
ResultFcFs = []

path = "process.txt"


if __name__ == "__main__":
    ProcessList = data_preparation(path)
    print(FCFS(ProcessList, ResultFcFs))
    print(ProcessList)