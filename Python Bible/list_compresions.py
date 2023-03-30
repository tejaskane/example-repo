#veriable i is defined within the look and used to itrable in range only when divisible by 2
even_num=[i for i in range(1,51) if i %2==0]
print(even_num)
words=['the','quick','brown','fox','jumpes','over','the','lazy','dog']
answer=[[w.upper(),w.lower(),len(w)]
        for w in words]
print(answer)
# o/p [['THE', 'the', 3], ['QUICK', 'quick', 5], ['BROWN', 'brown', 5], ['FOX', 'fox', 3]....]
