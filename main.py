import shortPathFinder as spf
import argparse as arg
#Run with a.out distanceFile.txt random_file
#path to file
#The input is processed
parser = arg.ArgumentParser(description="Given a matrix of distances between cities, calculates a good travelling salesman solution")
parser.add_argument('path',metavar='pathToDistancesFile',nargs=1,help='A text file containing an inferior triangular matrix with the distance between cities',action='store')
parser.add_argument('path2',metavar='pathToRandomsFile',help='A text file containing a set of random numbers',nargs='?',default=0,action='store')
args = parser.parse_args()
finder = spf.TravellingSalesman(args.path[0],args.path2)
finder.generateInitialSolution()
finder.run()
#First we open the desired file and obtain a distance matrix
# distanceMatrix=fileManager.openFile(path,numberOfCities)
#
# #The next step for this project is to obtain a neighbor matrix that we're going to use not to generate
# #two times the same neighbor
# neighborMatrix=[[0] * (i+1) for i in range(numberOfCities)]
#
#
# #We also need a solution vector that will contain the solution itself
# #In first instance the solution will be generated randomly and all solutions will be compared
# #with the actual best solution
#
# solutionVector=citiesVector.generateInitialSolution(numberOfCities)
#
# actualDistance=citiesVector.calculateDistance(distanceMatrix,solutionVector)
#
# print("Actual distance ",actualDistance)
#
# citiesVector.calculateNeighbors(numberOfCities,neighborMatrix)
