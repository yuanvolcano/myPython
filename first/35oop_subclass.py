class SchoolMember:
  """代表了学校中的任何一个成员"""
  def __init__(self, name, age):
    self.name = name
    self.age = age
    print('(Initialized SchoolMember:{})'.format(self.name))

  def tell(self):
    """告诉我细节"""
    print('Name:"{}" Age:"{}"'.format(self.name, self.age), end=" ")

class Teacher(SchoolMember):
  '''表征一个老师'''
  def __init__(self, name, age, salary):
    SchoolMember.__init__(self, name, age)
    self.salary = salary
    print('(Initialized Teacher:{})'.format(self.name))

  def tell(self):
    SchoolMember.tell(self)
    print('Salary:"{:d}"'.format(self.salary))

class Student(SchoolMember):
  '''表征一个学生'''
  def __init__(self, name, age, marks):
    SchoolMember.__init__(self, name, age)
    self.marks = marks
    print('(Initialized Student:{})'.format(self.name))

  def tell(self):
    SchoolMember.tell(self)
    print('Marks:"{:d}"'.format(self.marks))

t = Teacher('Mrs.Smith', 40, 10000)
s = Student('Jackie', 15, 82)

members = [t, s]
for member in members:
  member.tell()