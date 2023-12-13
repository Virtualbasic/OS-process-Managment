#libs
import random

# configuration
AmountOfRepeat = 1
AmountOfprocess = 5
MaxExecTime = 30
MaxAwaitTime = 220
random.seed(11111)
#Generation
process = open("process.txt" , "w")

for i in range(0,AmountOfRepeat):
    for j in range(0,AmountOfprocess):
        proc = str(random.randint(0,MaxExecTime)) + " | " + str(random.randint(0,MaxAwaitTime)) +"\n"
        #proc =  str(random.randint(0, MaxAwaitTime)) + "," +  str(random.randint(0, MaxExecTime)) + "\n"
        process.write(proc)
process.close()

