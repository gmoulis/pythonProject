#Print
print("Hello, SQA batch 11")

x = 5
y = "Student"
print(x*10)
print(y)

#age= "30"
age = 30
y = "Hello, my age is "
print(y + str(age))


z = "7"
a = int(z)
print(a)

#Type of object
b = 6
c = "Hi"
d = True
e = 5,9
print(type(b))
print(type(c))
print(type(d))
print(type(e))

#Sensible aux majuscules
f = 20
F = 30
print(f)
print(F)

#studentMarks = 30 #camel casing
#StudentMarks = 40 #Pascal casing
#student_marks = 50 #Snake casing

g, h, i ="Orange", "Mango", 15
print(g)
print(h)
print(i)

j = k = l = 20
print(j+k+l)

#Si je rajoute une variable (z) n'ayant pas de valeur, message d'erreur
fruits = ["apple", "banana", "cherry"]
x,y,z = fruits
print(z)

#Python Numbers

m = 6
n = 3.5
o = m + n
print("Result for O = " + str(o))

p = "hello"
q = "world"
r = """this is a 
multiline string
and it is very cool.
"""
print(r)

s = "Hello, world"
print(s[1])
print(s[2:5])
print(s[5])
print(s[:5])
print(s.upper())
print(s.lower())
print(s.strip()) #Supprime les caractères à droite et à gauche
print(s.replace("H", "M"))
print(s.find("world"))

t = 10
u = 11
print(u>t)
print(u<t)
print(u==t)
print(bool("hello"))
print(bool())
print(bool(15))

fruitsbis= ["apple", "banana", "cherry"]
print(len(fruitsbis))
print(fruits[1])

list1 = [23, 14, 16, "hello", True]
print(len(list1))

v=5
w=10
print(v+w)

v=5
w=10
print(v-w)

A = "Hello"
B = "I am"
C = "Gaëlle"
print(A,B,C)

#Boolean
D = 50
E = 60
if D>E:
    print("E is greater than D") #Respecter l'espace. Si pas d'espace, message d'erreur
else:
    print("D is smaller than E")

F = 60
G = 60
if F>G:
    print("F is greater than G")
elif F == G:
    print("F is equal to G")
else:
    print("F is smaller to G")

I = 70
J = 80
print("I is greater") if I>J else print("J is greater") #short hand

K = 90
L = 90
print("K is greater") if K>L else print("equal") if K==L else print("J is greater")

cars = ["Suzuki", "BMW", "Toyota"]
x = cars[2]
cars.append("Honda") #Ajout une valeur
cars.pop(1) #Enlève
cars.remove("Toyota") #Enlève
cars.clear() #Enlève tout
print(x)
print(len(cars))



