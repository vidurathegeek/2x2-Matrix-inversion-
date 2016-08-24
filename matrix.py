print("Matrix inverse for 2x2 matrix")
n1=input().strip().split()
n2=input().strip().split()
nlist=n1+n2
a,b,c,d=int(nlist[0]),int(nlist[1]),int(nlist[2]),int(nlist[3])
detA=((a*d)-(b*c))
def adj(A):
    nlist[0],nlist[3]=nlist[3],nlist[0]
    t,s=b*(-1),c*(-1) 
    tlist=[((int(nlist[0]))/detA),(t/detA),(s/detA),((int(nlist[3]))/detA)]
    r=(str(tlist[0])+'\t'+str(tlist[-3])+'\n'+str(tlist[-2])+'\t'+str(tlist[-1]))
    return r
print(adj(nlist))
