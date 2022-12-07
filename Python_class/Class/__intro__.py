#Class

#1. class is a block of methods and veriables.
#2. we can create new methods basied on our requirment.
#3. there will be three kind of variables and methods.
#4. we can create class with constractor(intilisation method).
#5. we can also create a class without constractor as well

#Methods
#1. intilisation method
#2. instaneous method
#3. Static method
#4. class method

#Variables
#1. instaneous variables.
#2. static variables ___________class level variable
#3. local variable

##################################################################################################################


#1. intilisation method

#     def __init__(self,id_card,salary,work):  #initiliztion method
#         self.id=id_card
#         self.sal=salary
#         self.wor=work

#1. we can write the constractor below the class to store some of paramaters.
#2. here self can be used as class variable.
#3. objet can be strored in self.

#2. instaneous method

# def identity(self):  # instaneous mathods
#     return ("Every employee will be having an id to identify the employee, His name is ", self.id)

#1. this method can be used with objet.


#1. instaneous variables.

#         self.id=id_card
#         self.sal=salary
#         self.wor=work

#1. these will call as instaneous variable.



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



class human:
    "this class about human"      # to see this we need to use ___doc___ function
    legs=2  #static variable      #we should not change this variable unless we need to change.
    def __init__(self,color,height,weight):  #intilistion method
        self.color=color
        self.height=height       #instantaneous variables
        self.weight=weight
        print(human.legs)        #we can use static variable only with class or object.

    def talk(self):              #instantaneous method
        return ("He can talk",human.legs)   #we can use static variable in methods also.
    def walk(self):
        return ("He can walk")
    def eat(self):
        return ("he can eat")
    def fight(self):
        return ("he can fight")

person=human("Black","5'6",70)
result=person.talk()  #we can use static variable only with class or object.
print((result))
print(person.legs)

#we can use instaneous variables by using object only, with out abject we can'nt use instaneous variable.
#when we call the class automatically the constractor will execute
#to use static variable we need to mention class name before of it
