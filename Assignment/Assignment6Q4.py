# Assignment6Q4
import logging

logging.basicConfig(filename='Assignment6Q4.log', level=logging.DEBUG)


class node():  # create the node class
	def __init__(self, val=None, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right


class Solution:
	pre_list, in_list, post_list = [], [], []

	def create(self, root):  # create the binary tree
		try:
			a = eval(input("Please enter a value between 0 to 9:"))
			if a == None:
				return None
			elif 0 <= a <= 9:  # recursively create the tree according to the node value
				root = node(val=a)
				root.left = self.create(root.left)
				root.right = self.create(root.right)
				return root
			else:
				print("Please enter a correct number or None!")
		except NameError:
			print("Please enter a number or None!")
			logging.info("Please enter a number or None!")
		except TypeError:
			print("Please enter a correct type!")
			logging.info("Please enter a correct type!")

	def pre_order(self, root):  # pre-order traversal
		if root != None:
			self.pre_list.append(root.val)
			self.pre_order(root.left)
			self.pre_order(root.right)
		return self.pre_list

	def in_order(self, root):  # in-order traversal
		if root != None:
			self.in_order(root.left)
			self.in_list.append(root.val)
			self.in_order(root.right)
		return self.in_list

	def post_order(self, root):  # post-order traversal
		if root != None:
			self.post_order(root.left)
			self.post_order(root.right)
			self.post_list.append(root.val)
		return self.post_list

	def path(self, root):  # call two functions to get the path and sum of all paths
		path = ''
		res = []
		self.cre(root, path, res)
		sum = self.split(root, res)
		return res, sum

	def cre(self, root, path, res): # get the path
		if root == None:
			return
		path += str(root.val)
		if root.left != None:
			self.cre(root.left, path + '->', res)
		if root.left != None:
			self.cre(root.right, path + '->', res)
		if root.left == None and root.right == None:
			res.append(path)

	def sum(self, path_list):  # get the sum of all paths
		sum = 0
		for i in range(len(path_list)):
			sum = sum + int(path_list[i]) * pow(10, len(path_list) - i - 1)
		return sum

	def split(self, root, res):  # convert paths to number list
		sum = 0
		for i in res:
			path_list = i.split('->')
			sum = sum + self.sum(path_list)
		return sum


def main():
	s = Solution()
	root = s.create(None)
	pre_order=s.pre_order(root)
	in_order=s.in_order(root)
	post_order=s.post_order(root)
	path, sum = s.path(root)
	print("Pre-order traversal:",pre_order,"\nIn-order traversal:",in_order,"\nPost-order traversal:",post_order)
	print("Path:",path, "\nSum of all paths:", sum)


if __name__ == '__main__':
	main()
