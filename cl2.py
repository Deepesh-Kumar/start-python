class Student(object):

	def __init__(self, name, school):
		self.name = name
		self.school = school
		self.marks = []

	def average(self):
		return sum(self.marks) / len(self.marks)

	@classmethod
	def friend(cls, origin, fr_name, salary):
		return cls(fr_name, origin.school, 20)



class WorkingStudent(Student):

	def __init__(self, name, school, salary):
		super(WorkingStudent, self).__init__(name, school)
		self.salary = salary





a = WorkingStudent('anna', 'mit', 90)
print a.salary

b = WorkingStudent.friend(a, 'madar', 15 )
print b.salary
