# ---Task 1 (Digital Root Sequence)---

n = int(input("Please enter a positive integer greater than 9: "))

while n <=9 :
    n = int(input("Please enter a positive integer greater than 9: "))


steps = 0
print(n, end="")

while n>9:

    temp =n
    sum = 0

    while temp > 0:

        sum = sum + temp%10
        temp = temp // 10 

    n= sum
    steps = steps+1
    print(" -> ", n, end="")

print()
print("Final value: ",n)
print("Total steps:", steps)




# ---Task 2 (FizzBuzz Counter)---

m = int(input("\nPlease enter a number between 10 and 100: "))

while m<10 or m>100:
    print("Invalid input. Please enter a number between 10 and 100: ")
    m= int(input())


fizz =0
buzz =0
fizzbuzz =0

for i in range(1, m+1):

    if i%7 ==0:

        print("(", i, "is skipped)", sep="")
        continue

    if i%3 ==0 and i%5 ==0:
        print("FizzBuzz")
        fizzbuzz +=1
    
    elif i%3 ==0 :
        print("Fizz")
        fizz +=1

    elif i%5 ==0:
        print("Buzz")
        buzz +=1

    else:
        print(i)


print("--- Summary ---")
print("Fizz count : ", fizz)
print("Buzz count : ", buzz)
print("FizzBuzz count: ", fizzbuzz)




# ---Task 3---

x = int( input("\nPlease enter a number between 3 and 9: "))

while x<3 or x>9:
    x = int( input("Please enter a number between 3 and 9: "))

for i in range(1, 2*x):

    y = x - abs(x-i)

    for j in range(1,y+1):
        print(j, end="")

    print()

