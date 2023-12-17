def ReadRefs(data_refs):
    Refss = []
    with open(data_refs,'r') as odczyt:
        for i in odczyt:
            Refss.append(int(i[:-1]))
        odczyt.close()
    return Refss