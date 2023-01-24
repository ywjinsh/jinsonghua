import random
import time
def game():
    level=int(input('please choice level:(1,easy 2,normal 3,hard 0,exit):'))
    time.sleep(1)
    if level==0:
        return
    elif level==1:
        lev=5
    elif level==2:
        lev=10
    elif level==3:
        lev=15

    n=random.randint(1,lev)
    x=int(input('please guess number 1 to {} :'.format(lev)))
    time.sleep(1)

    r=1
    while x!=0 and r==1:
        if x==n:
            s=input('your guess right do you wang play again(yes or no):')
            if s=='yes':
                game()
            elif s=='no':
                r=0
        elif x>n:
            x=int(input('your guess too large:'))
        elif x<n:
            x=int(input('your guess too small:'))
game()
