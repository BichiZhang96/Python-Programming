import logging

logging.basicConfig(filename='Assignment5Q4.log', level=logging.DEBUG)  # create a log file and level is debug


class Node():  # create a node class to store the node information
	def __init__(self, data, next=None):
		self.data = data
		self.next = next


class LinkedList(object):  # create a linkedlist class
	def __init__(self, head=None, tail=None):  # linkedlist has head and tail for the first and the last element
		self.head = head
		self.tail = tail

	def addElement(self, data):
		node = Node(data)
		if self.head is None:  # if the head is empty, head=tail=node
			self.head = node
			self.tail = node
		else:  # if there is a element in head, tail=node
			self.tail.next = node
			self.tail = node

	def iter(self):
		if not self.head: # if head is empty,return
			return
		cur = self.head
		yield cur.data  # return current head data
		while cur.next:
			cur = cur.next
			yield cur.data  # return current next data until tail

	def removeElement(self, data):
		cur = self.head
		previous = None
		found = False
		while not found:
			if cur.data == data:  # if data is found, stop the loop
				found = True
			else:  # if current data != data want to remove, previous = current data, current = next data,
				previous = cur
				cur = cur.next
		if cur.next is None:  # if next data is none, the data want to remove is tail, tail = previous to delete the last one
			self.tail = previous
		if previous is None:  # if previous is none, the data want to remove is head, head = next data
			self.head = cur.next
		else:  # in other situation, previous = next data
			previous.next = cur.next

	def print_str(self):
		for node in LinkedList.iter(self):  # for LinkedList.iter, print elements in it
			print('node: {0}'.format(node))


class Stack():
	def __init__(self, top=None):
		self.top = top

	def push(self, data):  # create a new node to store in the top of the stack
		self.top = Node(data, self.top)

	def pop(self):  # pick the top element out and this operation will change the stack
		if self.top is None:
			print("Stack is empty, cannot pop anymore.\n")
			return None
		data = self.top.data
		self.top = self.top.next
		return data

	def peek(self):  # return the top element without changing the stack
		return self.top.data if self.top is not None else None

	def print_num(self):
		current = self.top
		while current:
			print("Number: ", format(current.data))
			current = current.next

	def isEmpty(self):  # check if it is empty
		return self.peek() is None


class Structure(Stack, LinkedList):
	def __init__(self):
		Stack.__init__(self, top=None)
		LinkedList.__init__(self, head=None, tail=None)


def main():
	obj = Structure()
	try:
		with open("assignment5q4_input.txt") as file:
			for input in file.readlines():
				input = input.strip()
				if input.isdigit():  # if input is number, use push function
					obj.push(input)
				elif input.isalpha:  # if input is string, use addElement function
					obj.addElement(input)
			obj.print_num()
			obj.print_str()
			obj.pop()  # try to use pop function to remove the top number
			obj.removeElement("abc")  # try to use remove function to remove "abc"
			obj.print_num()  # check if the number and string has been removed correctly
			obj.print_str()
	except FileNotFoundError:
		print("Could not find the file named assignment5_input.txt")
		logging.info('Could not find the file named assignment5_input.txt')
	except Exception:  # other error
		print("An unexpected error occurred")
		logging.info('An unexpected error occurred')


if __name__ == '__main__':
	main()
