# this module reads the file passed as an argument
# and returns a matrix that contains the file

def openFile(path,size):
    i=0
    j=0
    #Creates the matrix for storing the distance between cities
    matrix = [[0] * (i+2) for i in range(size-1)]
    #opens the file passed as an argument
    f=open(path)
    #Opens the file in an assumed way and copies it to the matrix
    for line in f:
       j=0
       for element in line.split('\t'):
           matrix[i][j]=int(element)
           j += 1
       i += 1
    #closes the file containing the distance  matrix
    f.close()
    #prints the matrix for debugging purposes
    #for line in matrix:
    #    print(line)
    #returns the actual matrix
    return matrix