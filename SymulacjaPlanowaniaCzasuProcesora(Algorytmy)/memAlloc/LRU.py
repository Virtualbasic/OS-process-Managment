memoryConfig={}
with open("configMem.txt" , "r") as memconf:
    for i in memconf:
        slasher = i.index(":")
        if i[:slasher] != "AmountOFframes":
            memoryConfig[i[:slasher]] = int(i[slasher + 1:-1])
        if i[:slasher] == "AmountOFframes":
            memoryConfig[i[:slasher]] = [int(x) for x in i[slasher+1:-1].split(",")]


def LRU(refs_list, FrameVal):
    queue_size = memoryConfig["AmountOFframes"][FrameVal]
    faults = 0
    refs_c = 0
    queue = []
    pagehit = 0
    lru_queue = []

    while refs_c < memoryConfig["AmountOFrefs"] * memoryConfig["AmountOFseries"]:
        if refs_list[refs_c] in queue:
            print("No fault oc")
            pagehit +=1
            pass
            if refs_list[refs_c] in lru_queue:
                del lru_queue[lru_queue.index(refs_list[refs_c])]
            lru_queue.append(refs_list[refs_c])
            pass
        elif refs_list[refs_c] not in queue:
            if len(queue) < queue_size:
                queue.append(refs_list[refs_c])
                lru_queue.append(refs_list[refs_c])
                faults += 1
                print("faults found")
            else:
                queue[queue.index(lru_queue[0])] = refs_list[refs_c]
                del lru_queue[0]
                lru_queue.append(refs_list[refs_c])
                faults += 1
                print("faults found")
        refs_c += 1
    return [faults,pagehit]
