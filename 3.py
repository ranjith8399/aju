#ranjith
n=input()
if ord(n) in [97,101,105,111,117] :
    print('Vowel')
elif ord(n) not in [97,101,105,111,117]:
    print('Consonant')
else :
    print('Invalid')
