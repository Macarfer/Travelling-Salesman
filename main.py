import fileManager
import citiesVector

#Run with a.out distanceFile.txt random_file
#path to file
path='./distances_10.txt'
path2='./random_ls_2016.txt'

# Extracts the number of cities from the file name
numberOfCities = int(path.split('_')[1].split('.')[0])

#First we open the desired file and obtain a distance matrix
distanceMatrix=fileManager.openFile(path,numberOfCities)

#The next step for this project is to obtain a neighbor matrix that we're going to use not to generate
#two times the same neighbor
neighborMatrix=[[0] * (i+1) for i in range(numberOfCities)]


#We also need a solution vector that will contain the solution itself
#In first instance the solution will be generated randomly and all solutions will be compared
#with the actual best solution

solutionVector=citiesVector.generateInitialSolution(numberOfCities)

citiesVector.calculateDistance(distanceMatrix,solutionVector)