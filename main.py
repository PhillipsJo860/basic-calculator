# Joshua Phillips
# 10/8/24
# Basic Calculator

# Input
print("""Hello and thank you for using this basic calculator, remember though its VERY basic and can only do the folllowing:
    1. Addition, 
    2. Subtraction, 
    3. Multiplication, 
    4. Division.""")
operator = int(input("Which math operator mentioned previously would you like to use today? Enter a number 1-4 to represent adding, subtracting, multiplying, and dividing in order: "))
first_num = int(input("Please enter the first number: "))
second_num = int(input("Please enter the second number: "))

# Process
add = first_num + second_num
sub = first_num - second_num
multi = first_num * second_num
divi = first_num / second_num



# Output
if operator == 1:
    print(f"{first_num} + {second_num} = {add}.")
elif operator == 2:
    print(f"{first_num} - {second_num} = {sub}.")
elif operator == 3:
    print(f"{first_num} * {second_num} = {multi}.")
elif operator == 4:
    print(f"{first_num} / {second_num} = {divi}.")
else:
    print("Please try typing the operator number again the number you entered was not on our list of operators.")
    
