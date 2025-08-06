GRADE={}
while True:
    name=input("ENTER STUDENT NAME(q to quit): ")
    if name.lower()=="q":
        break
    score=float(input(f"ENTER {name}'s SCORE: "))
    if score>=90:
        grade="A"
        GRADE[name]=grade
    elif score>=80:
        grade="B"
        GRADE[name]=grade
    elif score>=70:
        grade="C"
        GRADE[name]=grade
    elif score>=60:
        grade="D"
        GRADE[name]=grade
    elif score>=50:
        grade="E"
        GRADE[name]=grade
    else:
        grade="F"
        GRADE[name]=grade

for students,grade in GRADE.items():
   print(f"{students}: {grade}")















