students={
    'male':['Tejas','Dan','Bob','Tom','Frank'],
    'female':['Alice','Samanta','Sarah','Ellie','Maggie']
    }
for i in students.keys():
    for j in students[i]:
        #print students who has 'a' in their name
        if 'a' or 'A' in j:
            print(j)
