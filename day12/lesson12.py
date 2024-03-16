#დავალება 1
grade = int(input ("enter your grade: "))
if grade > 90 and grade < 100:
    print("თქვენ დაგიფინანსდებათ სწავლა სრულიად") 
elif grade > 70  and grade < 80:
    print("თქვენ დაგიფინანსდებათ სწავლა 1500 ლარით")
elif grade > 40  and grade < 70:
    print("თქვენ დაგიფინანსდებათ სწავლა 500 ლარით")
elif grade > 40:
    print("თქვენ არ დაგიფინანსდებათ სწავლის პროცესი")
else:
    print("100 ქულიანი შეფასების სისტემაა :)")
#დავალება 2
points = int(input("enter your points: "))
if points == 10:
    print("შექება")
elif points == 9 or points == 8:
    print("პატარა შენიშვნა")
elif points == 5:
    print("შენიშვნა")
elif points < 5:
    print("სკოლიდან გაგდება")
else:
    print("10 ქულიანი სისტემაა")
