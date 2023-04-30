"""
Напишете програма, реализираща класове базов клас SchoolMember, 
и производни класове Teacher и Student, като всеки от тях има атрибути име и възраст.
Обекти от класа Teacher освен това съхраняват информация за заплатата си и списък от курсовете, които преподават.
Обекти от класа Student съхраняват информация за курсовете, които са записали, годината,
в която е записан всеки всеки курс и списък с оценки за всеки курс.

Конструктурът на Teacher трябва да приема низ за име, години и заплата.
Да са реализирани методите:
getSalary(), който връща заплатата.
addCourse(), който приема два параметъра - сигнатура и име на курс и ги добавя в речник с ключ сигнатурата и стойност името на курса
getCourses(), който разпечатва всички курсове, по един на ред, първо сигнатурата, после интервал, после името.

Контсруктурът на Student приема име и възраст.
Класът студент трябва да реализира следните методи:
attentCourse, който приема сигнатура на курс и година и го добавя в речник с ключ сигнатурата и стойност друг речник, който съдържа ключове grades и year, 
и стойностите им са съответно списък с оценки и година на записване на курса.
addGrade метод, който получава като параметри сигнатура и оценка и добавя оценката в съответния списък в речниковата стойност grades на курса с тази сигнатура. 
Методът извършва това само ако вече съществува курс с това име в речникът с курсове. В противен случай не прави нищо.

getCourses(), който разпечатва всички курсове, по един на ред, първо сигнатурата, после стойността като речник.
getAvgGrade() метод, който приема за входен параметър сигнатура на курс и връща средното аритметично за всичко оценки, съхранени в списъка с оценки.

След тестване на написаните от вас класове оставете основната програма празна. Нека няма никакви декларации на обекти от тези класове, нито приемане на параметри от командния ред, нито друг код в "главната програма".
Програмата да е с име FXXXXX_L7_T1.py, където XXXXX е вашият факултетен номер.
"""

class SchoolMember:
    def __init__(self, name, age):
        self.name = name
        self.age = age

       
class Teacher(SchoolMember):
    def __init__(self,name, age, salary):
        super().__init__(name, age)
        self.salary = salary
        self.courses= {}

        
    def addCourse(self, course_signature, course_name ):
        self.courses[course_signature] = course_name
    
    def getSalary(self):
        return self.salary
        
    def getCourses(self):
        for course_signature, course_name in self.courses.items():
            print(course_signature, course_name)
        
           
    
class Student(SchoolMember):
    def __init__(self, name, age):
        super().__init__(name, age)
        self.courses= {}
    
    def attendCourse(self, course_signature, year ):
        grades_year = {'grades': [], 'year':  year }
        self.courses[course_signature] = grades_year
        
    def addGrade(self, course_signature, grade):
        if course_signature in self.courses:
            self.courses[course_signature]['grades'].append(grade)    
        
    def getCourses(self):
        for course_signature, gradeYear_dictionary in self.courses.items():
            print(course_signature, gradeYear_dictionary)
        
    def getAvgGrade(self, course_signature):
        grades = self.courses[course_signature]['grades']
        return sum(grades) / len(grades)
 
     
    
    """ 
    A = Teacher('Andonov',30,3000)
    print(A.name, A.age)
    print(A.getSalary())
    A.addCourse('CSCB101','Python')
    A.addCourse('CITB201','Databases')
    A.getCourses()

    B = Student('Petrov',21)
    print(B.name, B.age)
    B.attendCourse('CSCB101',2013)
    B.addGrade('CITB203',6)
    B.getCourses()
    B.addGrade('CSCB101',3)
    B.addGrade('CSCB101',4)
    B.getCourses()
    print(B.getAvgGrade('CSCB101'))
    """
    
def main():
    """ """

if __name__ == '__main__':
    main()
