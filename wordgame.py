print('\nHello!!! Welcome to WORD GAME')
word1="Speed"
word=word1.lower()
life=len(word)
print(f"You have {life} chances for this unknown word")
for i in range(life):
    print('_',end=' ')
print('\n')
g1=str()
while(life>0):
    guess=str(input('\nEnter a guessing character or word : ')).lower()
    if(guess not in word):
        life -=1
        print(f'You r WRONG and {life} chances is left')
    if(life==0):
        print('\nSORRY :( u LOSE')
        print(f'The Word is {word}')
        break
    wrong=0
    g1=g1+guess
    for i in word:
        if(i in g1):
            print(i,end=' ')
        else:
            print('_',end=' ')
            wrong +=1
    if(wrong==0):
        print('\nUUURRRREEEE!!!!!!!   YOU   WON')
        break
