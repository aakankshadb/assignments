from python_assignments.mutations_prob.core.utils import *
print("Enter the string:")
string=input()
print("Enter the character:")
character=input()
print("Enter the position:")
position=input()
new_string=mutate_string(string,position,character)
print(new_string)
