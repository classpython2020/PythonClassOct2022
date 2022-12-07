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
        print("i am leelaprasad")

    def adress_ofstudent(self):
        print("my native tirupathi")

    def blood_group(self)
        print("blood group was o+ positive")

prasad=student("raja",212,"A section","A grade")
nithin=student("ravi",333,"b section","a grade")


#employe

class employe:

    def __init__(self,name,eid,designation,remark):
        print("i am executing")
        self.ne=name
        self.id=eid
        self.de=designation
        self.re=remark


    def current_organtion(self):
        print("webmatic solutions")

    def current_noticeperiod(self):
        print("30 days of notice period")

    def experinace_ofemploye(self):
        print("3.5 yaers in automation")

ravi=employe("ravi",4536,"IT","none")
teja=employe("teja",7865,"QA automation","none")
