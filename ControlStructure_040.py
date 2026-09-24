performance = input("Please enter your performance")

if performance >= "90":
    print("Excellent")
elif performance >= "80":
    print("Very Good Performance")
elif performance >= "70":
    print("Good Performance")
elif performance >= "60":
    print("Then Average Performance")
    
for steps in range(1,4):
        print(steps)
        
import math
batas = math.factorial(10)
a, b = 0, 1
while a <= batas:
    print(a)
    a, b = b, a + b
    
    n = 5

import math
n = 5
batas = math.factorial(n)
for i in range(1, batas + 1, 2):
    print(i)
    
n = 5
for i in range(1, n + 1):
    print(f"{i} " * i)