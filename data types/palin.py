num=546
temp=num
rev=0

while num>0:
    remainder=num%10 # ramainder=3
    rev=rev*10+remainder # 0*10+3=3
    num=num//10 #546//10=54

    remainder=num%10 #remainder=4
    rev=rev*10+remainder # 3*10+4=34
    num=num//10 #54//10 = 5

    remainder=num%10 #remainder= 1
    rev=rev*10+remainder #34*10+1=341
    num=num//10 #5/10=0
print(rev)