class grade:
    def __init__(self,name,score):
        self.name=name
        self.score=score
    def s_grade(self):
        if self.score >= 90:
            self.grade="A"
        elif self.score >= 80:
            self.grade="B"
        else:
            self.grade="C"
    def __str__ (self):
        return "%s:%c 등급" %(self.name,self.grade)
    
a1=grade("혜성",89)
a1.s_grade()
print(a1)