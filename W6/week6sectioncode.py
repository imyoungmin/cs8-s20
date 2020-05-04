#PROBLEM 2
concoction = [[1, 2, 3,],
              [10,11,12,]]

i = 0
j = 0
while(i < len(concoction)):
  while(j < len(concoction[i])):
    print(concoction[i][j])
    j += 1
  j = 0
  i += 1

for lyst in concoction:
    for element in lyst:
        print(element)    

#PROBLEM 3
def printList(lyst):
    for num in range(len(lyst)):
        print("Element {}: {}".format(num, lyst[num]))
lyst = ["into", "the", "unknown"]
printList(lyst)

#PROBLEM 5
lyst = ['a', 'b', 'c', 'd', 'e']
def printList1(lyst):
    for element in lyst:
        element = 'f'
        print(element)
    print(lyst)
    
def printList2(lyst):
    for num in range(len(lyst)):
        lyst[num] = 'f'
        print(lyst[num])
    print(lyst)
    
#PROBLEM 6
matrix1 = [ [1, 2, 3],
           [4, 5, 6] ]
matrix2 = [[]]
matrix3 = [[1]]

def transpose(matrix):
    returnval = [[]]
    for col in range(len(matrix[0])):
        for row in range(len(matrix)):
            returnval[col].append(matrix[row][col])
        if (col+1) != len(matrix[0]):
          returnval.append([])
    return returnval
  
print(transpose(matrix1))
print(transpose(matrix2))
print(transpose(matrix3))

