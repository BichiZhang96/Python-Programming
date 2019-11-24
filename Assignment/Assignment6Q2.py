# Assignment6Q2
import logging

logging.basicConfig(filename='Assignment6Q2.log',level=logging.DEBUG)

class Group:
	def __init__(self, ori):  # have one parameter: original matrix
		self.ori = ori

	def split(self):  # split the original matrix, get the ingredients than appear more than once
		dishes,number,ingredient,ingredients = [],[],[],[]
		for i in range(len(self.ori)):  # for every list in the matrix, get the first element as the dishes' element
			dishes.append(self.ori[i][0])
			for j in range(1,len(self.ori[i])):  # for each list, add the elements to the ingredient list if it is not in it
				if self.ori[i][j] not in ingredient:
					ingredient.append(self.ori[i][j])
					number.append(1)
				else:  # if the element is already in it, number+=1
					k = ingredient.index(self.ori[i][j])
					number[k] += 1
		for i in range(len(number)):  # get all the elements that number greater than 1, sorted and return them
			if number[i]>1:
				ingredients.append(ingredient[i])
		ingredients.sort()
		return ingredients

	def merge(self,ingredients):  # get the output matrix
		output=[]
		for i in ingredients:  # for each ingredient, get the dishes that contain it
			ingredient=[]
			ingredient.append(i)
			for j in range(len(self.ori)):
				if i in self.ori[j]:
					ingredient.append(self.ori[j][0])
			a_part_sorted=sorted(ingredient[1:])  # sorted the dishes
			ingredient[1:]=a_part_sorted
			output.append(ingredient)
		return output

def main():
	try:
		input_list = eval(input("Please enter the dishes and the ingredients:"))
		'''
		[["Salad", "Tomato", "Cucumber", "Salad", "Sauce"],["Pizza", "Tomato", "Sausage", "Sauce", "Dough"],
		["Quesadilla", "Chicken", "Cheese", "Sauce"],["Sandwich", "Salad", "Bread", "Tomato", "Cheese"]]
		'''
		group = Group(input_list)
		output=group.merge(group.split())
		print(output)
	except NameError:
		print("Please enter names of dishes and ingredients with quotation marks!")
		logging.info("Please enter name of dishes and ingredients with quotation marks!")
	except TypeError:
		print("Please enter correct form of names!")
		logging.info("Please enter correct form of names!")
	except SyntaxError:
		print("Please check the end of input!")
		logging.info("Please check the end of input!")
	except Exception:
		print("An unexpected error occurred!")
		logging.info("An unexpected error occurred!")


if __name__=='__main__':
	main()
