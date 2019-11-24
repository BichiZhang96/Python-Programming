# Assignment6Q3
import logging

logging.basicConfig(filename='Assignment6Q3.log', level=logging.DEBUG)


def main():
	try:
		string1 = eval(input("Please input the string array:"))  # ["Python", "Programming", "Programming"]
		string2 = eval(input("Please input the pattern array:"))  # ["X", "Y", "Y"]
		judge = True
		if len(string1) == len(string2):  # compare length
			for i in range(len(string1)):
				for j in range(len(string1)):  # for every i and j, the strings and patterns should be the same
					if j != i:
						if string1[i] == string1[j] and string2[i] != string2[j]:
							judge = False
							break
			print(judge)
		else:
			print("Please input two arrays which have same length!")
	except SyntaxError:  # syntax error
		print("Please input a array with valid characters!")
		logging.info("Please input a array with valid characters!")
	except Exception:  # other error
			print("An unexpected error occurred")
			logging.info('An unexpected error occurred')


if __name__ == '__main__':
	main()
