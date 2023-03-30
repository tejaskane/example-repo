known_users=['Alice','Bob','Claire','Dan','Emma','Fred','Georgie','Harry']

while True:
    print("Hi! my name is Travis")
    choice=input("Do you want to enter our security system ? (Y/N) ").strip().upper()
    if choice=='Y':
    
        name=input('what is your name ? : ').strip().capitalize()
        if name in known_users:
            print("Hello {}!".format(name))
            remove=input("Would you like to be removed from the system ? (Y/N) : ").strip().upper()
            if(remove=='Y'):
                print(known_users)
                known_users.remove(name)
                print("you are removed")
                print(known_users)
                break
            elif(remove=='N'):
                print(" Ok ")
            else:
                print("invalid option")
                continue
        else:
            print("do you want to be added to this list : {}".format(known_users))
            add=input('Y or N : ').strip().upper()
            if add=='Y':
 #                newname=input('what is your name ? : ').strip().capitalize()
                 known_users.append(name)
                 print("you have been added {}".format(name))
                 print(known_users)
                 break
            elif add=='N':
                print("ok bye")
                break
            else:
                print("invalid selection")
                continue
    else:
        print("ok bye")
        break
    
