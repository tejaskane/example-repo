import random
mylist=['Why is sky blue ? ','why is grass green ? ','who is a gay ? ']
#randomly select a question from list using random.choice() method
answer=input(random.choice(mylist)).strip().lower()
#answer=input(" Why is the sky blue ? :").strip().lower()
while answer!='just because':
    answer=input(" but why ? :").strip().lower()
else:
    print("oh ! ok....")

    
