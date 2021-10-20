#This program calculates the working zones
maxbpm = -999
minbpm = 999
zone5 = 0
zone4 = 0
zone3 = 0
numberActivities = 0

age = int(input("How old are you:"))
maxTheoricalBpm = 220 - age

while True:
    bpm = int(input("Bpm value:"))
    if bpm == 0:
        break

    if bpm > maxbpm:
        maxbpm = bpm
    if bpm < minbpm:
        minbpm = bpm

    if bpm > maxTheoricalBpm*0.9:
        zone5 += 1
    elif bpm > maxTheoricalBpm*0.8:
        zone4 += 1
    elif bpm > maxTheoricalBpm*0.7:
        zone3 += 1   
    numberActivities += 1

#Print the results
print("Results:")
print("Zone3 >(",maxTheoricalBpm*0.7,") :", round(zone3/numberActivities*100,2), "%" )
print("Zone4 >(",maxTheoricalBpm*0.8,") :", round(zone4/numberActivities*100,2), "%" )
print("Zone5 >(",maxTheoricalBpm*0.9,") :", round(zone5/numberActivities*100,2), "%" )
print("Max pbm:",maxbpm)
print("Min pbm:",minbpm)






