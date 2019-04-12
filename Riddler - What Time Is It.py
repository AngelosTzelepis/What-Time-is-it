hourMinute=[]
minuteHour=[]
times=[]
cantTellTime=[]

for i in range(0,1440):
    hour = str(i / 60)
    if len(hour)==1:
        hour = '0'+hour
    minute = str(i % 60)
    if len(minute)==1:
        minute = '0'+minute
    hourHand = (i * 0.5) % 360
    minuteHand = (i * 6.0) % 360
    # Add the hour and minute hand degrees to a list
    hourMinute.append([hourHand,minuteHand])
    # Add the reversed degrees (minute then hour) to a list
    minuteHour.append([minuteHand,hourHand])
    # Add the time string such as 22:17 to a list
    times.append(hour+':'+minute)    

i = 0
for item in hourMinute:
    # Check all the degree combos in hourMinute to see if they can exist in reverse in minuteHour
    # If they do, that's a potentially confusing time
    if hourMinute[i] in minuteHour:
        cantTellTime.append(times[i])
        print i, times[i],hourMinute[i]
    i += 1