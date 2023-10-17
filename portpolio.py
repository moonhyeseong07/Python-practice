class bssm:
    def __init__(self,role,age,name):
        self.school='부소마고'
        self.role=role
        self.age=age
        self.name=name
    def intro(self):
        print("안녕하세요, %s에서 %s를 담당하고 있는 %s살 %s입니다"%(self.school,self.role,self.age,self.name))
role,age,name=input().split()
a=bssm(role,age,name)
a.intro()
