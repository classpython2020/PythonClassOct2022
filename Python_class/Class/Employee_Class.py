class employee:
    def __init__(self,id_card,salary,work):  #initiliztion method
        self.id=id_card     #instaneous variables
        self.sal=salary
        self.wor=work

    def identity(self):   # instaneous mathods
        return ("Every employee will be having an id to identify the employee, His name is ",self.id)

    def work(self):
        print("every employee will be having some work to do",self.wor)

    def sala(self):
        print("Raja is getting",self.sal, "for his work")


emp=employee("Raja yanamala",30000,"and Raja has testing work")
emp=emp.identity()
print(emp)

# result1=emp.work()
# print(result1)
#
# result2=emp.sala()
# print(result2)