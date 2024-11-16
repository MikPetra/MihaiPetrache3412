import math
import cmath

def sum_nat():
    sum = 0
    for i in range(1, 101):
        sum += i
    print("Sum of first 100 natural nrs is:",sum)

def show_odd_nr():
    odd = 0
    n = 100
    odd_nr = []
    for i in range(1,100):
        while (odd <=20):
            if i%2 == 1:
                odd_nr.append(i)
            i += 1
            odd += 1
    print("first 20 odd nrs are:", odd_nr)

def biggest_divizor():
    a = int(input("Enter the first number: "))
    b = int(input("Enter the second number: "))

    while b:
        a,b = b, a % b
    print("the greatest common divisor is:",a)

def prime():
    number = int(input("Enter the number: "))
    if number < 2:
        print(f"{number} is not a prime number.")
        return
    for i in range(2, int(math.sqrt(number)) + 1):
        if number % i == 0:
            print(f"{number} is not a prime number.")
            return
    print(f"{number} is a prime number.")

def sum_and_average():
    numbers = input("Enter numbers separated by spaces: ").split()
    numbers = [int(num) for num in numbers]
    total_sum = sum(numbers)
    #This is needed for math sense purposes :)
    average = total_sum / len(numbers) if numbers else 0
    print("Sum:", total_sum)
    print("Average:", average)

def can_form_triangle():
    a = float(input("Enter the first side: "))
    b = float(input("Enter the second side: "))
    c = float(input("Enter the third side: "))
    if a + b > c and a + c > b and b + c > a:
        print("The numbers can form the sides of a triangle.")
    else:
        print("The numbers cannot form the sides of a triangle.")

def bubble_sort():
    numbers = input("Enter numbers separated by spaces: ").split()
    numbers = [int(num) for num in numbers]
    n = len(numbers)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if numbers[j] > numbers[j + 1]:
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
                swapped = True
        if not swapped:
            break
    print("Sorted list:", numbers)

def day_of_week():
    day_number = int(input("Enter a number (1-7) to get the day of the week: "))
    days = {
        1: "Monday",
        2: "Tuesday",
        3: "Wednesday",
        4: "Thursday",
        5: "Friday",
        6: "Saturday",
        7: "Sunday"
    }
    if day_number in days:
        print("The day is:", days[day_number])
    else:
        print("Invalid input! Please enter a number between 1 and 7.")   

def find_max():
    numbers = input("Enter numbers separated by spaces: ").split()
    numbers = [int(num) for num in numbers]
    max_value = max(numbers)
    print("The maximum value is:", max_value)

def solve_quadratic():
    a = float(input("Enter coefficient a: "))
    b = float(input("Enter coefficient b: "))
    c = float(input("Enter coefficient c: "))

    discriminant = b**2 - 4*a*c

    if discriminant > 0:
        root1 = (-b + cmath.sqrt(discriminant)) / (2 * a)
        root2 = (-b - cmath.sqrt(discriminant)) / (2 * a)
        print("The equation has two real roots:", root1.real, "and", root2.real)
    elif discriminant == 0:
        root = -b / (2 * a)
        print("The equation has one real root:", root)
    else:
        root1 = (-b + cmath.sqrt(discriminant)) / (2 * a)
        root2 = (-b - cmath.sqrt(discriminant)) / (2 * a)
        print("The equation has two complex roots:", root1, "and", root2)

sum_nat()
show_odd_nr()
biggest_divizor()
prime()
sum_and_average()
can_form_triangle()
bubble_sort()
day_of_week()
find_max()
solve_quadratic()