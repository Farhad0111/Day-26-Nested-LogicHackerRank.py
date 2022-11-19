#n = input()
'''x = list(map(int, input().split()))
#m = input()
y = list(map(int, input().split()))
z=0
if y[2] < x[2]:
    z = 10000
elif y[2] == x[2]:
    if y[1] < x[1]:
        z = 500*(x[1]-y[1])
    elif y[0] < x[0]:
        z = 15*(x[0]-y[0])
print(z)'''

class Farhad:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def faru(self):
        self.z=0
        if self.a[2]>self.b[2]:
            self.z=10000
        elif self.a[2]==self.b[2]:
            if self.a[1]>self.b[1]:
                self.z=500*(self.a[1]-self.b[1])
            elif self.a[0]>self.b[0]:
                self.z=15*(self.a[0]-self.b[0])
        print(self.z)
farhad=Farhad(a=list(map(int,input().split())),b=list(map(int,input().split())))
farhad.faru()