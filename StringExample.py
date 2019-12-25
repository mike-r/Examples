# StringExample.py

text = input()
if (text.startswith('!1')):
    print('Time:    ', text[3:11])
    print('Pitch:  ', text[11:15])
    print('Roll:   ', text[15:20])
    print('Heading: ', text[20:23])
    print('IAS:     ',  text[23:27])
    print('pALT:   ',  text[27:33])
    print('TAS:     ', text[52:56])
elif (text.startswith('!2')):
 print(text)


