print('What is your name?')
myname = input()
if myname == 'Sharmistha':
    print('Welcome Sharmistha')
elif myname == 'Nushu':
    print('Welcome Nushu')
elif myname == 'Sukanta':
    print('Welcome Sukanta')
elif myname == 'Reem':
    print('Welcome Reem')
elif myname == 'Nipa':
    print('Welcome Nipa')
else:
    print('You are not a nwu student!')

print('Are you affected in COVID-19?')
corona_affected = input()

if corona_affected == 'yes':
    print('You can not enter in the univerity')
    print('\n')
    print('Stay Home')
    print('Stay Safe')
else:
    print('You can enter in the univerity')
