def calculate_area_triangle(base, height):
    area = (base * height) / 2
    return area
print('Exercise 1:', calculate_area_triangle(10, 5))
print('Exercise 1:', calculate_area_triangle(7, 3))

def calculate_simple_interest (principal, rate, time):
    return(principal * rate * time) / 100 
print('exercise 2:', calculate_simple_interest(1000, 5, 2))

def apply_discount(price, discount): 
    return price * (1 - (discount / 100))
print('Exercise 3:', apply_discount(100, 25))

def convert_temperature(temp, unit):
    if unit == "F":
        return (temp - 32) * 5/9
    elif unit == "C":
        return(temp * 9/5) + 32
print('Exercise 4: Convert 0°C to Fahrenheit:', convert_temperature(0, 'C'))
print('Exercise 4: Convert 32°F to Celsius:', convert_temperature(32, 'F'))

def sum_to(integer):
    total = 0
    for n in range(1, integer + 1):
        total += n
    return total

print('Exercise 5:', sum_to(6))

def find_largest_number(pink, blue, yellow):
    return max(pink, blue, yellow)
print('Exercise 6:', find_largest_number(1, 2, 3))
print('Exercise 6:', find_largest_number(10, 32, 13))

def calculate_tip(amount, tip): 
    tip_amount = amount * tip / 100
    return round(tip_amount)
print('Exercise 7:', calculate_tip(50, 20))

def product(*args):
    result = 1
    for num in args: 
        result *= num 
    return result
print('Exercise 8:', product(2, 5, 5))

def basicCalculator(num1, num2, operation):
    if operation == 'add':
        return num1 + num2
    elif operation == 'subtract':
        return num1 - num2
    elif operation == 'multiply':
        return num1 * num2
    elif operation == 'divide':
        return num1 / num2
print('Exercise 9 Result:', basicCalculator(10, 5, 'subtract'))  
print('Exercise 9 Result:', basicCalculator(10, 5, 'add'))  
print('Exercise 9 Result:', basicCalculator(10, 5, 'multiply'))  
print('Exercise 9 Result:', basicCalculator(10, 5, 'divide')) 
