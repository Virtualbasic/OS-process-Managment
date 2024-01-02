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
    pagehit = 0
    refsCount = 0
    queue = [-1] * queue_size
    while refsCount <  memoryConfig["AmountOFrefs"]:
        if refslist[refsCount] in queue:
            pagehit+=1
            print("No fault occurred!")
            pass
        elif refslist not in queue and len(queue) < queue_size:
            faults+=1
            queue.insert(0,refslist[refsCount])
            #queue.append(refslist[refsCount])
            print("fault")
        else:
            queue[-1] = refslist[refsCount]
            newest = queue.pop(-1)
            queue.insert(0,newest)
            #queue[queue_size-1] = refslist[refsCount]
            faults +=1
            print("fault")
        refsCount += 1
    return [faults,pagehit]
        #print(refslist[refsCount])
        #print(queue)
        #if refslist[refsCount] in queue:
        #    print("No fault occurred!")
        #    pass
        #elif refslist[refsCount] not in queue:
        #    if len(queue) < queue_size:
        #        queue.append(refslist[refsCount])
        #        faults += 1
        #        print("A fault occurred!")
        #else:
        #    queue[queueCount % queue_size] = refslist[refsCount]
        #    queueCount += 1
        #    faults += 1
        #    print("A fault occurred!")
        #refsCount += 1
    #return faults
