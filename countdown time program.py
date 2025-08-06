import time

s=int(input("ENTER A TIME IN SECONDS: "))
for s in reversed(range(1,s+1)):
    second= s % 60
    minute= int(s/60) % 60
    hour= int(s/3600)
    if hour>99:
       print("TOO MUCH!")
       break
    else:
        print(f"{hour:02}:{minute:02}:{second:02}")
    time.sleep(1)
print("TIME IS OVER!")

