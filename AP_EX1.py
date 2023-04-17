class university : 
    def __init__ (self, name:str, country:str, city:str, year_of_opening:int, rank:int):
        self.name = name
        self.country = country
        self.city = city
        self.year_of_opening = year_of_opening
        self.rank = rank
    def open(self) :
        print ("university opened")
    def close(self) : 
        print ("university closed")
    def get_employee(self) :
        print ("employee signed")
    def get_student (self) :
        print ("sudent signed")
#creating university class

class person : 
    def __init__ (self, name:str, age:int, gender:bool, weight:int, height:int) :
        self.name = name
        self.age = age
        self.gender = gender
        self.weight = weight
        self.height = height
    def go_to_university(self) :
        print ('now in university')
    def go_home (self) :
        print ('not in university')
    def quit(self) :
        print ('quitted university')
    def go_to_vacation (self) :
        print ('currently in vacation')
    def res (self) :
        print ('currently resting')

class student :
    def __init__ (self, college:str, GPA:int, student_code:int ) :
        self.college = college
        self.GPA = GPA
        self.student_code = student_code
class graduated_student :
    def __init__ (self, employee_status:bool, salary:int) :
        self.employee_status = employee_status
        self.salary = salary
    def teach(self) :
        print ("now teaching in university")
class not_graduated_student :
    def __init__ (self, courses_left :int) :
        self.courses_left = courses_left
    def take_class(self) :
        print ("taking class")
    def give_exam (self) :
        print ("giving exam")
    def study (self) :
        print ("studing")
    def take_course (self) : 
        print ("taken a course")
class employee :
    def __init__ (self, position:str, salary:int, year_of_start:int) :
        self.position = position
        self.salary = salary
        self.year_of_start = year_of_start
    def work(self) : 
        print ("working")
    def promote (self) : 
        self.position = input ("write new position")
    
class professor :
    def __init__ (self, degree : str, classes : int, students : int) :
        self.degree = degree
        self.classes = classes
        self.students = students
    def teach (self) :
        print ('teaching')
    def take_exam (self) : 
        print ('taking exam')
    def give_scores (self) :
        print ('scores given')
class guard : 
    def __init__ (self, gaurding_location : str, time_of_work: int) :
        self.gaurding_location : gaurding_location
        self.time_of_work : time_of_work
    def walking_around(self) : 
        print ('walking around right now')
    def check_students(self) : 
        print ('currently checking students')
     