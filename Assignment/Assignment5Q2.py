import logging

logging.basicConfig(filename='Assignment5Q2.log', level=logging.DEBUG)  # create a log file and level is debug


class Compute:
	def __init__(self, element):
		self.element = element

	def __add__(self, other):
		if type(self.element) == tuple and type(other.element) == tuple:  # if two elements are all tuples
			list_self = list(self.element)
			list_other = list(other.element)
			for i in range(len(self.element)):  # converse tuples to lists for calculation
				list_self[i] = float(list_self[i]) + float(list_other[i])
			self.element = tuple(list_self)
			return self.element

		elif type(self.element) == list and type(other.element) == list:  # if two elements are all lists
			for i in range(len(self.element)):
				self.element[i] = self.element[i] + other.element[i]
			return self.element

		elif type(self.element) == dict and type(other.element) == dict:  # if two elements are all dicts
			for i in self.element:
				if i in other.element:  # for each key in self, if it exists in other, add to self and delete other element
					self.element[i] = self.element[i] + other.element[i]
					del other.element[i]
			for k, v in other.element.items():  # add other to self
				self.element[k] = v
			return self.element
		else:
			print("Please enter two elements in the same format!")


def main():
	while True:
		print("Please input the first element you want to calculate: ")
		# use eval to get the input without changing format
		element1 = Compute(eval(input()))  # [1,2,3,4] {1:'abc',3:'xyz',5:'test'}
		print("Please input the second element you want to calculate: ")
		element2 = Compute(eval(input()))  # [3.3,4,5,1.2] {2:'test1',3:'test2',4:'test3'}
		try:
			ans = element1 + element2
			print("The answer is :", ans)
		except TypeError:
			print("Please input two elements in the same format!")
			logging.info('Please input two elements in the same format!')
		except IndexError:
			print("Please input the same range lists!")
			logging.info('Please input the same range lists!')
		print("Do you want to continue? Y/N")
		if input().upper() != "Y":
			break


if __name__ == '__main__':
	main()
