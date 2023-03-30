films={
    'Finding dory':[3,2],
    'Bourne':[18,5],
    'Tarzen':[15,5],
    'Ghost Busters':[12,5]
    }
while True:
    choice=input("what movie would you like to watch ? : ").capitalize().strip()
    if choice in films:
        #check if age is old enough
        age=int(input("how old are you ? : ").strip())
        if age >=films[choice][0]:
            #check enough seats
            if films[choice][1]>=1:
                films[choice][1]=films[choice][1]-1
                print("you can watch, enjoy")
                continue
            else:
                print("sorry we sold out")
                break
        else:
            print("you too young")
            break
    else:
        print("We don't have that film")
        break
