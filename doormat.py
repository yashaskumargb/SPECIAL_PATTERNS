q=input().split()
N=int(q[0])
M=(q[1])
M=3*N
c=1
b=list()
for l in range(N):
    if(l==((N-1)/2)):
        msg="ILOVEFANS"
        print(msg.center(M,"-"))
        continue
    elif(l<((N-1)/2)):
        x="-"*(int((M-(3*((2*l)+1)))/2))
        y=".|."*((2*l)+1)
        ms=x+y+x
        print(ms)
        b.append(ms)
    else:#l>n-1/2
        print(b.pop())
        
        
