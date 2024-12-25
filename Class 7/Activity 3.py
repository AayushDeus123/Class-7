#Grading System
m = float(input('Enter your marks for Maths = '))
if m>100:
    print('Invalid marks')
e = float(input('Enter your marks for English = '))
if e>100:
    print('Invalid marks')
h = float(input('Enter your marks for Hindi = '))
if h>100:
    print('Invalid marks')
s = float(input('Enter your marks for Science = '))
if s>100:
    print('Invalid marks')
ss = float(input('Enter your marks for Social Studies  = '))
if ss>100:
    print('Invalid marks')
avg = (m+e+h+s+ss)/5

if avg>90:
    print('You have recieved the grade of A+')
elif avg>80 and avg<=90:
    print('You have received the grade of A')
elif avg>70 and avg<=80:
    print('You have received the grade of B+')
elif avg>60 and avg<=70:
    print('You have received the grade of B')
elif avg>50 and avg<=60:
    print('You have received the grade of C+')
elif avg>40 and avg<=50:
    print('You have received the grade of C')
elif avg>32 and avg<=40:
    print('You have received the grade of D')
elif avg>20 and avg<=32:
    print('You have received the grade of E')
elif avg>=0 and avg<=20:
    print('You have received the grade of F')