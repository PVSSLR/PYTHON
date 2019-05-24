import random

rd = random.randint(1,9)
g = int(input('Enter your guess: '))
count = 0
count = count+1

if rd == g:
    print("Your guess is correct in",count)
elif rd>g:
    print('Its High',count)
elif rd<g:
    print('Its Low',count)
    
    




