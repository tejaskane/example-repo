# get user email address
email=input("what is your email address ? : ").strip()
# slice out user name
# name = email[:email.index('@')] # eyerything until @ is your username
fn = email[:email.index('.')].capitalize()
ln =  email[email.index('.')+1:email.index('@')].capitalize()
name = fn + ' ' + ln
# slice out company name
placeholder=email.index('@')+1 # since from @ also display @ we add 1 for index position next to @
company = email[placeholder:email.index('.com')].capitalize() # after @ until .com is our company name

# display output message
print("your name is {}".format(name))
print("you work for {}".format(company))

#output example
'''what is your email address ? : tejas.babu@kyndryl.com
your name is Tejas Babu
you work for Kyndryl'''
