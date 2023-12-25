#libs
import random


def ProcGeneration(AmountOfRepeat,AmountOfprocess,MaxExecTime ,MaxAwaitTime,randomizationExecTime ,  randomizationAwaitTime ):

# configuration
    #AmountOfRepeat = 1
    #AmountOfprocess = 100
    #MaxExecTime = 30
    #MaxAwaitTime = 220
    random.seed(11111)
#Generation
    process = open("process.txt" , "w")

    for i in range(0,AmountOfRepeat):
        for j in range(0,AmountOfprocess):
            proc = str(random.randint(randomizationExecTime,MaxExecTime)) + " | " + str(random.randint(randomizationAwaitTime ,MaxAwaitTime)) +"\n"

        #proc =  str(random.randint(0, MaxAwaitTime)) + "," +  str(random.randint(0, MaxExecTime)) + "\n"
            process.write(proc)
    process.close()

