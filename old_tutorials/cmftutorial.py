import numpy as np 
import time

sampleData = open('sampleData.txt', 'r').read()
splitData = sampleData.split('\n')

date,closep,highp,lowp,openp,volume = np.loadtxt(splitData,delimiter=',',unpack=True)

def CHMoF(d,c,h,l,o,v,tf):
    CHMF = []
    MFMs = [] # Money Flow multiplier
    MFVs = [] # Money Flow Volume
    x = tf

    while x < len(d):
        PeriodVolume = 0
        volRange = v[x-tf:x]
        for eachVol in volRange:
            PeriodVolume += eachVol
        
        #Calculate Money Flow Multiplier
        MFM = ((c[x]-l[x])-(h[x]-c[x]))/(h[x]-l[x])

        #Calculate Money Flow Volume
        MFV = MFM*(PeriodVolume)

        #Append the values into their lists

        MFMs.append(MFM)
        MFVs.append(MFV)
        x+=1 # this is to iterate thru the rows
    
    # Next step: Calculate Chaiking Money Flow
    y =tf

    while y < len(MFVs):
        PeriodVolume = 0
        volRange = v[x-tf:x]
        for eachVol in volRange:
            PeriodVolume += eachVol

        consider = MFVs[y-tf:y]
        tfsMFV = 0

        for eachMFV in consider:
            tfsMFV += eachMFV

        tfsCMF = tfsMFV/PeriodVolume
        CHMF.append(tfsCMF)
        
        y+=1
    print (CHMF)

    return date[tf+tf:], CHMF

CHMoF (date,closep,highp,lowp,openp,volume,20)
