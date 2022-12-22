

#ques2
a = int(input("enter date of birth\n"))
b = int(input("enter month of birth\n"))
c = int(input("enter year of birth\n"))
if 1<=a<31:
    1<=b<=12
    1800<=c<2025
    a = a+1
    b = b
    c = c
    print(a,b,c)
elif a == 31:
    1800<=c<2025
    if  1<=b<12:
     a = 1
     b=b+1  
     c = c
    elif b == 12:
     a = 1
     b = 1
     c = c + 1
print(a,b,c)

#ques3

#ques4
a = int(input("Please enter the grade points\n"))
if a<4:
   print("not pass")
elif a>3:
    if a == 4:
       b = 'D' 
       c = 'poor'    
    elif a>4:
        if a == 5:
           b = 'C'
           c = 'below average' 
        elif a>5:
            if a == 6:
                b = 'C+'
                c = 'average'
            elif a>6:
                if a == 7:
                    b = 'B'
                    c = 'good'
                elif a>7:
                   if a == 8:
                      b = 'B+'
                      c = 'very good'
                   elif a>8:
                      if a == 9:
                         b='A'
                         c='excellent'
                      elif 10>=a>9:
                           b = 'A+'
                           c = 'Outstanding'
    print("grade is :",b ,"and remark is :", c)    

#ques5
