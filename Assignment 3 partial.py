#ques1
a = str(input('enter the string:'))
b = input('Enter word:')
print(a.count(b))

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
list1=list(map(int,input("Enter the numbers separated by space:").split()))

list2=[]
for e in list1:
    t=(e,e*e)
    list2.append(t)

print("\nList containing (n,n^2) is shown below:")
print(list2)


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
word = 'ABCDEFGHIJIK'
i = 12
while i>0:
   word_2 = word[0:i] 
   i = i - 1
   print(word_2)

#ques6
#a
dict = {}
values_list = ('Y','y','n','N')
values_true = ('Y','y')
values_false = ('N','n')
values = 'y'

while values in values_true:
    values_input = str(input('more values?(y/n)'))
    if values_input in values_list: 
        values = values_input
        if values in values_true:
            sid = int(input('Enter Sid\n'))
            name = str(input('Enter Name Of Student\n'))
            dict[sid] = name
        elif values in values_false:   
            print(dict)
    
#b

dict = {}
values_list = ('Y','y','n','N')
values_true = ('Y','y')
values_false = ('N','n')
values = 'y'

while values in values_true:
    values_input = str(input('more values?(y/n)'))
    if values_input in values_list: 
        values = values_input
        if values in values_true:
            sid = int(input('Enter Sid\n'))
            name = str(input('Enter Name Of Student\n'))
            dict[sid] = name
        elif values in values_false:
            print(dict)
            sorted_dict=sorted(dict.items(),key = lambda x:x[1])
            print(sorted_dict)
#c
dict = {}
values_list = ('Y','y','n','N')
values_true = ('Y','y')
values_false = ('N','n')
values = 'y'
dict_1 = {}

while values in values_true:
    values_input = str(input('more values?(y/n)'))
    if values_input in values_list: 
        values = values_input
        if values in values_true:
            sid = int(input('Enter Sid\n'))
            name = str(input('Enter Name Of Student\n'))
            dict[sid] = name
        elif values in values_false:
            print(dict)
            sorted_dict=sorted(dict.items(),key = lambda x:x[1])
            converted_dict = sorted_dict
            print(converted_dict)
#d
dict = {}
values_list = ('Y','y','n','N')
values_true = ('Y','y')
values_false = ('N','n')
values = 'y'

while values in values_true:
    values_input = str(input('more values?(y/n)'))
    if values_input in values_list: 
        values = values_input
        if values in values_true:
            sid = int(input('Enter Sid\n'))
            name = str(input('Enter Name Of Student\n'))
            dict[sid] = name
        elif values in values_false:   
            print(dict)
enter_sid = int(input('Enter Sid for name o student:'))
name_output = str(dict.get(enter_sid))
print(f'Name of student is {name_output}')

#ques7
n=int(input("Enter number of elements N in fibonacci series:\n[N must be positive Integer]: N="))

if n<=0 :
    print("\nError\nNumber of elements in fibonacci series must be integer and greater than zero.")

else:
   
    if n == 1:
        print("\nThe fibonacci series with 1 element is shown below\n[1]")
        print("\nAverage of given fibonacci series is", 1)

    elif n == 2:
        print("\nThe fibonacci series with 2 element is shown below\n[1,1]")
        print("\nAverage of given fibonacci series is", 1)
    
    else:
        
        list1 = [1, 1]
        
        a = 1
        b = 1
        
        for i in range(n - 2):
            s = a + b
            list1.append(s)
            a = b
            b = s
        
        print(f"\nThe fibonacci series with {n} elements is shown below:")
        print(list1)
        
        sum = 0    #intial sum=0
        
        for num in list1:
            sum = sum + num
        average = (sum / n)
        
        two_decimal = "{:.2f}".format(average)
        
        print(f"\nAverage of given fibonacci series is {two_decimal}")

#ques8
set1= {1, 2, 3, 4, 5}
set2= {2, 4, 6, 8}
set3= {1, 5, 9, 13, 17}
print(f"Set1= {set1}\nSet2= {set2}\nSet3= {set3}")
#a
print("\nQ.8(a)")
print("\nA new Set of all 'elements that are in Set1 and Set2 but not both' is:")
set_sym_dif=set1.symmetric_difference(set2)
print(set_sym_dif)
#b
print("\nQ.8(b)")
print("\nA new set of all elements that are 'in only one of the three sets Set1,Set2 and Set3' is:")
set_u1=set1.union(set2)

set_uf=set_u1.union(set3)

set_i1=set1.intersection(set2)

set_if=set_i1.intersection(set3)

set_12=set1.intersection(set2)

set_23=set2.intersection(set3)

set_13=set1.intersection(set3)

set_f1=set_uf-set_12-set_23-set_13
print(set_f1)
#c
print("\nQ.8(c)")
set_c1=set_12.union(set_23)
set_c2=set_c1.union(set_13)
set_final=set_c2-set_if
print("\nA new set of elements that are 'exactly in two of the sets Set1 , Set2 and Set3' is:")
print(set_final)
#d
print("\nQ.8(d)")
set_d={1,2}
set_d.clear()
for i in range(1,11):
    set_d.add(i)
set_new=set_d-set1
print("\nA new set of all Integers in the range 1 to 10 that are not in Set1 is:")
print(set_new)
#e
print("\nQ.8(e)")
set_e=set_d-set_uf
print("\nA new set of all Integers in the range 1 to 10 that are not in Set1 , Set2 and Set3.")
print(set_e)
       
      
