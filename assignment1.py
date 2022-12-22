#ques1
num1=int(input("first number\n"))
num2=int(input("second number\n"))
num3=int(input("third number\n"))
avg=(num1+num2+num3)/3
print(avg)

#ques2
income=int(input("Enter Your Gross Income\n"))
dependents=int(input("Enter no of dependents\n"))
deduction=10000 + 3000*dependents
taxableincome=income-deduction
taxdeducted=taxableincome*0.2
print(taxdeducted)

#ques3
num=int(input("Enter no of seconds:"))
minutes=num//60
seconds=num%60
print("no of minutes:", minutes, "no of second:", seconds)

#ques4
num1=int(25)
num2=int('25')
num3=int(25.0)
add=num1+num2+num3
print(add)

#ques5
import math
i=1
while i<=23:
    a=round(math.sin(15*i*0.0175),4)
    b=round(math.cos(15*i*0.0175),4)
    i=i+1
    print(a , b)
    
