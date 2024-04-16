# ATTENDENCE PERSENT

nd=int(input('Enter of Working days:-'))
na=int(input('Enter of absent days:-'))
per=(nd-na)/nd*100
print('Your attendence',per)
if per>75:
    print('you are eligible for exam')
else:
    print('you are not eligible for exam')
    

#PERCENTAGE GRADE

per=int(input('Enter your percentage:-'))
if per<25:
    print('Grade-D')
elif per>25 and per<45:
    print('Grade-C')
elif per>45 and per<50:
    print('Grade-B')
elif per>50 and per<60:
    print('Grade-B+')
elif per>60 and per<80:
    print('Grade-A')
elif per>80:
    print('Grade-A+')
    

#SALARY AND BONUS

ser=int(input('Enter your working time of job:-'))
sal=int(input('Enter your salary:-'))
if ser>=10 and ser<60:
    b=10/100*sal
elif ser>=6 and ser<10:
    b=8/100*sal
elif ser<6:
    b=5/100*sal
print('Bonus',b)

# NET PRICE AND DISCOUNT

price=int(input('Enter prices:-'))
if price>10000:
    d=20/100*price
if price>7000 and price<=10000:
    d=15/100*price
if price<7000:
    d=10/100*price
na=price-d
print('Net price',na)
print('Discount',d)


# PERCENTAGE

per=int(input('Enter your percentage:-'))
if per<40:
    print('failed')
elif per>40 and per<55:
    print('fail')
elif per>55 and per<65:
    print('good')
elif per>=65 and per<100:
    print('excellent')


# TRIANGLE

s1=int(input('Enter your side1:-'))
s2=int(input('Enter your side2:-'))
s3=int(input('Enter your side3:-'))
if s1==s2==s3:
    print('Equilaterial Triangle')
elif (s1==s2 and s1!=s3) or (s1==s3 and s1!=s2) or (s2==s3 and s2!=s1):
    print('Isosceles triangle')
elif s1!=s2!=s3:
    print('Scalene Triangle')


# OPERATOR

num1=int(input('Enter first num1:-'))
num2=int(input('Enter second num2:-'))
op=input('Select operator (+,-,*,/):-')
if op=='+':
    print('result is',num1+num2)
if op=='-':
    print('result is',num1-num2)
if op=='/':
    print('result is',num1/num2)
if op=='*':
    print('result is',num1*num2)    


# MALE AND FEMALE AGE

age=int(input('Enter age(18 to 40):-'))
gender=input('Enter gender(m/f):-')
day=int(input('Enter working days:-:-'))
if age>=18 and age<30:
    if gender=='m':
        amt=day*700
        print('Wage',amt)
    else:
        amt=day*750
        print('Wage',amt)
if age>30 and age<40:
    if gender=='m':
        amt=day*800
        print('Wage',amt)
    else:
        amt=day*850
        print('Wage',amt)
