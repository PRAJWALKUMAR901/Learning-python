MARKS={}
name=input("Enter your student's name: ")
while True:
    subject=input("Enter a subject(q to quit): ")
    if subject.lower() == "q":
        break
    marks=float(input(f"Enter {subject} marks: "))
    score=marks*2.5
    MARKS[subject]=score
print()
print()
print(f"{name}'s marks is as below")
print()
for subject, score in MARKS.items():
    print(f"{subject}= {score}")
percent=sum(MARKS.values())/len(MARKS)
print(f"{name}'s percentage = {percent}")
if percent >= 90:
    print()
    print("OUTSTANDING!!!!")
elif percent >= 85:
    print()
    print("GOOD!!")
elif percent >= 80:
    print()
    print("OK")
elif percent >= 70:
    print()
    print("BELOW AVERAGE??")
elif percent >= 60:
    print()
    print("BAD????")
else:
    print()
    print("GO READ 24 HOURS YOU DUMBBBBB")


