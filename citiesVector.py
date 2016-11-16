import random
import math
#if 8 repeated then we try 8+1, then 8+2...

#generates an initial vector with random values
def generateInitialSolution(size,path=0):
    size=int(size)-1
    citiesVector=[0]*size
    index=0
    #If read is 0 then we generate the random numbers
    if path==0:
        while index<size:
            actualValue=1 + math.floor(random.random() * size)
            if actualValue not in citiesVector:
                citiesVector[index]=actualValue
                index+=1
            else:
                while actualValue in citiesVector:
                    actualValue=int(math.fmod((actualValue+1),size))
                citiesVector[index] = actualValue
                index += 1
    #if path has a value, then we read the random numbers from the specified file
    else:
        print("else")

    return citiesVector


def calculateDistance(distanceMatrix,citiesVector):
    print("Ditance matrix:")
    for line in distanceMatrix:
        print(line)
    print("\nCities vector: ",citiesVector)

