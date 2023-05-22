from collections import namedtuple

def named_tuple(N,Id, Marks, Name, Class):
    Student = namedtuple("Student", [Id, Marks, Name, Class])
    total = 0
    for i in range(N):
        Id, Marks, Name, Class = input().split()
        stud_info = Student(Id, Marks, Name, Class)
        total += int(stud_info.Marks)
    avg =total/N
    print(format(avg, '.2f'))
