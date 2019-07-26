#ra.ku
n=int(input())
temp=n
rev=0
while n>0 and n<=1000 :
    inter=n%10
    rev=rev*10+inter
    n=n//10
if temp==rev:
    print('yes')
else:
    print('no')
