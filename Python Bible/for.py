'''for i in 'abcd':
    print(i)

for j in range(0,11,2):
    print(j)
    '''
vowel=0
vowellist=[]
consonants=0
conslist=[]
print(" we count vowels and consonents")
name=input("enter a word or sentance : ").strip().lower()

for i in name:
    if i in 'abcdefghijklmnopqrstuvwxyz':
        if i in 'aeiou':
            vowel=vowel+1
            vowellist.append(i)
        else:
            consonants=consonants+1
            conslist.append(i)
print('there are Total {} vowals : {}'.format(vowel,vowellist))
print("there are Total {} consonants: {}".format(consonants,conslist))

