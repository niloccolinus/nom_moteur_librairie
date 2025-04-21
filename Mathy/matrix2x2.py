class Matrix_2x2:
	def __init__ (self,x1,x2,x3,x4):
		matrix = [[x1,x2],[x3,x4]]

	def add (self, matrix2):
		if (isinstance(matrix2, Matrix_2x2)):
			res = [[0,0][0,0]]
			for i in range(0,2):
				for j in range(0,2):
					res[i][j] = self.matrix[i][j] + matrix2[i][j]
			return res
		else : 
			raise Error('{matrix2} is not a matrix')

	def prod_r (self, k):
		for i in range(0,2):
			for j in range(0,2):
				self.matrix[i][j] = self.matrix[i][j] * k

	def prod (self,matrix2):
		if (isinstance(matrix2, Matrix_2x2)):
			x1 = (self.matrix[0][0] * matrix2[0][0]) + (self.matrix[0][1] * matrix2[1][0])
			x2 = (self.matrix[0][0] * matrix2[0][1]) + (self.matrix[0][1] * matrix2[1][1])
			x3 = (self.matrix[1][0] * matrix2[0][0]) + (self.matrix[1][1] * matrix2[1][0])
			x4 = (self.matrix[1][0] * matrix2[0][1]) + (self.matrix[1][1] * matrix2[1][1])
		return [[x1,x2],[x3,x4]]
		else: 
			raise Error('{matrix2} is not a matrix')