'''board = [
    [4,9,0,8,0,0,5,1,0],
    [0,1,8,0,5,0,0,0,6],
    [0,0,0,1,6,9,0,0,4],
    [1,0,5,0,9,0,6,0,0],
    [0,7,4,5,1,6,2,9,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7]
]
'''
import csv
def solve(bo):
    #print_board(bo)
    find = find_empty(bo)
    if not find:
        #Find the solution
        return True
        
    else:
        row, col = find

    for i in range(1,10):
        if valid(bo,i, (row,col)):
            bo[row][col] = i
            
            if solve(bo):
                return True
            
            bo[row][col] = 0
    
    return False


def valid(bo, num, pos):


    #row = pos[0]
    #column = pos[1]

    #Need to understand the second if statment

    #Check row
    #Check the number of the constant row and iterate through every column
    for j in range(9):
        #if bo[pos[0]][j] == num and pos[1] != j:
        if bo[pos[0]][j] == num:
            return False
        
    #Check column
    #Check the number of the constant column and iterate through every row
    for i in range(9):
        #if bo[i][pos[1]] == num and pos[0] != i:
        if bo[i][pos[1]] == num:
            return False
    
    #Check box
    box_x = pos[1] // 3
    box_y = pos[0] // 3

    for i in range(box_y*3, box_y*3 + 3):
        for j in range(box_x*3, box_x*3+3):
            if bo[i][j] == num and (i,j) != pos:
                return False
    
    return True


def print_board(bo):
    
    for i in range(9):
        if i % 3 == 0 and i != 0:
            print("- - - + - - - + - - - ")
        
        for j in range(9):
            if j % 3 == 0 and j != 0:
                print("| ", end="")

            if j == 8:
                print(bo[i][j])
            else:
                print(str(bo[i][j]) + " ", end="")

def find_empty(bo):
    for i in range(9):
        for j in range(9):
            if bo[i][j] == 0:
                #print(i,j)
                return (i,j) #row, col
    return None

def input(filename):
    testcase=[]
    with open(filename,newline='') as f:
        reader = csv.reader(f)
        for line in reader:
            row=[]
            for num in line:
                n = int(num)
                row.append(n)
            testcase.append(row)
            #print(type(testcase[0][0]))
    return testcase

board = input('test.csv')
#print_board(board)
solve(board)
print("Solution: ")
print_board(board)

