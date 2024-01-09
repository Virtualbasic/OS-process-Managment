
import random

def ProcGeneration(AmountOfRepeat,AmountOfprocess,MaxExecTime ,MaxAwaitTime,randomizationExecTime ,  randomizationAwaitTime ):
    random.seed(11111)
    process = open("process.txt" , "w")

    for i in range(0,AmountOfRepeat):
        for j in range(0,AmountOfprocess):
            proc = str(random.randint(randomizationExecTime,MaxExecTime)) + " | " + str(random.randint(randomizationAwaitTime ,MaxAwaitTime)) +"\n"
            process.write(proc)
    process.close()

