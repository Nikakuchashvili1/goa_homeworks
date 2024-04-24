# input("დაწერეთ რიცხვი")
# if input== 5:
#     print (input ())
# elif input == 2:
#     print(input)





# password = "saidumlo"
# guess = "1234"
# print( guess != password)


password =str(input("crate your password:  "))
password2 =str(input("enter your password:  "))
while not password2 == password:
    print("incorrect! try again")
    password2 =str (input(" enter your password:   "))
else:
    print("acces granted")