#SQUARE PATTERN
for i in range(4):
   for j in range(4):
        print('*',end=' ')
   print(' ')

#RECTANGLE PATTERN
for i in range(3):
    for j in range(5):
        print('*',end=' ')
    print(' ')

    #RIGHT ANGLE TRANGLE
for i in range(5):
    for j in range(5):
        if(j<=i):
            print('*',end=' ')
        else:
            print('',end='')
    print('')

    #TRIANGLE
for i in range(4):
    for j in range(4-i-1):
        print(' ',end='')
    for k in range(2*i+1):
        print('*',end='')
    print()

    #NUMBER
for i in range(5):
    for j in range(i+1):
        print(j+1,end=' ')
    print()


    #RHOMBUS
for i in range(5):
    for j in range(4-i+1):
        print(end=" ")
    for j in range(4):
        print("*",end="")
    print()
