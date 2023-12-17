from  refsGenerator import AmountOFframes, AmountOFrefs


def FIFO(refslist, FrameVal):
    queue_size = AmountOFframes[FrameVal]
    print(refslist)
    faults = 0
    queueCount = 0
    refsCount = 0
    queue = []
    while refsCount < AmountOFrefs:
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
