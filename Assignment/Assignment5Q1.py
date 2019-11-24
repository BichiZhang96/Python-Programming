import math
import logging

logging.basicConfig(filename='Assignment5Q1.log', level=logging.DEBUG)  # create a log file and level is debug


class Sharp:  # create a class called sharp, defult value of height=0
	def __init__(self, rad, hei=0):
		self.rad = rad
		self.hei = hei

	def getArea(self):  # calculate area of the sharp
		if self.hei == 0:
			area = 4 * math.pi * pow(self.rad, 2)
		else:
			area = 2 * math.pi * pow(self.rad, 2) + 2 * self.rad * self.hei
		return area

	def getVolume(self):  # calculate volume of the sharp
		if self.hei == 0:
			volume = 4 / 3 * math.pi * pow(self.rad, 3)
		elif self.hei > 0:
			volume = math.pi * pow(self.rad, 2) * self.hei
		return volume


def main():
	while True:
		print("1. Sphere \n2. Cylinder \n3. Exit\nPlease enter the number of sharp you want to calculate:")
		num = input()
		if num == "1":
			print("Please input the radius of sphere:")
			try:
				rad=float(input())
				if rad > 0:  # the input should greater than 0
					sphere = Sharp(rad=rad)
					print("Sphere Area: ", sphere.getArea())
					print("Sphere Volume: ", sphere.getVolume())
				else:
					print("Please enter a correct nubmer!")
			except ValueError:  # if the input is not a number, print error information
				print("Please enter a correct number!")
				logging.info('Please enter correct numbers!')
			except Exception:  # other error
				print("An unexpected error occurred")
				logging.info('An unexpected error occurred')
		elif num == "2":
			print("Please input the radius and height of cylinder (form: radius, height) :")
			try:
				list = input().split(",")
				if float(list[0]) > 0 and float(list[1]) > 0:  # judge if inputs are greater than 0
					cylinder = Sharp(rad=float(list[0]), hei=float(list[1]))
					print("Cylinder Area: ", cylinder.getArea())
					print("Cylinder Volume: ", cylinder.getVolume())
				else:
					print("Please enter correct nubmers!")
			except IndexError:  # if the input is only one number or not in a correct format
				print("Please enter the information in a correct format!")
				logging.info('Please enter the information in a correct format!')
			except ValueError:  # if the input are not two numbers
				print("Please enter correct numbers!")
				logging.info('Please enter correct numbers!')
			except Exception:  # other error
				print("An unexpected error occurred")
				logging.info('An unexpected error occurred')
		elif num == "3":
			break
		else:
			print("Please enter a correct number!")


if __name__ == '__main__':
	main()
