from math import *
 
import random
from datetime import datetime
 
import hashlib
 
import binascii
 
 
# Hashing Algo
#_______________________________________________________
def hash1(msg):
    hash_object = hashlib.sha256(msg.encode('utf-8'))
    hex_dig = hash_object.hexdigest()
    return hex_dig
#_______________________________________________________
 
 
 
# Generate Hash Cash
#_______________________________________________________
 
def genCash(include,numOfZeros):    
    loop = True
    counter = 0
    random.seed(datetime.now())
    x = str(random.randint(1, 1180591620717411303424))
    while(loop):
        counter = counter + 1
 
        solution = True
 
        testHash = hash1(include + ":" + x + ":" + str(counter))
 
        for i in range(0,numOfZeros):
            if ( testHash[i] != "0" ):
                solution = False
                break
 
        if (solution == True):
            print('x is: %s' %testHash)
            print(len(testHash))
            loop = False

    return counter
 
    # print("")
    # print("Value (ProofOfWork):")
    # print("")
    # print(include + ":" + x + ":" + str(counter))
    # print("")
    # print("")
    # print("Hash (Verification):")
    # print("")
    # print(hash1(include + ":" + x + ":" + str(counter)))
    # print("")
    # print("")
    # print("It took me " + "{:,}".format(counter) + " hashes to figure this out")

    #genCash("BizVlogsCash", 3)


if __name__ == '__main__':
    import matplotlib.pyplot as plt
    leading_zeros = 7
    counts = []
    for i in range(leading_zeros):
        counts.append(genCash("BizVlogsCash", i))

    print(counts)

    plt.plot([i for i in range(leading_zeros)], counts)
    plt.show()