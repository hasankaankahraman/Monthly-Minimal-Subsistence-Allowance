
"""HASAN KAAN KAHRAMAN"""
"""192010010065"""


minimumwage = float(input("Enter minimum wage. ="))

marriage = int(input("Enter 1 if you are married and 0 if you are single. ="))

if marriage == 1:
    marriage = 'The Married'

    wifeworking = int(input("Enter 1 if your spouse is working, 0 if not.="))

    if wifeworking == 1:
        wifeworkingrate = 0
        workstatus = 'Wife is working. '

        numberofchildren = float(input("Enter the number of children. ="))

        if numberofchildren == 0:
            rateofchildren = 0
            howmanykids = 0
        elif numberofchildren == 1:
            rateofchildren = 7.5
            howmanykids = 1
        elif numberofchildren == 2:
            rateofchildren = 15
            howmanykids = 2
        elif numberofchildren == 3:
            rateofchildren = 25
            howmanykids = 3
        elif numberofchildren == 4:
            rateofchildren = 30
            howmanykids = 4
        elif numberofchildren == 5:
            rateofchildren = 35
            howmanykids = 5
        else:
            rateofchildren = 35
            howmanykids = 'More than 5'

    elif wifeworking == 0:
        wifeworkingrate = 10
        workstatus = 'Wife is not working.'

        numberofchildren = float(input("Enter the number of children. ="))

        if numberofchildren == 0:
            rateofchildren = 0
            howmanykids = 0
        elif numberofchildren == 1:
            rateofchildren = 7.5
            howmanykids = 1
        elif numberofchildren == 2:
            rateofchildren = 15
            howmanykids = 2
        elif numberofchildren == 3:
            rateofchildren = 25
            howmanykids = 3
        else:
            rateofchildren = 25
            howmanykids = 'More than 3'
    else:
        print("Please enter a valid case.")

elif marriage == 0:
    marriage = 'Not Married'
    wifeworkingrate = 0
    workstatus = 0

    numberofchildren = float(input("Enter the number of children.="))

    if numberofchildren == 0:
        rateofchildren = 0
        howmanykids = 0
    elif numberofchildren == 1:
        rateofchildren = 7.5
        howmanykids = 1
    elif numberofchildren == 2:
        rateofchildren = 15
        howmanykids = 2
    elif numberofchildren == 3:
        rateofchildren = 25
        howmanykids = 3
    elif numberofchildren == 4:
        rateofchildren = 30
        howmanykids = 4
    elif numberofchildren == 5:
        rateofchildren = 35
        howmanykids = 5
    else:
        rateofchildren = 35
        howmanykids = 'More than 5'
else:
    print("Please enter a valid case.")



msap = (50 + rateofchildren + wifeworkingrate)
MMSA = ((minimumwage * 12 * 0.15 / 12) * (msap / 100))


print("*********************")
print("Monthly Minimal Subsistence Allowance")

print('Minimum Wage :', minimumwage)
print('Marriage     :', marriage)
if marriage == 'The Married':
    print('Work Status       :', workstatus)
    print('How Many Chilren? :', howmanykids)
elif marriage == 'Not Married.':
    print("How Many Chilren? :", howmanykids)
print('Rate of Children  : %', rateofchildren)
print("Wife Working Rate : %", wifeworkingrate)
print("MSAP = %50 + Rate of Children + Wife Working Rate ")
print('MSAP : %', msap)
print('MMSA : ', round(MMSA, 2))