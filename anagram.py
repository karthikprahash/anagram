# anagram
i=int(input())
f=[]
e=['a','a','b','i','k','l']
c=0
for s in range(0,i):
    f.append(list(input()))
for i in f:
    b=sorted(i)
    if b==e:
        c=c+1
               
print(c)
            
