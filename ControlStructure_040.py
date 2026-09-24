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