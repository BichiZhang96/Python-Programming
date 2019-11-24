import csv
import warnings
import logging
import numpy as np

np.set_printoptions(suppress=True)
warnings.simplefilter(action='ignore',category=FutureWarning)  # it will give futurewarning when check if any of the row values for zeros because the title is string

logging.basicConfig(filename='Assignment8P2.log', level=logging.DEBUG)

try:
    with open('heart.csv', 'r') as f:  # store the file data in list
        hearts = list(csv.reader(f, delimiter='\t'))
except FileNotFoundError:
    print("Could not find the file named assignment5_input.txt")
    logging.info('Could not find the file named assignment5_input.txt')
except Exception:  # other error
    print("An unexpected error occurred")
    logging.info('An unexpected error occurred')

a = np.array(hearts)  # store the file data in a numpy array
print("Display first three rows:", a[:3, ...])  # slice
print("Check if any of the row values for zeros:", np.any(a == 0))
b = np.random.rand(7, 1)  # create a random array
print("Using random function to generate 7 values and display it:", b)
np.random.shuffle(b)  # shuffle it
print("Use shuffle function and display the values", b)
print("The minimum value from the array:", np.min(b), "The maximum value from the array:", np.max(b))
c = []
with open('heart.csv', 'r') as f:  # get each line data as a string and store as a list
    heart = csv.reader(f, delimiter='\t')
    i = 0
    for line in heart:
        d = []
        if 0 < i < 5:
            string = ""
            for data in line:
                string = string + " " + data
            i += 1
            d.append(string)
            c.append(d)
        elif i == 0:
            i += 1
        else:
            break
print("The 1 x n matrix is:", np.transpose(c))  # c is n x 1 matrix, use transpose function to transpose it
print("The n x 1 matrix is:", c)

twoD_matrix = np.random.rand(3, 3)
print("The randomly generated 2 dimensional matrix is:", twoD_matrix)
values, vectors = np.linalg.eig(twoD_matrix)  # this function can get Eigen Values and Eigen Vectors
print("Eigen Values:", values)
print("Eigen Vectors:", vectors)
