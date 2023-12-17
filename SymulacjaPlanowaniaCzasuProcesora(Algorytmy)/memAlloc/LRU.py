from refsGenerator import AmountOFframes, AmountOFrefs

def LRU(refs_list, frameVal):
    queue_size = AmountOFframes[frameVal]
    faults = 0
    refs_c = 0
    queue = []
    lru_queue = []

    while refs_c < AmountOFrefs:
        if refs_list[refs_c] in queue:
            print("No fault oc")
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
                # Remove  latest used mem page from lru queue
                del lru_queue[0]
                lru_queue.append(refs_list[refs_c])
                faults += 1
                print("faults found")
        refs_c += 1
    return faults
