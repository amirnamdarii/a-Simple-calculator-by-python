def sum_of_two(a, b):
    return a + b
def minus_of_two(a, b):
    return a - b
def multiply_of_two(a, b):
    return a * b
def divide_of_two(a, b):
    if b == 0:
        print("Invalid, Zero Division")
    return a / b

print("Hello Guys Welcome To My Calculator! \n")
print("Ok so! Give me an two numbers I can calcualte them:/ \n")

while True:
    try:
        a = float(input("Give me your 1st number: \n"))
        operator = input("Choose an operator +, -, *, /: \n")
        b = float(input("Give me 2nd number!: \n"))
    
        if operator == "+":
            print(f"Your Result is: {sum_of_two(a, b) + sum_of_two(a, b)}!")
        elif operator == "-":
            print(f"Your Result is: {minus_of_two(a, b) - minus_of_two(a, b)}!")
        elif operator == "*":
            print(f"Your Result is: {multiply_of_two(a, b) * multiply_of_two(a, b)}")
        elif operator == "/":
            print(f"Your Result is: {divide_of_two(a, b) / divide_of_two(a, b)}")
        else:
            print("Invalid! Please Choose from : +, -, *, /")

        play_again = input("Do you want to play again? (y/n)\n").strip().lower()
        if play_again != "y" or "Y":
            print("Thanks for using my calculator")
            print("Goodbye!")
            print("-", end=" ")
            break
    except ZeroDivisionError:
            print("Invalide Please Just Choose from: +, -, *, /")