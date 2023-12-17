import random

AmountOFseries = 10
AmountOFrefs = 100
Amountofpages = 15
AmountOFframes = [4, 8, 12]
random.seed(9729)

with open("refs.txt" , "w") as refs:
    for ref in range(AmountOFseries):
        for i in range(AmountOFrefs):
            refs.write(str(random.randint(0,Amountofpages)) + "\n")
    refs.close()