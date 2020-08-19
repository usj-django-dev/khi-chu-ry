#Main gate security system
#First of all it ask the strangers to tell their name
#Onle family member are allowed
#if their name matches any members name then it write its name and say welcome _________(name)
#next ask password if it is correct write access is granted otherwise access is denaied







print('What is your name?')
myname = input()
if myname == 'Utsho':
    print('Welcome Utsho')
elif myname == 'Adri':
    print('Welcome Adri')
elif myname == 'Sharmistha':
    print('Welcome Sharmistha')
elif myname == 'Sushil':
    print('Welcome Sushil')
elif myname == 'Joyanti':
    print('Welcome Joyanti')
else:
    print('Are you a pig?')

print('Type the password')
password = input()

if password == 'obeygod':
    print('Access Granted')
else:
    print('Access denied')

