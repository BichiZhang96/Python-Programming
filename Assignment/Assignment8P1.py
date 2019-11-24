import csv
import logging
import numpy as np
np.set_printoptions(suppress=True)

logging.basicConfig(filename='Assignment8P1.log', level=logging.DEBUG)

try:
    with open('winequality-red.csv', 'r') as f:  # open the file and store it in list
        wines = list(csv.reader(f, delimiter=';'))

    with open('winequality-white.csv', 'r') as f:
        wine = list(csv.reader(f, delimiter=';'))
except FileNotFoundError:
    print("Could not find the input file!")
    logging.info('Could not find the input file!')
except Exception:  # other error
    print("An unexpected error occurred")
    logging.info('An unexpected error occurred')

a = np.array(wines)  # create a array to store the file data
print("Select first 5 items from the 4th column and display the values:", a[:5, 3])  # slice
print("Select all rows of the 6th column and print the values:", a[..., 5])
print("Display all rows and columns:", a)
print("Display 2nd item from 1st row:", a[0, 1])
print("The data type before converting:", a.dtype)
a_data = a[1:, ...].astype(np.float32)  # get all the data in the file, ignore the title
print("The data type after converting:", a_data.dtype)
for i in range(len(wines[0])):  # get the quality column
    if wines[0][i] == "quality":
        quality = i
print("The quality score of the wine before increasing:", a_data[..., quality])
a_in_quality = a_data[..., quality] * 1.15
print("The quality score of the wine after increasing:", a_in_quality)
print(a_data[..., -2])
max_alcohol = np.argmax(a_data[..., -2])  # get the wine which has the highest alcohol
max_quality = np.argmax(a_data[..., -1])  # get the wine which has the highest quality
print("The wine which has the highest alcohol:", a_data[max_alcohol, ...])
print("The wine which has the highest quality:", a_data[max_quality, ...])
print("The sum of all elements in the row 6 of wines:", a_data[4, ...].sum())
print("The sum of all elements in the column 6 of wines:", a_data[..., 5].sum())
quality_7 = np.where(a_data[..., -1] > 7)
print("The wines which have their quality greater than 7:", quality_7)
quality_5 = np.where(a_data[..., -1] == 5)
print("The wines which have quality equal to 5:", quality_5)
print("Display all the wines which have the quality greater than 7:")
print(a_data[np.where(a_data[..., -1] > 7), ...])

b = np.array(wine)
print("The shape of white wines after combining it with wines:", np.concatenate((b, wines)).shape)
print("The shape of white wines after combining it with red wines:", np.concatenate((b, a)).shape)
print("Display the white wines after combining it with wines:", np.concatenate((b, wines)))
print("Display the white wines after combining it with red wines:", np.concatenate((b, a)))
