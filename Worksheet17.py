#Q1
'''
print('Hello World')

#Q2
name=input('Enter your name:')
if name=='Alice':
    print('Greetings',name)
if name=='Bob':
    print('Greetings',name)
    
#Q4
num=0
n=int(input('Enter a number:'))
for i in range(1,n+1,1):
    if i%3==0 or i%5==0:
        num=num+i
        print(num)

#Q6
count=0
counter=1
number=int(input('Enter a number:'))
choose=input('Would you like the product or sum of the number:')
for i in range(1,number+1,1):
    if choose=='Sum'or choose=='sum':
        count=count+i
        print(count)
    elif choose=='Product' or choose=='product':
        counter=counter*i
        print(counter)

#Q7
for i in range(0,13):
    print(i,'x 12','=',i*12)

#Q8
prime=[2]
isprime=True
for i in range(3,101,1):
    for p in prime:
        if i%p==0:
            isprime=False
    if isprime==True:
        prime.append(i)
    else:
        isprime=True
print(prime)
 
#Q9
import random
random= random.randint(1,20 + 1)
guessList=[]
guesses=0
boolean=True

guess=int(input('Guess the secret number between 1 and 20:'))
guesses=guesses+1  
while boolean:
    if guess==random:
        print('SIUU')
        print('You guessed the secret number in',guesses,'guesses')
        boolean=False
        guesses=guesses+1        
        
    if guess !=random:
        print('Níl, Try again')
        if guess not in guessList:
            guesses=guesses+1
            guessList.append(guess)
        guess=int(input('Enter another number:'))
'''
#Q10
noLeap=[]
leapYear=[]
leap=True
while leap:
    for i in range(2022,2043,1):
        if i%4 and i%400:
            noLeap.append(i)
            leap=False
        else:
            leapYear.append(i)
            leap=True
            print(leapYear)