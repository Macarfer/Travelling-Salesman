import random
import math
import fileManager

class TravellingSalesman:
    #Properties of the class
    numberOfCities=0
    solutionNumber = -1
    neighborNumber=-1
    distanceMatrix=[]
    pathToRandomFile=0
    actualSolution=[]
    actualDistance=0
    newDistance=0
    neighbors = []
    swapMatrix=[]
    swapArrayCount=0
    swapArrayDimension=0
    randomFile = 0

    #Intial function
    def __init__(self,pathToDistances,pathToRandomFile=0):
        # Extracts the number of cities from the file name
        self.numberOfCities = int(pathToDistances.split('_')[1].split('.')[0])
        # First we open the desired file and obtain a distance matrix
        self.distanceMatrix = fileManager.openFile(pathToDistances, self.numberOfCities)
        # #The next step for this project is to obtain a neighbor matrix that we're going to use not to generate
        # #two times the same neighbor
        self.swapMatrix=[[0] * (i+1) for i in range(self.numberOfCities)]
        for i in range(0,self.numberOfCities):
            self.swapMatrix[i][i]=1
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
        print("SOLUCION S_", self.solutionNumber, " -> ", self.actualSolution, "; ",self.actualDistance,"km",sep='')

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

    def calculateInitialDistance(self):
        i = 0
        index01 = 0
        index02 = 0
        self.actualDistance = self.distanceMatrix[self.actualSolution[0] - 1][0]
        while i < (self.numberOfCities - 1):
            index01 = self.actualSolution[i]
            index02 = self.actualSolution[i + 1]
            if index01 > index02:
                self.actualDistance += int(self.distanceMatrix[index01 - 1][index02])
            else:
                self.actualDistance += int(self.distanceMatrix[index02 - 1][index01])

            i += 1
        self.actualDistance += self.distanceMatrix[self.actualSolution[self.numberOfCities - 1]-1][0]
        self.newDistance=self.actualDistance

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
        self.calculateInitialDistance()

    #
    def swap(self,vector,index0,index1):
        returnVector = list(vector)
        returnVector[index0] = vector[index1]
        returnVector[index1] = vector[index0]
        self.swapArrayCount+=1
        return returnVector
    #
    def calculateNeighbors(self):
        #self.neighbors=[[0]*self.numberOfCities]
        # self.neighbors=[self.actualSolution]
        self.swapArrayCount=0
        vector=self.actualSolution
        i=-1
        lineCount=0
        #We repeat the bucle while we haven't reached a better solution
        print()
        self.printActualSolution()
        while self.newDistance >= self.actualDistance and self.swapArrayCount < self.swapArrayDimension:
            self.neighbors.append(vector)
            self.neighborNumber+=1
            lineCount=0
            # First we've got to choose two random numbers to swap them
            #element0=math.floor(self.calculateRandom() * self.numberOfCities)
            # element0=1+math.floor(self.calculateRandom() *self.numberOfCities)

            element0 = math.floor(self.calculateRandom() * self.numberOfCities)

            element1 = math.floor(self.calculateRandom() * self.numberOfCities)

            # print("element0 - element1",element0,element1)

            while self.swapMatrix[max(element0,element1)][min(element0,element1)]==1:
                if element0 == element1:
                    element0 +=1
                    element0 = math.fmod(element0,self.numberOfCities)
                    element0 = int(element0)
                    element1 = 0
                else:
                    tmp=max(element0,element1)
                    element1=min(element0,element1)
                    element1+=1
                    element1 = math.fmod(element1, self.numberOfCities)
                    element1=int(element1)
                    element0=tmp
                    # print("element0 - element1", element0, element1)
            vector=self.swap(self.actualSolution,max(element0,element1),min(element0,element1))
            self.calculateDistance(vector)
            # print("element0 - element1",element0,element1)
            self.swapMatrix[max(element0,element1)][min(element0,element1)]=1
            print("\tVECINO V_", self.neighborNumber, " -> Intercambio: (",max(element0,element1),", ",min(element0,element1),"); ", vector, "; ", self.newDistance,"km",sep='')

        self.actualSolution=vector
        self.neighbors=[]
        self.reinitializeSwapMatrix()
        self.actualDistance=self.newDistance
        self.solutionNumber+=1
        self.neighborNumber=-1
    #
    def run(self):
        while self.swapArrayCount < self.swapArrayDimension:
            self.calculateNeighbors()
