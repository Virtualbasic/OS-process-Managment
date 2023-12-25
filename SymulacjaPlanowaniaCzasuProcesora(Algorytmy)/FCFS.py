def FCFS(proceslist, TmTexec):
    TimerForProcesses = 0
    IfEnded = 2
    AwaitTime = 1
    queue = []
    while not all(item[2] for item in proceslist) or  queue:
        for proc in proceslist:
            if proc[AwaitTime] == TimerForProcesses:
                print("Process added to CPU queue....")
                queue.append(proc)
                proc[IfEnded] = True
        if queue:
            if queue[0][0] == 0:
                print("process ended , time to execute:" + str(queue[0][3]))
                TmTexec.append(queue[0][3])
                del queue[0]
            elif queue[0]:
                print("Exec Process")
                queue[0][0]-=1
        for  sub in queue[1:]:
            sub[3] +=1
        TimerForProcesses+=1
    print(TimerForProcesses)
    print(TmTexec)