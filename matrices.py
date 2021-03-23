import numpy as np

A = np.array([[4, 6, 2],
            [0, 1, 5],
            [0, 3, 2]])
B = np.array([[0, 1, -1],
            [3, -1, 4],
            [-1, 2, 1]])
            
print("Original matrix A: \n", A, "\n")
print("Original matrix B: \n", B, "\n")

def task1_reshape(matrix, dim1, dim2):
    """ Reshaping a matrix to another dimension """
    return matrix.reshape(dim1, dim2)

def task2_maxmin(matrix):
    """ Finding the maximum and minimum element in a matrix """
    return np.amax(matrix), np.amin(matrix)

def task3_transpose(matrix):
    """ Finding the transpose of a matrix """
    return matrix.T

def task4_onedimarray(matrix):
    """ Converting a matrix into a one dimensinal array """
    return matrix.flatten()
    
def task5_determinant(matrix):
    """ Finding the determinant of a matrix """
    return np.linalg.det(matrix)
    
def task6_diagonal(matrix):
    """ Finding the diagonal elements of a matrix """
    return np.diagonal(matrix)
    
def task7_addsub(matrix1, matrix2):
    """ Calculating the addition and subtraction of two matrices """
    return np.add(matrix1, matrix2), np.subtract(matrix1, matrix2)
    
def task8_matmul(matrix1, matrix2):
    """ Calculatinf the numtiplication of two matrices """
    return np.matmul(matrix1, matrix2)
    
def task9_inv(matrix):
    """ Calculating the inverse of a matrix """
    return np.linalg.inv(matrix)
 
# task 1   
print("Reshaping A: \n", task1_reshape(A, 1, 9), "\n")
# print(task1_reshape(B, 2, 3)) --> throws error
print("Reshaping B: \n", task1_reshape(B, 1, -1), "\n")

#task 2
A_max, A_min = task2_maxmin(A)
print("The maximum value of matrix A is ", A_max, " and the minimum value is: ", A_min, "\n")
B_max, B_min = task2_maxmin(B)
print("The maximum value of matrix A is ", B_max, " and the minimum value is: ", B_min, "\n")

# task 3
print("Transposing A: \n", task3_transpose(A), "\n")
print("Transposing B: \n", task3_transpose(B), "\n")

# task 4
print("Converting A to a one dimensional array: \n", task4_onedimarray(A), "\n")
print("Converting B to a one dimensional array: \n", task4_onedimarray(B), "\n")

# task 5
print("The determinant of A is: ", task5_determinant(A), "\n")
print("The determinant of B is: ", task5_determinant(B), "\n")

# task 6
print("The diagonal elements of A are: ", task6_diagonal(A), "\n")
print("The diagonal elements of B are: ", task6_diagonal(B), "\n")

# task 7
add, sub = task7_addsub(A, B)
print("The addition of A and B is: \n", add, "\n")
print("The subtraction of A and B is: \n", add, "\n")

# task 8
print("On multiplying A with B: \n", task8_matmul(A, B), "\n")
print("On multiplying B with A: \n", task8_matmul(B, A), "\n")

# task 9
print("The inverse matrix of A is: \n", task9_inv(A), "\n")
print("The inverse matrix of B is: \n", task9_inv(B), "\n")
