class Matrix2x2:
	def __init__(self, x1: float | int, x2: float | int, x3: float | int, x4: float | int):
        self.matrix = [[x1, x2], [x3, x4]]

    def __repr__(self):
        return f"Matrix2x2([\n  {self.matrix[0]},\n  {self.matrix[1]}\n])"

	def add(self, matrix2: 'Matrix2x2') -> 'Matrix2x2':
		if (isinstance(matrix2, Matrix_2x2)):
		    res = [[0, 0], [0, 0]]
		    for i in range(2):
		        for j in range(2):
		            res[i][j] = self.matrix[i][j] + matrix2.matrix[i][j]
		    return Matrix2x2(res[0][0], res[0][1],	res[1][0], res[1][1])
		else : 
			raise TypeError('{matrix2} is not a Matrix2x2')

	def prod_r(self, r: float | int) -> 'Matrix2x2':
		for i in range(2):  
        	for j in range(2):
            	self.matrix[i][j] *= r
        return Matrix2x2(res[0][0], res[0][1], res[1][0], res[1][1])

	def prod(self, matrix2: 'Matrix2x2') -> 'Matrix2x2':
        if isinstance(matrix2, Matrix_2x2):
            a = self.matrix
            b = matrix2.matrix
            x1 = a[0][0] * b[0][0] + a[0][1] * b[1][0]
            x2 = a[0][0] * b[0][1] + a[0][1] * b[1][1]
            x3 = a[1][0] * b[0][0] + a[1][1] * b[1][0]
            x4 = a[1][0] * b[0][1] + a[1][1] * b[1][1]
            return Matrix2x2(x1, x2, x3, x4)
        else:
            raise TypeError(f"{matrix2} is not a Matrix2x2")

    def determinant(self) -> float:
	    a = self.matrix[0][0]
	    b = self.matrix[0][1]
	    c = self.matrix[1][0]
	    d = self.matrix[1][1]
	    return a * d - b * c

	def solve_system(self, b: Vector2) -> Vector2:
        det = self.determinant()
        a = self.matrix

        det_x = b.x * a[1][1] - b.y * a[0][1]
        det_y = a[0][0] * b.y - a[1][0] * b.x

        x = det_x / det
        y = det_y / det

        return Vector2(x, y)