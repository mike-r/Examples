# StringExample.py

text = input()
if (text.startswith('!1')):
    print('Dynon Skyview ADAHRS Serial Data')
    print('ADAHRS Data version: ', text[2:3])
    print('Time:    ', text[3:11])
    print('Pitch:  ', text[11:15], 'deg')
    print('Roll:   ', text[15:20], 'deg')
    print('Heading: ', text[20:23], 'deg')
    print('IAS:     ',  text[23:27], 'kts')
    print('pALT:   ',  text[27:33], 'ft')
    print('TAS:     ', text[52:56], 'kts')
elif (text.startswith('!2')):
    print('Dynon Skyview System Serial Data')
    print('System Data version: ', text[2:3])
    print(text[2:-0])
elif (text.startswith('!3')):
    print('Dynon Skkyview EMS Serial Data')
    print('EMS Data version: ', text[2:3])
print(text)


