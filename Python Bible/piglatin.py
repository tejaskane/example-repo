#get sentence from the user
print("Welcome to pig latin translator")
sentance=input("Please enter a word or sentance to translate : ").lower().strip()
#split sentence into words
words=sentance.split(' ')
new=[]
c1=''
c2=''
final=''
vowel_pos=0
cons=''
#loop through the words and convert them into pig latin
for i in words:
    if i[0] in 'aeiou'or i[0] in 'AEIOU':
        new.append(i+'yay')
    else:
        for j in i:
            if j not in 'aeiou':
                vowel_pos=vowel_pos+1
            else:
                break
        cons=i[:vowel_pos]
        rest=i[vowel_pos:]
        # print(vowel_pos)
        new.append(rest+cons+'ay')
        '''    c2=c2+j
        new.append(c1+c2+'ay')
        '''
#stick words back to sentence
for w in new:
    final=final+w+' '
# output the final string
print(final)
