#ques1
name='Python is a case sensitive language'

#a
print(len(name))

#b
print(name[::-1])

#c
print(name[10:26])

#d
newname=name.replace("a case sensitive","object oriented")
print(newname)

#e
x=name.index("a")
print(x)

#f
y=name.replace(" ","")
print(y) 
y1=newname.replace(" ","")
print(y1)

#ques2
a = "Rishabh Sood"
b = "22104003"
c = "Electrical"
d = '10'
print(f" Hey,{a} Here!\n",f"My SID is:{b}\n",f"I am from {c} department and my cgpa is {d}")

#ques3
a = int(56)
b = int(10)

#1
i=a,b
print(i)

#2
j = a/b
print(j)

#3
k=a**b
print(k,bin(k))

#4
l=a<<2
m=b<<2
print(l,bin(l))
print(m,bin(m))

#5
n=a>>2
p=b>>4
print(n,bin(n))
print(p,bin(p))

#ques4
a = int(input('enter first no :\n'))
b = int(input('enter second number:\n'))
c = int(input('enter third number:\n'))
if b>c:
    if a>b:
       print(a)
    else :
       print(b)
else :
    if a>c:
        print(a)
    else :
        print(c)           

#ques5
a = str(input('enter string:'))
if "name" in a:
    print("yes")
else:
    print("no")    

#ques6
a=int(input('enter first side:\n'))
b=int(input('enter 2 side:\n'))
c=int(input('enter 3 side:\n'))    
d = a+b
e = b+c
f = a+c
if d<c or e<a or f<b:
    print('no')
else :
    print('yes')    

