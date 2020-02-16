class Vector:
    def __init__(self,x,y):
        self.x = x
        self.y =y 

    def __repr__(self):
        return "{} ({},{})".format(self.__class__.__name__,self.x,self.y)
        #return

v = Vector(5,3)

print(dir(v))

print(v.__dict__)
print(v.__dict__['x'])

v.__dict__['x'] = 45

print(v.__dict__['x'])

#'x' in v.__dict__: give Flase 
#adding object 

v.__dict__['z'] = 15

print(v.__dict__['z'])

#find
getattr(v,'z')
#in operations 
hasattr(v,'+')

