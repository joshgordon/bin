import time
warning=True
try: 
  from terminal import *
# This uses the terminal library from: 
# http://nadiana.com/python-curses-terminal-controller
# Go download it from there and put it in the same dir as this
# if you want to be fancy! 
except: 
  warning=False


currentTime = time.time()  #get the current time...
currentTime += 60 * 14 #14 minutes to fall asleep. 
print "If you go to bed now, you should wake up at:" 


wakeUpTimes = list() #make a list of times to wake up. Still as float here... 

#Do the next 6 wake up times...
for i in range(1, 7): 
  wakeUpTimes.append(currentTime + 5400 * i) #add 1.5 hours * the number
						   #of cycles.  

#If we're doing pretty print output: 
if (warning): 
  # Make the output look nice. 
  for WUtime in wakeUpTimes: 
    if WUtime - currentTime <= 16200: 
      print BG_RED + WHITE + time.strftime("%I:%M%p" , time.localtime(WUtime)) + NORMAL 
    elif WUtime - currentTime <= 21600: 
      print BG_YELLOW + time.strftime("%I:%M%p" , time.localtime(WUtime)) + NORMAL 
    else: 
      print BG_GREEN + time.strftime("%I:%M%p" , time.localtime(WUtime)) +  NORMAL 
else: 
  # Make the output look nice. 
  for WUtime in wakeUpTimes: 
    print time.strftime("%I:%M %p" , time.localtime(WUtime)) 


#Tell user to go to bed! 
if warning: 
  print render('%(BOLD)sNOW GO TO BED%(NORMAL)s') 
else:
  print "NOW GO TO BED!" 

