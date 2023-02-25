import random

for i in range(0,10):
    number= random.randint(25,35)
    print (number)


print("------------------------------------------------------")
for i in range(0,10):
    number= random.randrange(1,100,2)
    print (number)


print("------------------------------------------------------")
lists=['sunday','monday','tuesday','wednesday','thursday','Friday','saturday']

number= random.choice(lists)
print(number)

print("------------------------------------------------------")

import math

# Set the number of iterations for the approximation
iterations = 1000000

# Initialize the variables
pi_approx = 0
sign = 1

# Compute the approximation using the Leibniz formula for pi
for i in range(iterations):
    pi_approx += sign * 4 / (2 * i + 1)
    sign = -sign

# Print the approximation and the value of pi from the math module
print("Approximation of pi:", pi_approx)
print("Value of pi from math module:", math.pi)

print("------------------------------------------------------")

# Prompt the user to input a value in radians
radians = float(input("Enter a value in radians: "))

# Convert radians to degrees using the formula
degrees = radians * 180 / math.pi

# Print the calculated value and the value from the math module
print("Calculated value in degrees:", degrees)
print("Value in degrees from math module:", math.degrees(radians))


print("------------------------------------------------------")


# Prompt the user to input a value
n = int(input("Enter a positive integer: "))

# Calculate the factorial using a for loop
factorial = 1
for i in range(1, n+1):
    factorial *= i

# Print the calculated value and the value from the math module
print("Calculated factorial:", factorial)
print("Factorial from math module:", math.factorial(n))
