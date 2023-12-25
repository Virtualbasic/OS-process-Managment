memoryConfig={}
with open("configMem.txt" , "r") as memconf:
    for i in memconf:
        slasher = i.index(":")
        if i[:slasher] != "AmountOFframes":
            memoryConfig[i[:slasher]] = int(i[slasher+1:-1])
        if i[:slasher] == "AmountOFframes":
            memoryConfig[i[:slasher]] = [int(x) for x in i[slasher+1:-1].split(",")]


def FIFO(refslist, FrameVal):
    queue_size = memoryConfig["AmountOFframes"][FrameVal]
    print(refslist)
    faults = 0
    queueCount = 0
    refsCount = 0
    queue = []
    while refsCount <  memoryConfig["AmountOFrefs"]:
        print(refslist[refsCount])
        print(queue)
        if refslist[refsCount] in queue:
            print("No fault occurred!")
            pass
        elif refslist[refsCount] not in queue:
            if len(queue) < queue_size:
                queue.append(refslist[refsCount])
                faults += 1
                print("A fault occurred!")
        else:
            queue[queueCount % queue_size] = refslist[refsCount]
            queueCount += 1
            faults += 1
            print("A fault occurred!")
        refsCount += 1
    return faults
