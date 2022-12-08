class Car:

    def __init__(self,color,Cu,cost,move):   # intilisation method
        print("I am executing")
        self.col=color    #instaneous variables
        self.c=Cu
        self.cos=cost
        self.mo=move

    def move_right(self):   #instaneous method
        print("I can move right"+self.mo)

    def move_left(self):
        print("I am able to movie"+self.mo)

    def move_reverse(self):
        print("I can travel reverse")

i20=Car("blac",2000,15555,"right")   #object
i20sports=Car("whit2",2500,1555,"left")

i20.move_left()
i20sports.move_right()

#pratice and workout

#students
class student:

    def __init__(self,name,idnumber,section,grade):
        print("i am executing")
        self.nm=name
        self.id=idnumber
        self.se=section
        self.gr=grade

    def name_ofstudent(self):
        print("i am leelaprasad"+self.nm)

    def adress_ofstudent(self):
        print("my native tirupathi")

    def blood_group(self):
        print("blood group was o+ positive")

prasad=student("raja",212,"A section","A grade")
print(prasad.nm)
nithin=student("ravi",333,"b section","a grade")


#employe


class Car:

    def __init__(self, color, Cu, cost, move):  # intilisation method
        print("I am executing")
        self.col = color  # instaneous variables
        self.c = Cu
        self.cos = cost
        self.mo = move

    def move_right(self):  # instaneous method
        print("I can move right" + self.mo)

    def move_left(self):
        print("I am able to movie" + self.mo)

    def move_reverse(self):
        print("I can travel reverse")


i20 = Car("blac", 2000, 15555, "right")  # object
i20sports = Car("whit2", 2500, 1555, "left")

i20.move_left()
i20sports.move_right()


class employe:

    def __init__(self,name,eid,designation,remark):
        print("i am executing")
        self.ne=name
        self.id=eid
        self.de=designation
        self.re=remark


    def current_organtion(self):
        print("webmatic solutions"+self.ne)

    def current_noticeperiod(self):
        print("30 days of notice period")

    def experinace_ofemploye(self):
        print("3.5 yaers in automation"+self.de)

ravi=employe("ravi",4536,"IT","none")
print(ravi.ne)
teja=employe("teja",7865,"QA automation","none")

# Instant varoables
    # Always bound to object , which are delcare in __init__ method.
    # inside constructor by using self
    # Inside methods should be access by self.variable
    # outside of class by using object reference variable.

# static Variable
    # This value will not be changed
    # inside the constrictor using class name
    # it should inside class outside all methods.
    # Inside Instant method by using class name
    # ouside of class using class name and object name
    # modficataion of variable

# class variable

class Car:
    "This class is about car"
    wheel = 4   # static variable
    def __init__(self,color,Cu,cost,move):   # intilisation method
        #print("I am executing")
        self.color=color    #instaneous variables
        self.Cu=Cu
        self.cost=cost
        self.move=move
        print(Car.wheel)


    def move_right(self):   #instaneous method
        "This method s about moving right or left"
        print("I can move right"+self.move)
        Car.wheel=100
        #print(Car.wheel)

    def move_left(self):
        print("I am able to movie"+self.move)

    def move_reverse(self):
        print("I can travel reverse")

i20=Car("blac",2000,15555,"right")   #object
i20.move_right()
print(Car.wheel)
print(i20.wheel)

# i20sports=Car("whit2",2500,1555,"left")
# print(i20sports.mo)

# i20.move_left()
# i20sports.move_right()