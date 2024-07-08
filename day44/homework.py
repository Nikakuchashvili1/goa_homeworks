#    For Loop:

# # 1) Print all integers from 0 to 20 inclusive.

for i in range(0,21):
     print(i)

# # 2) Print the first 10 natural numbers

for i in range(0, 10):
     print(i)


print("Even numbers from 0 to 100:")
for i in range(0, 101, 2):
    print(i, end=" ")
print()

# 4) Enter a number to the user and then using a for loop output the sum of all the numbers 
# up to this number (for example, if he enters 10, output the sum of all the numbers up to 10, for example).

num = int(input("Enter a number: "))
sum_numbers = 0
for i in range(1, num + 1):
    sum_numbers += i
print(f"The sum of all numbers from 1 to {num} is: {sum_numbers}")

# 5) Write an algorithm that prints multiples of 5 (numbers divisible by 5) from 1 to 50 inclusive


num = 5
while num <= 50:  
    print(num) 
    num += 5  

# While Loop:

# 1) Print even numbers up to 20.
num = 2  

while num <= 20:  
    print(num)  
    num += 2  

# 2) calculate the sum of numbers from 1 to 10.
sum_numbers = 0
for i in range(1, 11):
    sum_numbers += i 
print("The sum of numbers from 1 to 10 is:", sum_numbers)

# 3) Write a while loop that asks the user to guess a number between 1 and 10 until they get it right. The correct number is 7.
correct_number = 7
while True:
    guess = int(input("Guess a number between 1 and 10: "))
    if guess == correct_number:
        print("Congratulations! You guessed the correct number.")
        break 
    else:
        print("Sorry, that's not the correct number. Please try again.")

# 4) Write a while loop that processes a list of numbers, doubling each number, and prints the new list.
numbers = [1, 2, 3, 4, 5]
doubled_numbers = []

index = 0

while index < len(numbers):
    doubled_numbers.append(numbers[index] * 2)
    index += 1

print("Original list of numbers:", numbers)
print("Doubled list of numbers:", doubled_numbers)


# 5) Write a while loop that repeatedly asks the user to enter a password until the correct password "password123" is entered.


correct_password = "password123"
user_input = ""
while user_input != correct_password:
    user_input = input("Enter the password: ")
    
    if user_input == correct_password:
        print("Correct password entered. Access granted.")
    else:
        print("Incorrect password. Please try again.")


# If - Else:
# 1) Write an if-else statement that prints "Good morning!" if the current hour is less than 12 and "Good afternoon!" otherwise.

import datetime
current_hour = datetime.datetime.now().hour

if current_hour < 12:
    print("Good morning!")
else:
    print("Good afternoon!")
    # 2) Write an if-else statement that checks if a number is even or odd. If the number is even, print "Even"; otherwise, print "Odd."
def even_or_odd(number):
    if number % 2 == 0:
        print("Even")
    else:
        print("Odd")
number = 17  
even_or_odd(number)

# 3) Create an if-else statement to check if the temperature is 
# above 30 degrees. If it is, print "It's hot outside!"; otherwise, print "It's not too hot."

temperature = 32 
if temperature > 30:
    print("It's hot outside!")
else:
    print("It's not too hot.")




# 4) Create an if-else statement that determines if a person is a teenager. If the age is between 13 and 19 (inclusive), print 
# "You are a teenager!"; otherwise, print "You are not a teenager."

def is_teenager(age):
    if age >= 13 and age <= 19:
        print("You are a teenager!")
    else:
        print("You are not a teenager.")
age = 16  

is_teenager(age)