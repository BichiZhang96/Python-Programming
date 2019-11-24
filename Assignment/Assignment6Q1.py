# Assignment6Q1
import logging

logging.basicConfig(filename='Assignment6Q1.log', level=logging.DEBUG)


class TreeNode:  # create class TreeNode to store the root information
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None


class Solution:
	def Construct(self, pre_list, in_list):  # return the root of TreeNode
		if len(pre_list) == 0:
			return None
		root = TreeNode(pre_list[0])  # initialize the TreeNode = the first element in the pre-order list
		InIndex = in_list.index(pre_list[0])  # find the TreeNode's position in the in-order list
		root.left = self.Construct(pre_list[1:InIndex + 1], in_list[0:InIndex])  # call Construct itself to construct tree on the left and right side
		root.right = self.Construct(pre_list[InIndex + 1:], in_list[InIndex + 1:])
		return root

	def Post(self, root):  # post-order
		if root != None:
			self.Post(root.left)  # create post-order tree
			self.Post(root.right)
			print(root.val, end=" ")


def main():
	try:
		pre_list = eval(input("Please input the pre-order traversal list:"))  # [1, 2, 4, 3, 5, 6]
		in_list = eval(input("Please input the in-order traversal list:"))  # [4, 2, 1, 5, 3, 6]
		S = Solution()
		root = S.Construct(pre_list, in_list)
		S.Post(root)
	except NameError:  # name error if just enter letters
		print("Please enter the correct number list!")
		logging.info("Please enter the correct number list!")
	except ValueError:  # if the lengths of two lists are different
		print("Please enter two lists of the same length!")
		logging.info("Please enter two lists of the same length!")
	except Exception:
		print("An unexpected error occurred!")
		logging.info("An unexpected error occurred!")


if __name__ == '__main__':
	main()
