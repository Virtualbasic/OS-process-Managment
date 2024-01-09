import random
def refsgen(AmountofRefs , AmountOFseries , AmountOFpages ,Randomizer):

    random.seed(9284)

    with open("refs.txt" , "w") as refs:
        for ref in range(0,AmountOFseries):
            for i in range(0,AmountofRefs):
                refs.write(str(random.randint(Randomizer,AmountOFpages)) + "\n")
        refs.close()