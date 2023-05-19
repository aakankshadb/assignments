from python_assignments.secondmax_prob.core.utils import *
print("Enter the length of the list")
n=int(input())
lis=[]
for i in range(n):
    item=int(input())
    lis.append(item)
mylis=lis
result=second_max(n,mylis)
print(result)