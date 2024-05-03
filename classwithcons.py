class re:#re=royalenfield
    def __init__(self,name,color,mileage) -> None:
        self.name=name
        self.c=color
        self.m=mileage
a=re("classic 350","black",10)
b=re("xyz",'red',30)
c=re('pqr','white',40)
print(a.name,a.c,a.m) 
print(b.name,b.c,b.m)
print(c.name,c.c,c.m)          

