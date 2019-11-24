# question 1
print("Please input a list: ")
list_input = eval(input())  # get the input and store as a list
list_output = list(set(list_input))  # converse list to set to remove duplicates
list_output.sort()
print(list_output)

# question 2
print("Please input a matrix: ")
matrix_input = eval(input())  # get the input and store as a list of lists
for x in matrix_input:
	x.reverse()  # reverse each list
	length = len(x)
	i = 0
	while i < length:  # invert the matrix
		if x[i] == 0:
			x[i] = 1
		else:
			x[i] = 0
		i += 1
print(matrix_input)

# question 3
print("Please input a list: ")
web_input = eval(input())  # get the input and store as a list
num_www = num_org = num_mail = num_com = 0
list_item = []
input_length = len(web_input)
for item in web_input:
	list_item.append(item)  # fisrt get the main domain
	length = len(item)
	num_position = item.find(" ")  # get the position of the first space
	num = int(item[0:num_position])  # get the first number
	if "www." in item:  # get the number of www.
		num_www += num
		item = item[num_position + 5:]  # delete the number and www.
	if ".org" in item:  # get the number of .org
		num_org += num
	if ".com" in item:  # get the number of .com
		num_com += num
	if ".mail.com" in item:  # get the number of .mail.com
		num_mail += num
if num_www != 0:
	list_item.append(str(num_www) + " " + item)  # add number and a string do not contain "www." to the list
if num_org != 0:
	list_item.append(str(num_org) + " " + "org")
if num_com != 0:
	list_item.append(str(num_com) + " " + "com")
if num_mail != 0:
	list_item.append(str(num_mail) + " " + "mail.com")
print(list_item)

# question 4
print("Please input a string: ")
string_a = input()
print("Please input another string: ")
string_b = input()
output = []
string_c = string_a + " " + string_b
list_c = string_c.split()  # converse the string to list
for word in list_c:
	if list_c.count(word) == 1:  # if the word only appears once in the list
		output.append(word)
print(output)

# question 5
import copy

print("Please input a matrix: ")
matrix_input = eval(input())
i = j = n = x = y = sum = 0
t_to_b = []
l_to_r = []
for x in matrix_input:  # get the view from left to right and the size of matrix
	l_to_r.append(max(x))
	n += 1
empty = [0] * n
for j in range(0, n):  # get the view from top to bottom
	for i in range(0, n):
		empty[i] = matrix_input[i][j]
		i += 1
	t_to_b.append(max(empty))
	i = 0
	j += 1
matrix_new = copy.deepcopy(matrix_input)  # make a deep copy of input to get the change
for x in range(0, n):
	for y in range(0, n):
		matrix_new[x][y] = min(l_to_r[x], t_to_b[y])  # the grid after adjusting
		sum = sum + matrix_new[x][y] - matrix_input[x][y]  # the total sum of height changes
print(sum)

# question 6
print("Please input a list: ")
array_input = eval(input())
i = j = k = l = sum = 0
array_output = []
length = len(array_input)
array_sort = [""] * length  # create a list to store the strings after sorting
for i in range(0, length):  # sort every string
	array_sort[i] = ''.join(sorted(array_input[i]))
for j in range(0, length):  # count the number of string to judge if there are duplicate strings
	count = array_sort.count(array_sort[j])
	new = [] * count  # create a list to store strings according to the number of strings
	if count == 1:  # if the string only appear once, just use append to output
		new.append(array_input[j])
		array_output.append(new)
	else:  # if the string appear more than once, use new to store all the strings
		for k in range(0, length):
			if array_sort[k] == array_sort[j]:
				new.append(array_input[k])
		array_output.append(sorted(new))
while l < length:  # to remoce the duplicate list in array_output
	if array_output[l] != "":
		if array_output.count(array_output[l]) != 1:
			array_output.remove(array_output[l])
			array_output.append("")
			sum += 1
		else:
			l += 1
	else:
		l += 1
print(array_output[:-sum])

#question 7
num_array=eval(input())
print(sum(set(num_array))*2-sum(num_array))
