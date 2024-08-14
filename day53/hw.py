# 1) შექმენით კალკულატორის ფუნქცია  რომელიც მომხმარებელს შეეკითხება ორ რიცხვს და მოქმედების 
# ტიპს(მიმატება, გამოკლება, გამრავლება, გაყოფა) შესაბამისად ფუნქცია დააბრუნებს ანუ დაბეჭდავს შედეგს 
# იმისდამიხედვით მომხმარებელს რა სურს და რა რიცხვები შემოიტანა, მაგალითად მომხმარებელმა თუ შემოიტანა 5 და 2 და ასევე მას 
# სურს გამრავლება ფუნქციამ უნდა დააბრუნოს დაბეჭდოს შედეგად 2 * 5 ანუ 10


# def calculator():
#     try:
#         num1 = float(input("Enter the first number: "))
#         num2 = float(input("Enter the second number: "))
#     except ValueError:
#         print("Invalid input. Please enter numeric values.")
#         return

#     operation = input("Enter the operation (addition, subtraction, multiplication, division): ").strip().lower()
#     if operation == "addition":
#         result = num1 + num2
#         print(f"{num1} + {num2} = {result}")
#     elif operation == "subtraction":
#         result = num1 - num2
#         print(f"{num1} - {num2} = {result}")
#     elif operation == "multiplication":
#         result = num1 * num2
#         print(f"{num1} * {num2} = {result}")
#     elif operation == "division":
#         if num2 == 0:
#             print("Error: Division by zero is not allowed.")
#         else:
#             result = num1 / num2
#             print(f"{num1} / {num2} = {result}")
#     else:
#         print("Invalid operation. Please choose from addition, subtraction, multiplication, or division.")



# 2) შექმენით ფუნქცია რომელშიც იქნება რიცხვებით სავსე სია და ფუნქცია დააბრუნებს ამ რიცხვების ჯამს

# def sum_of_numbers(numbers):
#     return sum(numbers)


# 3) შექმენით ფუნქცია რომელშიც დააბრუნებს სიაში არსებული რიცხვების საშუალო არითმეტიკულ

# def arithmetic_mean(numbers):
#     if not numbers:
#         return 0 
#     total_sum = sum(numbers)
#     count = len(numbers)
#     return total_sum / count

# 4) შექმენით ფუნქცია რომელიც მომხმარებელს შეეკითხება რიცხვს და შემდეგ კი 
# დააბრუნებს დაბეჭდავს მომხმარებლის შემოტანილი რიცხვი კენტია თუ ლუწი

# def check_odd_or_even():
#     try:
#         number = int(input("Enter a number: "))
#     except ValueError:
#         print("Invalid input. Please enter an integer.")
#         return
#     if number % 2 == 0:
#         print(f"{number} is even.")
#     else:
#         print(f"{number} is odd.")

#    5) შექმენით დროში მოგზაურობის ფუნქცია რომელიც მომხმარებელს შეეკითხება მის 
# ახლანდელ ასაკს და ამჟამინდელ წელს, ასევე რამდენი ხანით სურს დროშ მოგზაურობა შემდეგ კი 
# ფუნქციამ უნდა დააბრუნოს დაბეჭდოს დროში მოგზაურობის შემდეგ რომელი წელი იქნება და 
# რამდენი წლის იქნება მომხმარებელი, ასევე დაამატეთ რომ მომხმარებელმა მიიღოს 
# გადაწყვეტილება წარსულში სურს დრში მოგზაურობა თუ მომავალში

def time_travel():
    try:
        current_age = int(input("Enter your current age: "))
        current_year = int(input("Enter the current year: "))
    except ValueError:
        print("Invalid input. Please enter integer values.")
        return
    try:
        years_to_travel = int(input("Enter how many years you want to time travel: "))
    except ValueError:
        print("Invalid input. Please enter an integer value for years.")
        return
    direction = input("Do you want to travel forward or backward in time? (Enter 'forward' or 'backward'): ").strip().lower()

    if direction not in ['forward', 'backward']:
        print("Invalid direction. Please enter 'forward' or 'backward'.")
        return

    if direction == 'forward':
        future_year = current_year + years_to_travel
        future_age = current_age + years_to_travel
    else: 
        future_year = current_year - years_to_travel
        future_age = current_age - years_to_travel
    print(f"After traveling {years_to_travel} years {direction}, it will be the year {future_year}.")
    print(f"You will be {future_age} years old.")