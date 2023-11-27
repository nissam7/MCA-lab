class Rectangle:
	def __init__(self,length,breadth):
		self.length=length
		self.breadth=breadth
	
	def area(self):
		return self.length*self.breadth
	
	def perimeter(self):
		return 2*(self.length+self.breadth)

	def compare_area(self,other_rectangle):
		if self.area()>other_rectangle.area():
			return "The first rectangle has a larger area."
		elif self.area()<other_rectangle.area():
			return "The Second rectangle has a larger area."
		else:
			return"Botch rectangles have the same area."

rectangle1=Rectangle(5,10)
rectangle2=Rectangle(8,6)

print("Rectangle 1 Area:",rectangle1.area())
print("Rectangle 1 perimeter:",rectangle1.perimeter())

print("\nRectangle 2 Area:",rectangle2.area())
print("Rectangle 2 perimeter:",rectangle2.perimeter())
comparison_result=rectangle1.compare_area(rectangle2)
print("\ncomparison result:",comparison_result)
