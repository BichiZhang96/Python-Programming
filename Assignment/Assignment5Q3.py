import logging

logging.basicConfig(filename='Assignment5Q3.log', level=logging.DEBUG)  # create a log file and level is debug


class PathFinder:  # create a class called pathfinder
	def __init__(self, size, start_pos, end_pos, obs_pos, grid=None):  # parameters: size,start, end and obstacle positions and a grid
		if grid is None:
			grid = []
		self.size = size
		self.startx = (int(start_pos) - 1) // 7
		self.starty = (int(start_pos) - 1) % 7
		self.endx = (int(end_pos) - 1) // 7
		self.endy = (int(end_pos) - 1) % 7
		self.obs = obs_pos
		self.grid = grid
		self.currentx = (int(start_pos) - 1) // 7
		self.currenty = (int(start_pos) - 1) % 7

	def create(self):  # create the empty grid
		self.grid = [["-"] * (self.size) for i in range(self.size)]
		return self.grid

	def start_end(self):  # give the start and the end positions
		self.create()
		self.grid[self.startx][self.starty] = "S"
		self.grid[self.endx][self.endy] = "E"
		return self.grid

	def obstacle(self):  # give the obstacle positions
		self.start_end()
		for i in range(len(self.obs)):
			self.grid[(int(self.obs[i]) - 1) // 7][(int(self.obs[i]) - 1) % 7] = "O"
		return self.grid

	def print(self):  # print the matrix
		for i in range(self.size):
			for j in range(self.size):
				if j % 7 != 6:
					print(self.grid[i][j], end="")
				if j % 7 == 6:
					print(self.grid[i][j])

	def walk(self):  # run the game
		self.obstacle()
		step_sum = 0
		path = [(self.startx,self.starty)]  # store the path information to output the matrix
		footprint = []  # store the footprint information to check if it has been passed
		steps = ((1, 0), (0, 1), (-1, 0), (0, -1))  # down, right, up, left
		while self.currentx != self.endx or self.currenty != self.endy:
			for h, v in steps:
				step_sum += 1  # count the steps, when sum is 4 it means the position cannot move, we need to go back
				if self.currentx + h == self.endx and self.currenty + v == self.endy:
					path.append((self.currentx + h, self.currenty + v))
					break
				elif 0 <= self.currentx + h < self.size and 0 <= self.currenty + v < self.size:
					if self.grid[self.currentx + h][self.currenty + v] == "-" and (
							self.currentx + h, self.currenty + v) not in footprint:
						path.append((self.currentx + h, self.currenty + v))
						footprint.append((self.currentx + h, self.currenty + v))
						step_sum = 0
						break
					else:  # the next position is not empty or has been passed
						if step_sum == 4:  # if this position is the fourth try, go back
							path.pop()
							step_sum = 0
				else:  # if the next position is out of range and the position is the fourth try, go back
					if step_sum == 4:
						step_sum = 0
						path.pop()
			try:  # if there is no element in the path, it means the destination is unreachable
				self.currentx, self.currenty = path[-1]
			except IndexError:
				print("Unreachable Destination!")
				break
		path.pop(0)  # remove the start and the destination position information
		path.pop()
		for route in path:  # change the route in the grid
			i, j = route
			self.grid[i][j] = "#"
		return True

def main():
	try:
		with open("assignment5_input.txt") as file:
			size = int(file.readline())  # size
			start_end = file.readline().split()
			start_pos = start_end[0]  # start position
			end_pos = start_end[1]  # end position
			obs_pos = []
			for line in file.readlines():  # obstacle positions
				line = line.strip()
				obs_pos.append(line)
			finder = PathFinder(size=size, start_pos=start_pos, end_pos=end_pos, obs_pos=obs_pos)
			finder.walk()
			finder.print()
	except FileNotFoundError:
		print("Could not find the file named assignment5_input.txt")
		logging.info('Could not find the file named assignment5_input.txt')
	except Exception:  # other error
		print("An unexpected error occurred")
		logging.info('An unexpected error occurred')


if __name__=='__main__':
	main()
