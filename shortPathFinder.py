import random
import math
import fileManager


class TravellingSalesman:
    #Properties of the class
    #Matrix
    distanceMatrix=[]
    actualSolution=[]
    solution=[]
    minimalDistance=0
    tabuList=[]
    neighbors=[]
    bestNeighbor=[]
    #Integers
    iterations=0
    solIteration=0
    bestIndex0=0
    bestIndex1=0
    iterationsWithoutImprovement=0
    maxIterationsWithoutImprovement=100
    improvement=0
    restart=0

    numberOfCities=0
    solutionNumber = -1
    neighborNumber=0
    pathToRandomFile=0
    actualDistance=0
    newDistance=0

    maxIterationCount=0
    maxIterations=10000
    randomFile = 0
    tendencyParameter=100

    #Intial function
    def __init__(self,pathToDistances,pathToRandomFile=0):
        # Extracts the number of cities from the file name
        self.numberOfCities = int(pathToDistances.split('_')[1].split('.')[0])
        # First we open the desired file and obtain a distance matrix
        self.distanceMatrix = fileManager.openFile(pathToDistances, self.numberOfCities)
        # #The next step for this project is to obtain a neighbor matrix that we're going to use not to generate
        # #two times the same neighbor
        self.tendencyParameter=self.numberOfCities
        self.numberOfCities-=1
        if(pathToRandomFile)!=0:
            self.pathToRandomFile=pathToRandomFile
            self.randomFile=open(pathToRandomFile,"r")
        #We determine the maximum of swiches that we can do
        self.swapArrayDimension=sum(range(0,self.numberOfCities, 1))

    #Print different elements
    def printDistanceMatrix(self):
        print("Distance matrix: ")
        for line in self.distanceMatrix:
            print(line)

    def printActualSolution(self):
        print("\tRECORRIDO:", *self.actualSolution,"")

    def printSwapMatrix(self):
        print("Swaps done matrix: ")
        i=0
        print("  ",'  '.join(str(x) for x in range(0, self.numberOfCities+1)))
        for line in self.swapMatrix:
            print(i,line)
            i+=1

    #Rest of the functionality
    #if 8 repeated then we try 8+1, then 8+2...

    def reinitializeSwapMatrix(self):
        self.swapMatrix = [[0] * (i + 1) for i in range(self.numberOfCities)]
        for i in range(0, self.numberOfCities):
            self.swapMatrix[i][i] = 1

    def calculateRandom(self):
        if self.pathToRandomFile==0:
            return random.random()
        else:
            value = float(self.randomFile.readline())
            return value

    def calculateDistance(self,citiesVector):
        i = 0
        index01 = 0
        index02 = 0
        self.newDistance = self.distanceMatrix[citiesVector[0] - 1][0]
        while i < (self.numberOfCities - 1):
            index01 = citiesVector[i]
            index02 = citiesVector[i + 1]
            if index01 > index02:
                self.newDistance += int(self.distanceMatrix[index01 - 1][index02])
            else:
                self.newDistance += int(self.distanceMatrix[index02 - 1][index01])

            i += 1
        self.newDistance += self.distanceMatrix[citiesVector[self.numberOfCities - 1]-1][0]
        if self.actualDistance == 0:
            self.actualDistance=self.newDistance
        return self.newDistance

    #generates an initial vector with random values
    def generateInitialSolution(self):
        self.actualSolution=[0]*self.numberOfCities
        index=0
        #If read is 0 then we generate the random numbers
        while index < self.numberOfCities:
            actualValue=1 + math.floor(self.calculateRandom() * self.numberOfCities)
            while actualValue in self.actualSolution:
                actualValue+=1
                actualValue=math.fmod(actualValue,self.numberOfCities+1)
                actualValue=int(actualValue)
            self.actualSolution[index] = actualValue
            index+=1
        #if path has a value, then we read the random numbers from the specified file
        self.solutionNumber+=1
        self.calculateDistance(self.actualSolution)
        self.minimalDistance=self.actualDistance
    #
    def swap(self,vector,index0,index1):
        returnVector = list(vector)
        returnVector[index0] = vector[index1]
        returnVector[index1] = vector[index0]
        self.maxIterationCount+=1
        return returnVector
    # Calculates all neighbors and checks who is teh best solution
    def calculateNeighbors(self):
        line=0
        tabuCount=0
        while line < self.maxIterations:
            index0=0
            index1=0
            line+=1
            jump=0
            first=0
            #calculates 1 iteration

            while index0<=99 and index1<98:
                if jump==index1:
                    index0+=1
                    index1=0
                    jump+=1
                # here goes the actual content
                vector=self.swap(self.actualSolution,index0,index1)
                if [index0, index1] not in self.tabuList:
                    if ((self.calculateDistance(vector) < self.actualDistance) or first==0):
                        first=1
                        self.actualDistance=self.newDistance
                        self.bestNeighbor=vector
                        self.bestIndex0=index0
                        self.bestIndex1=index1
                index1+=1

            self.iterations+=1
            self.actualSolution=self.bestNeighbor

            if [self.bestIndex0,self.bestIndex1] not in self.tabuList:
                self.tabuList.append([self.bestIndex0, self.bestIndex1])
            tabuCount += 1

            if self.actualDistance < self.minimalDistance:
                self.solution=self.bestNeighbor
                self.solIteration=self.iterations
                self.minimalDistance=self.actualDistance
                self.iterationsWithoutImprovement=0
            else:
                self.iterationsWithoutImprovement+=1

            print("ITERACION:", self.iterations)
            print("\tINTERCAMBIO: (", self.bestIndex0, ", ", self.bestIndex1, ")", sep='')
            self.printActualSolution()
            print("\tCOSTE (km):", self.actualDistance)
            print("\tITERACIONES SIN MEJORA:", self.iterationsWithoutImprovement)
            print("\tLISTA TABU:")
            if tabuCount > self.tendencyParameter:
                self.tabuList.remove(self.tabuList[0])
                tabuCount -= 1
            for element in self.tabuList:
                print("\t", element[0], " ", element[1], sep='')


            if self.iterationsWithoutImprovement == self.maxIterationsWithoutImprovement:
                print()
                self.restart+=1
                print("***************")
                print("REINICIO:",self.restart)
                print("***************")
                self.tabuList.clear()
                self.iterationsWithoutImprovement=0
                self.actualSolution=self.solution
                self.actualDistance=self.minimalDistance
                tabuCount=0
            print()

    #
    def run(self):
            print("RECORRIDO INICIAL")
            self.printActualSolution()
            print("\tCOSTE (km):",self.newDistance)
            print()
            self.calculateNeighbors()
            print()
            print("MEJOR SOLUCION: ")
            self.actualSolution=self.solution
            self.printActualSolution()
            print("\tCOSTE (km):", self.minimalDistance)
            print("\tITERACION:",self.solIteration)