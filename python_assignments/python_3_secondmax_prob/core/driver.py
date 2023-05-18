from python_assignments.python_3_secondmax_prob.core.utils import *
n=int(input())
lis=[]
for i in range(n):
    item=int(input())
    lis.append(item)
result=second_max(n,lis)