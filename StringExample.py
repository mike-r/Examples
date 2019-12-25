# StringExample.py

text = input()
if (text.startswith('!1')):
    print('Dynon Skyview ADAHRS Serial Data')
    print('ADAHRS Data version: ', text[2:3])
    print('Time:    ', text[3:5], ':', text[5:7], ":", text[7:9])
    print('Pitch:  ', text[11:15], 'deg')
    print('Roll:   ', text[15:20], 'deg')
    print('Heading: ', text[20:23], 'deg')
    IAS = float(text[23:27])
    IAS = IAS / 10
    print('IAS:     {0:5.1f}'.format(IAS), 'kts')
    pALT = int(text[27:33])
    print('pALT:    {0:,}'.format(pALT), 'ft')
    print('OAT     ', text[49:52], 'deg C')
    TAS = float(text[52:56])
    TAS = TAS / 10
    print('TAS:    {0:5.1f},'.format(TAS), 'kts')
    BARO = float(text[56:59])
    BARO = BARO / 10
    print('BARO:    {0:5.2f}'.format(BARO), 'inHg')
    dALT = int(text[59:65])
    print('dALT:    {0:,}'.format(dALT), 'ft')
elif (text.startswith('!2')):
    print('Dynon Skyview System Serial Data')
    print('System Data version: ', text[2:3])
    print(text[2:-0])
elif (text.startswith('!3')):
    print('Dynon Skkyview EMS Serial Data')
    print('EMS Data version: ', text[2:3])
print(text)


