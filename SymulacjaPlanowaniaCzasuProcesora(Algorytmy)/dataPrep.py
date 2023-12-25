

def data_preparation(path):
    with open(path, "r") as proces:
        processList = []
        temp = [i[:-1] for i in proces]
        for i in range(0, len(temp)):
            for j in temp[i]:
                if j == "|":
                    MaxAwaitTime = temp[i].index("|")
                    #processList.append([ int(temp[i][MaxAwaitTime + 1:]), int(temp[i][:MaxAwaitTime]), False, 0])
                    processList.append([int(temp[i][:MaxAwaitTime]), int(temp[i][MaxAwaitTime + 1:]), False,0])
                    break
    processList.sort(key=lambda x:x[1])

    return processList