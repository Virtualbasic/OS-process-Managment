from LRU import LRU
from ReadRef import ReadRefs
from refsGenerator import AmountOFframes

refsD = []
tpf_fifo = [[] for i in range(0, len(AmountOFframes))]
print(tpf_fifo)

if __name__ == "__main__":
    path = "refs.txt"
    RefsTable = ReadRefs(path)
    # print(FIFO(RefsTable, 2))
    result = []
    for i in range(0, len(AmountOFframes)):
        print(LRU(RefsTable, i))
        result.append([AmountOFframes[i], LRU(RefsTable, i)])
    print(result)
