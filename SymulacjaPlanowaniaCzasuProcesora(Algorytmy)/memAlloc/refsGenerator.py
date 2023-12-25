import random
def refsgen(AmountofRefs , AmountOFseries , AmountOFpages ,Randomizer):



#AmountOFseries = 10
#AmountOFrefs = 100
#Amountofpages = 20
#AmountOFframes = [4, 8, 12]
    random.seed(9729)

    with open("refs.txt" , "w") as refs:
        for ref in range(0,AmountOFseries):
            for i in range(0,AmountofRefs):
                refs.write(str(random.randint(Randomizer,AmountOFpages)) + "\n")
        refs.close()