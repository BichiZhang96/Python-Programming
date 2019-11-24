# assignment 1
import logging
import re

logging.basicConfig(filename='Assignment4Q1.log', level=logging.DEBUG)  # create a log file and level is debug
numbers = []
try:
	with open("input1.txt") as read_file:  # try to open input1.txt
		for line in read_file:
			line = line.replace("\n", "")
			numbers.append(line)  # convert the file to a list
		for number in numbers:
			if len(number) == 12:  # use regular expressions to judge
				judge = re.match(r'^[0-9]{3}-[0-9]{3}-[0-9]{4}$', number)
				if judge is False:
					logging.info('The number is not a valid phone number: %s', number)
					numbers.remove(number)
			elif len(number) == 14:
				judge = re.match(r'^\([0-9]{3}\)\s[0-9]{3}-[0-9]{4}$', number)
				if judge is False:
					logging.info('The number is not a valid phone number: %s', number)
					numbers.remove(number)
			else:
				logging.info('The number is not a valid phone number: %s', number)
				numbers.remove(number)
	print(numbers)
except FileNotFoundError:  # File not found error
	print("Could not find the file named input1.txt")
	logging.info('Could not find the file named input1.txt')
except OSError:  # os error
	print("File found - error reading file")
	logging.info('File found - error reading file')
except Exception:  # other error
	print("An unexpected error occurred")
	logging.info('An unexpected error occurred')

# assignment 2
import logging
import re

logging.basicConfig(filename='Assignment4Q2.log', level=logging.DEBUG)
in_matrix = []
in_list = []
out_list = []
col = row = 0
try:
	with open("input2.txt", "r") as read_file:  # try to open input2.txt
		for line in read_file:  # convert the file to a list
			line = line.replace("\n", "")
			in_list.append(line)
		for string in in_list:  # delete the whitespace
			judge = re.match(r'^\s+$', string)
			if judge:
				in_list.remove(string)
		print(in_list)
		for string in in_list:  # convert the list to matrix
			in_list = string.split(" ")
			in_matrix.append(in_list)
			print(in_matrix)
			col += 1  # get the number of rows and columns of the matrix
			if len(in_list) > row:
				row = len(in_list)
		out_matrix = [[0 for i in range(row)] for j in range(col)]
		print(out_matrix)
		for i in range(col):  # reverse the in_matrix and store in out_matrix
			for j in range(row):
				out_matrix[j][i] = in_matrix[i][j]
			print(out_matrix)
		for i in range(row):  # convert the matrix to list
			out_list.append(tuple(out_matrix[i]))
		print(out_list)
except FileNotFoundError:
	print("Could not find the file named input2.txt")
	logging.info('Could not find the file named input2.txt')
except OSError:
	print("File found - error reading file")
	logging.info('File found - error reading file')
except Exception:
	print("An unexpected error occurred")
	logging.info('An unexpected error occurred')
try:  # write the list to the output2.txt file
	with open("output2.txt", "w") as out_file:
		out_file.write(str(out_list))
except FileNotFoundError:
	print("Could not find the file named output2.txt")
	logging.info('Could not find the file named output2.txt')
except OSError:
	print("File found - error reading file")
	logging.info('File found - error reading file')

# assignment 3
import logging
import re

logging.basicConfig(filename='Assignment4Q3.log', level=logging.DEBUG)


def display_menu():
	print("The Libary Manager")
	print()
	print("COMMAND MENU")
	print("1 - Add books")
	print("2 - Remove books")
	print("3 - Add membership")
	print("4 - Remove membership")
	print("5 - Rent books")
	print("6 - List books")
	print("7 - List members")
	print("8 - Exit")


def write_books(books):
	try:
		with open("Books.txt", "w") as file:  # write the information stored in list called books to the Books.txt
			for book in books:
				file.write(book + "\n")
	except FileNotFoundError:
		print("Could not find the file named Books.txt")
		logging.info('Could not find the file named Books.txt')
	except OSError:
		print("File found - error reading file")
		logging.info('File found - error reading file')
	except Exception:
		print("An unexpected error occurred")
		logging.info('An unexpected error occurred')


def read_books():
	books = []
	try:
		with open("Books.txt") as file:  # read books information from Books.txt and return a list called books
			for line in file:
				line = line.replace("\n", "")
				books.append(line)
		return books
	except FileNotFoundError:
		print("Could not find the file named Books.txt")
		logging.info('Could not find the file named Books.txt')
	except OSError:
		print("File found - error reading file")
		logging.info('File found - error reading file')
	except Exception:
		print("An unexpected error occurred")
		logging.info('An unexpected error occurred')


def add_books(books):
	book = input("Please input a book's name: ")  # use append to add a book to the end of the list and use write_books function to write to the file
	try:
		books.append(book)
		write_books(books)
		print(book + " was added.\n")
	except AttributeError:
		print("There is not a file called book.txt or there are not any books in the file")
		logging.info('There is not a file called book.txt or there are not any books in the file')


def remove_books(books):
	index = input("Please input the name of book you want to remove: ")  # use remove to delete a book and use write_books function to write to the file
	try:
		books.remove(index)
		write_books(books)
		print(index + " was deleted.\n")
	except ValueError:
		print("Please input a correct name of book")
		logging.info('Input a wrong name of book')
	except AttributeError:
		print("There is not a file called book.txt")
		logging.info('There is not a file called book.txt')


def read_membership():
	membership = []
	try:
		with open("Membership.txt") as file:  # read membership information from Membership.txt and return a list called membership
			for line in file:
				line = line.replace("\n", "")
				membership.append(line)
		return membership
	except FileNotFoundError:
		print("Could not find the file named Membership.txt")
		logging.info('Could not find the file named Membership.txt')
	except OSError:
		print("File found - error reading file")
		logging.info('File found - error reading file')
	except Exception:
		print("An unexpected error occurred")
		logging.info('An unexpected error occurred')


def write_membership(membership):
	try:
		with open("Membership.txt", "w") as file:  # write the information stored in list called membership to the Membership.txt
			for member in membership:
				file.write(member + "\n")
	except FileNotFoundError:
		print("Could not find the file named Membership.txt")
		logging.info('Could not find the file named Membership.txt')
	except OSError:
		print("File found - error reading file")
		logging.info('File found - error reading file')
	except Exception:
		print("An unexpected error occurred")
		logging.info('An unexpected error occurred')


def add_membership(membership):
	member_name = input("Please input name: ")
	if member_name.isalpha():  # use isalpha to check if the input name is composed of letters
		member_dob = input("Please input DOB (form: MM/DD/YYYY): ")
		if re.match(r'(0?[1-9]|1[0-2])/([0-2][0-9]|3[0-1])/([1-2]\d{3})', member_dob):  # use re to check the date of birth
			member_phone = input("Please input phone number (form:xxx-xxx-xxxx): ")
			if re.match(r'\d{3}-\d{3}-\d{4}', member_phone):  # use re to check the phone number
				member = member_name + " " + str(member_dob) + " " + str(member_phone)  # combine all the inputs together as a string
				try:
					membership.append(member)  # use append to add the string called member to the end of the list called membership and use write membership to write to the file
					write_membership(membership)
					print(member + " was added.\n")
				except AttributeError:
					print("There is not a file called Membership.txt or there are not any members in the file")
					logging.info('There is not a file called Membership.txt or there are not any members in the file')
			else:
				print("Please input a correct phone nubmer")
		else:
			print("Please input a correct DOB!")
	else:
		print("Please input a correct name!")


def remove_membership(membership):
	index = input("Please input the member you want to delete (form:name mm/dd/yyyy xxx-xxx-xxxx): ")
	try:
		membership.remove(index)  # use remove to delete index in list and use write_membership function to write to the file
		write_membership(membership)
		print(index + " was deleted.\n")
	except ValueError:
		print("Please input a correct member")
		logging.info('Input a wrong name of book')
	except AttributeError:
		print("There is not a file called book.txt")
		logging.info('There is not a file called book.txt')


def rent_book(books, membership):
	print("Please input the book's name: ")
	rent_b = input()
	print("Please input the your name: ")
	rent_name = input()
	print("Please input the your DOB: ")
	rent_dob = input()
	print("Please input the your phone number: ")
	rent_phone = input()
	rent_info = rent_name + " " + rent_dob + " " + rent_phone
	rent = rent_b + " " + rent_info
	if rent_b in books and rent_info in membership:  # check if the name of books and the information of member are correct
		try:
			with open("Rent.txt", "w") as file:
				file.write(rent)
				print(rent, " rent information has been writen")
		except FileNotFoundError:
			print("Could not find the file named Rent.txt")
			logging.info('Could not find the file named Rent.txt')
		except OSError:
			print("File found - error reading file")
			logging.info('File found - error reading file')
		except Exception:
			print("An unexpected error occurred")
			logging.info('An unexpected error occurred')
	else:
		print("Please check your input!")


def list_book(books):
	for i in range(len(books)):  # use loops to print the books information
		book = books[i]
		print(str(i + 1) + ". " + book)
	print()


def list_members(membership):
	for i in range(len(membership)):  # use loops to print the membership information
		member = membership[i]
		print(str(i + 1) + ". " + member)
	print()


display_menu()
books = read_books()
membership = read_membership()
while True:
	command = input("Command: ")
	if command == "1":
		add_books(books)
	elif command == "2":
		remove_books(books)
	elif command == "3":
		add_membership(membership)
	elif command == "4":
		remove_membership(membership)
	elif command == "5":
		rent_book(books, membership)
	elif command == "6":
		list_book(books)
	elif command == "7":
		list_members(membership)
	elif command == "8":
		break
	else:
		print("Not a valid command. Please try again.\n")

# assignment 4
import random
import logging

logging.basicConfig(filename='Assignment4Q4.log', level=logging.DEBUG)


def judge_player():
	with open("input3.txt", "r") as file:  # get the first line and determine which player is player 1 by checking the third letter is X or O
		line1 = file.readline()
		global player1, player2
		if line1[2] == "X":
			player1 = "A"
			player2 = "B"
		elif line1[2] == "O":
			player1 = "B"
			player2 = "A"
		else:
			print("Please input a correct file!")
		print("Player 1 is ", player1)
		print("Player 2 is ", player2)


def play(player):
	sum = 0
	i = j = 0
	if player == "B":  # if it is player B's turn
		while i < 9:
			if in_list[i] == '-':  # for all the space which is not occupied, try if it can win directly
				in_list[i] = "O"
				judge_list(in_list)
				if winner == "B":  # if this position can help player win directly, stop the loop and the winner=B
					break
				else:
					in_list[i] = "-"  # if this position can not help player win directly, restore the element
			i += 1
		while j < 9 and winner != "B":  # if the position can not help player win directly check if opponent will win in its next round will win directly
			if in_list[j] == '-':
				in_list[j] = "X"
				judge_list(in_list)
				if winner == "A":  # if opponent will win in its next round, fill this position
					in_list[j] = "O"
					sum += 1
					break
				else:
					in_list[j] = "-"  # count the number of spaces which are empty and store their position
					para_list.append(j)
			j += 1
		if sum == 0:  # if the opponent will not win directly in its next round
			length = len(para_list)
			if length > 1:  # if the number of spaces empty are greater than 1,random choose a space to fill
				ran = random.randrange(0, length - 1)
				in_list[para_list[ran]] = "O"
			elif length == 1:  # if the number of spaces empty is equal to 1
				in_list[para_list[0]] = "O"
	elif player == "A":  # same strategy to player A
		while i < 9:
			if in_list[i] == '-':
				in_list[i] = "X"
				judge_list(in_list)
				if winner == "A":
					break
				else:
					in_list[i] = "-"
			i += 1
		while j < 9 and winner != "A":
			if in_list[j] == '-':
				in_list[j] = "O"
				judge_list(in_list)
				if winner == "B":
					in_list[j] = "X"
					sum += 1
					break
				else:
					in_list[j] = "-"
					para_list.append(j)
			j += 1
		if sum == 0:
			length = len(para_list)
			if length > 1:
				ran = random.randrange(0, length - 1)
				in_list[para_list[ran]] = "X"
			elif length == 1:
				in_list[para_list[0]] = "X"


def judge_list(list):
	global winner  # check if the player will win directly
	lines3 = [list[0:3], list[3:6], list[6:9], list[0::3], list[1::3], list[2::3], list[0::4], list[2:7:2]]
	if ['X'] * 3 in lines3:
		winner = "A"
	elif ['O'] * 3 in lines3:
		winner = "B"
	elif '-' not in in_list:
		winner = "Draw"
	else:
		winner = " "


in_list = ['-'] * 9
para_list = []
m = n = 0
try:
	with open("input3.txt", "r") as file:
		for line in file:
			if line[2] == "X":  # get the position from the input3.txt and store the information in a list (easy to operate)
				in_list[int(line[0]) - 1] = "X"
			elif line[2] == "O":
				in_list[int(line[0]) - 1] = "O"
			else:
				break
		winner = " "
		judge_player()
		num = in_list.count('-')  # count the number of spaces to determine the next round
		player = [player1, player2]
		if num % 2 == 0 and num / 2 != 0:  # if the number of spaces is even, the input round is odd, it is player 2's round
			for i in range(num):
				i = (i + 1) % 2
				play(player[i])
				if winner == player[i]:
					break
		elif num % 2 == 1:  # if the number of spaces is odd, the input round is even, it is player 1's round
			for i in range(num):
				i = i % 2
				play(player[i])
				if winner == player[i]:
					break
		else:
			judge_list(in_list)
		print("Winner:", winner)
except FileNotFoundError:
	print("Could not find the file named input3.txt")
	logging.info('Could not find the file named input3.txt')
except OSError:
	print("File found - error reading file")
	logging.info('File found - error reading file')
except Exception:
	print("An unexpected error occurred")
	logging.info('An unexpected error occurred')
